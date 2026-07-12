from lib import Trie
import sys
from typing import Optional


"""
TODO:
- 일단 Trie부터 구현하기
- count 구현하기
- main 구현하기
"""


def count(trie: Trie, query_seq: str) -> int:
    """
    trie - 이름 그대로 trie
    query_seq - 단어 ("hello", "goodbye", "structures" 등)

    returns: query_seq의 단어를 입력하기 위해 버튼을 눌러야 하는 횟수
    """
    pointer = 0
    cnt = 0

    for element in query_seq:
        if len(trie[pointer].children) > 1 or trie[pointer].is_end:
            cnt += 1

        new_index: Optional[int] = None
        for child_idx in trie[pointer].children:
            if trie[child_idx].body == element:
                new_index = child_idx
                break

        assert new_index is not None
        pointer = new_index

    return cnt + int(len(trie[0].children) == 1)


def main() -> None:
    lines = sys.stdin.readlines()
    idx = 0

    while idx < len(lines):
        n = int(lines[idx])
        idx += 1

        words = []
        for _ in range(n):
            words.append(lines[idx].strip())
            idx += 1

        trie: Trie[str] = Trie()
        for word in words:
            trie.push(word)

        total = 0
        for word in words:
            total += count(trie, word)

        average = total / n
        print(f"{average:.2f}")
    pass


if __name__ == "__main__":
    main()
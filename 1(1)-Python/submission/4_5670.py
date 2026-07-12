from dataclasses import dataclass, field
from typing import TypeVar, Generic, Optional, Iterable


"""
TODO:
- Trie.push 구현하기
- (필요할 경우) Trie에 추가 method 구현하기
"""


T = TypeVar("T")


@dataclass
class TrieNode(Generic[T]):
    body: Optional[T] = None
    children: list[int] = field(default_factory=lambda: [])
    is_end: bool = False


class Trie(list[TrieNode[T]]):
    def __init__(self) -> None:
        super().__init__()
        self.append(TrieNode(body=None))

    def push(self, seq: Iterable[T]) -> None:
        """
        seq: T의 열 (list[int]일 수도 있고 str일 수도 있고 등등...)

        action: trie에 seq을 저장하기
        """
        current = 0

        for element in seq:
            found = None

            for child_idx in self[current].children:
                if self[child_idx].body == element:
                    found = child_idx
                    break
            if found is not None:
                current = found

            else:
                new_node = TrieNode(body=element)
                self.append(new_node)
                new_idx = len(self) - 1
                self[current].children.append(new_idx)
                current = new_idx

        self[current].is_end = True
        pass

    # 구현하세요!


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
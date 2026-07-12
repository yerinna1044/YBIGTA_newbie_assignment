from lib import Trie
import sys


"""
TODO:
- 일단 lib.py의 Trie Class부터 구현하기
- main 구현하기

힌트: 한 글자짜리 자료에도 그냥 str을 쓰기에는 메모리가 아깝다...
"""

MOD = 1_000_000_007

def factorial_mod(n: int) -> int:
    result = 1
    for i in range(1, n + 1):
        result = (result * i) % MOD
    return result


def main() -> None:
    input_data = sys.stdin.readlines()
    n = int(input_data[0])
    names = [input_data[i + 1].strip() for i in range(n)]

    trie: Trie[str] = Trie()
    for name in names:
        trie.push(name)

    answer = 1
    for node in trie:
        child_count = len(node.children)
        if node.is_end:
            child_count += 1
        answer = (answer * factorial_mod(child_count)) % MOD

    print(answer)
    pass


if __name__ == "__main__":
    main()
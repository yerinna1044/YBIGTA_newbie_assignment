from lib import SegmentTree
import sys


"""
TODO:
- 일단 SegmentTree부터 구현하기
- main 구현하기
"""


def main() -> None:
    lines = sys.stdin.readlines()
    n = int(lines[0])

    MAX_TASTE = 1_000_000
    tree = SegmentTree([0] * MAX_TASTE, lambda a, b: a + b, 0, lambda x: x)

    results = []
    for i in range(1, n + 1):
        query = list(map(int, lines[i].split()))

        if query[0] == 1:
            k = query[1]
            taste_index = tree.find_kth(1, 0, MAX_TASTE - 1, k)
            results.append(taste_index + 1)
        else:
            b, c = query[1], query[2]
            index = b - 1
            current = tree.query(index, index)
            tree.update(index, current + c)

    print('\n'.join(map(str, results)))
    pass


if __name__ == "__main__":
    main()
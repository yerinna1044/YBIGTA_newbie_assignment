from lib import SegmentTree
import sys


"""
TODO:
- 일단 SegmentTree부터 구현하기
- main 구현하기
"""


def main() -> None:
        lines = sys.stdin.readlines()
        idx = 0
        t = int(lines[idx])
        idx += 1

        results = []
        for _ in range(t):
            n, m = map(int, lines[idx].split())
            idx += 1
            queries = list(map(int, lines[idx].split()))
            idx += 1

            total = n + m
            data = [0] * total
            for i in range(1, n + 1):
                data[m + i - 1] = 1

            tree = SegmentTree(data, lambda a, b: a + b, 0, lambda x: x)

            pos = [0] * (n + 1)
            for i in range(1, n + 1):
                pos[i] = m + i - 1

            top_pointer = m - 1

            answer = []
            for movie in queries:
                p = pos[movie]
                count_above = tree.query(0, p - 1)
                answer.append(str(count_above))

                tree.update(p, 0)
                tree.update(top_pointer, 1)
                pos[movie] = top_pointer
                top_pointer -= 1

            results.append(' '.join(answer))

        print('\n'.join(results))
        pass


if __name__ == "__main__":
    main()
from __future__ import annotations

from dataclasses import dataclass, field
from typing import TypeVar, Generic, Optional, Callable, cast


"""
TODO:
- SegmentTree 구현하기
"""


T = TypeVar("T")
U = TypeVar("U")


class SegmentTree(Generic[T, U]):
    def __init__(self, data: list[T], func: Callable[[U, U], U], identity: U, transform: Callable[[T], U]) -> None:
        self.n = len(data)
        self.func = func
        self.identity = identity
        self.transform = transform
        self.tree: list[U] = [identity] * (4 * self.n)
        self._build(data, 1, 0, self.n - 1)

    def _build(self, data: list[T], node: int, start: int, end: int) -> None:
        if start == end:
            self.tree[node] = self.transform(data[start])
            return
        
        mid = (start + end) // 2
        self._build(data, node * 2, start, mid)
        self._build(data, node * 2 + 1, mid + 1, end)
        self.tree[node] = self.func(self.tree[node * 2], self.tree[node * 2 + 1])

    def _update(self, node: int, start: int, end: int, index: int, value: U) -> None:
        if start == end:
            self.tree[node] = value
            return
        
        mid = (start + end) // 2
        if index <= mid:
            self._update(node* 2, start, mid, index, value)
        else:
            self._update(node * 2 + 1, mid + 1, end, index, value)

        self.tree[node] = self.func(self.tree[node * 2], self.tree[node * 2 + 1])
        
    def _query(self, node: int, start:int, end: int, l: int, r: int) -> U:
        if r < start or end < l:
            return self.identity
        
        if l <= start and end <= r:
            return self.tree[node]
        
        mid = (start + end) // 2
        left_result = self._query(node * 2, start, mid, l, r)
        right_result = self._query(node * 2 + 1, mid + 1, end, l, r)
        return self.func(left_result, right_result)
    
    def update(self, index: int, value: T) -> None:
        self._update(1, 0, self.n - 1, index, self.transform(value))

    def query(self, l: int, r: int) -> U:
        return self._query(1, 0, self.n - 1, l, r)


    def find_kth(self, node: int, start: int, end: int, k: int) -> int:
        if start == end:
            self.tree[node] = cast(U, cast(int, self.tree[node]) - 1)
            return start

        mid = (start + end) // 2
        left_count = cast(int, self.tree[node * 2])
        if left_count >= k:
            result = self.find_kth(node * 2, start, mid, k)
        else:
            result = self.find_kth(node * 2 + 1, mid + 1, end, k - left_count)

        self.tree[node] = self.func(self.tree[node * 2], self.tree[node * 2 + 1])
        return result

    pass


import sys


"""
TODO:
- 일단 SegmentTree부터 구현하기
- main 구현하기
"""


class Pair(tuple[int, int]):
    """
    힌트: 2243, 3653에서 int에 대한 세그먼트 트리를 만들었다면 여기서는 Pair에 대한 세그먼트 트리를 만들 수 있을지도...?
    """
    def __new__(cls, a: int, b: int) -> 'Pair':
        return super().__new__(cls, (a, b))

    @staticmethod
    def default() -> 'Pair':
        """
        기본값
        이게 왜 필요할까...?
        """
        return Pair(0, 0)

    @staticmethod
    def f_conv(w: int) -> 'Pair':
        """
        원본 수열의 값을 대응되는 Pair 값으로 변환하는 연산
        이게 왜 필요할까...?
        """
        return Pair(w, 0)

    @staticmethod
    def f_merge(a: 'Pair', b: 'Pair') -> 'Pair':
        """
        두 Pair를 하나의 Pair로 합치는 연산
        이게 왜 필요할까...?
        """
        return Pair(*sorted([*a, *b], reverse=True)[:2])

    def sum(self) -> int:
        return self[0] + self[1]

def main() -> None:
    lines = sys.stdin.readlines()
    idx = 0

    n = int(lines[idx])
    idx += 1

    arr = list(map(int, lines[idx].split()))
    idx += 1

    m = int(lines[idx])
    idx += 1

    tree = SegmentTree(
        arr,
        Pair.f_merge,
        Pair.default(),
        Pair.f_conv
    )
    results = []

    for _ in range(m):
        query = list(map(int, lines[idx].split()))
        idx += 1

        if query[0] == 1:
            i, v = query[1], query[2]
            tree.update(i - 1, v)
        else:
            l, r = query[1], query[2]
            result_pair = tree.query(l - 1, r - 1)
            results.append(str(result_pair.sum()))

    print('\n'.join(results))
    pass


if __name__ == "__main__":
    main()
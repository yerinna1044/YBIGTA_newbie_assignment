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
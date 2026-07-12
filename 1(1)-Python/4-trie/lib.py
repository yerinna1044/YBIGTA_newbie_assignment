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
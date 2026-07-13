from collections import Counter
from typing import List


class MinHeap:
    def __init__(self) -> None:
        self._data: list[tuple[int, int]] = []

    def __len__(self) -> int:
        return len(self._data)

    def push(self, item: tuple[int, int]) -> None:
        self._data.append(item)
        self._sift_up(len(self._data) - 1)

    def pop(self) -> tuple[int, int]:
        last = len(self._data) - 1
        self._data[0], self._data[last] = self._data[last], self._data[0]
        item = self._data.pop()
        if self._data:
            self._sift_down(0)
        return item

    def _sift_up(self, i: int) -> None:
        while i > 0:
            parent = (i - 1) // 2
            if self._data[i] < self._data[parent]:
                self._data[i], self._data[parent] = (
                    self._data[parent],
                    self._data[i],
                )
                i = parent
            else:
                break

    def _sift_down(self, i: int) -> None:
        n = len(self._data)
        while True:
            smallest = i
            left = 2 * i + 1
            right = 2 * i + 2
            if left < n and self._data[left] < self._data[smallest]:
                smallest = left
            if right < n and self._data[right] < self._data[smallest]:
                smallest = right
            if smallest == i:
                break
            self._data[i], self._data[smallest] = (
                self._data[smallest],
                self._data[i],
            )
            i = smallest


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = MinHeap()

        for num, freq in count.items():
            heap.push((freq, num))
            if len(heap) > k:
                heap.pop()

        return [num for _, num in heap._data]


if __name__ == "__main__":
    solution = Solution()

    tests = [
        ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
        ([1], 1, [1]),
        ([4, 1, -1, 2, -1, 2, 3], 2, [-1, 2]),
        ([5, 5, 5, 5, 1, 1, 2], 2, [5, 1]),
    ]

    passed = 0
    for idx, (nums, k, expected) in enumerate(tests, 1):
        actual = solution.topKFrequent(nums, k)
        ok = sorted(actual) == sorted(expected)
        passed += ok
        status = "OK" if ok else "FAIL"
        print(
            f"[{idx}] {status}  nums={nums}  k={k}  "
            f"actual={actual}  expected={expected}"
        )

    print(f"\n{passed}/{len(tests)} passed")

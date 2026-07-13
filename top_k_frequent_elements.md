# input
integer array nums; integer k

# output
the k most frequent elements in nums, in any order

# steps
1. count how many times each number appears in nums
2. use a min heap of size k to keep the k highest frequencies
3. push (frequency, number) into the heap; if heap size exceeds k, pop the smallest frequency
4. return the numbers left in the heap

# requirements
1. write a python function, test it yourself, and put the code into top_k_frequent_elements.py
2. start with: def topKFrequent(self, nums: List[int], k: int) -> List[int]:

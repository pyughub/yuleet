# input
string s (lowercase English letters)

# output
integer list (length of each partition fragment, in order)

# steps
1. record the last index of each character in s
2. scan s from left to right; maintain the end index of the current fragment
3. at index i, extend the fragment end to max(end, last[s[i]])
4. when i == end, the fragment is complete; append its length (end - start + 1) and start the next fragment at i + 1
5. reminder: each letter may appear in at most one fragment; concatenating all fragments in order must equal s

# requirements
1. write a python function, test it yourself, and put the code into partition_labels.py
2. start with: def partitionLabels(self, s: str) -> List[int]:

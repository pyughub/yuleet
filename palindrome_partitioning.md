# input
string s

# output
various partitions that can divide s into palindromes, organized in array form.

# steps
1. single out the first character and divide the rest; if all partitions are found, see if the first character can be bound in a longer palindrome. if so, divide the rest by repeating the process(recurse)
2. put all partitions into an array and return it.
3. palindrome check: reverse the string and see if it still remains the same.

# requirements
1. write a python function, test it yourself, and put the code into palindrome_partitioning.py
2. start with: def partition(self, s: str) -> List[List[str]]:
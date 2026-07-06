# input
string s(length between 0 and 5*10^4; made up of english letters, numbers, empty spaces and signs)

# output
an integer, the length of the longest substring without repeating characters

# steps(see s as an array)
1. i=0 j=1 len=1
2. while j<len(s):
    check if the substring from s[i] to s[j] has repeating characters
    if so then:
        i++
    else:
        len = j-i+1
        j++

3. return len

# requirements
1. write a python function, test it yourself, and put the code into longest_substring_without_repeating_characters.py
2. start with: def lengthOfLongestSubstring(self, s: str) -> int:
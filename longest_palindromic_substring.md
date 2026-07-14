# input
string s

# output
a string(the longest palindromic substring of s; any one is fine if multiple exist)

# steps
1. use a 2D dp where dp[i][j] means whether s[i..j] is a palindrome; init all diagonal dp[i][i]=True
2. for length-2: if s[i]==s[i+1], set dp[i][i+1]=True and track the longest
3. for length from 3 to n: dp[i][j] is True when s[i]==s[j] and dp[i+1][j-1]; keep updating the longest substring
4. return s[start:start+max_len]

# requirements
1. write a python function, test it yourself, and put the code into longest_palindromic_substring.py
2. start with: def longestPalindrome(self, s: str) -> str:

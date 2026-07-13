# input
a string s and a string array wordDict

# output
boolean value(whether s can be broken into pieces that exist in wordDict)

# steps
1. search for all strings in wordDict that start with the first letter of s
2. for each, go to the first letter in s beyond the string and repeat step1 and step2
3. if able to cover s, return True; else go for the next string choice.
4. return False if unable to break s into wordDict pieces.

# requirements
1. write a python function, test it yourself, and put the code into word_break.py
2. start with: def wordBreak(self, s: str, wordDict: List[str]) -> bool:
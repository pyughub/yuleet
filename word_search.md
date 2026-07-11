# input
an m*n board of characters, organized in array form; a string word

# output
boolean value(whether the word can be found in board)

# steps
1. start from the first character of word and find it in board; then search the four(or two or three) surrounding characters and see if any matches the second character
2. go on until you find the whole word. all the letters must be connected and in order
3. use backtrack if there are multiple choices and return true once finding one that fits. 

# requirements
1. write a python function, test it yourself, and put the code into word_search.py
2. start with: def exist(self, board: List[List[str]], word: str) -> bool:
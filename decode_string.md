# input
a coded string

# output
a decoded string

# steps
1. iterate through the string character by character until you meet a number(followed closely a left bracket)
2. create a stack starting with the number until you meet a right bracket to match the left one; pop and reverse the order of letters popped out and repeat it according to the number that comes out last
3. within a pair of brackets, you mar encounter another number indicating a deeper repetition. deal with it the same way
4. return the decoded string.

# requirements
1. write a python function, test it yourself, and put the code into decode_string.py
2. start with: def decodeString(self, s: str) -> str:
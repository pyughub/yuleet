## Implement class Trie:

## steps
# __init__
self.val: the character-order(an integer, 0 to 25, matching the 26 lowercase letters one to one) stored in this node
self.leaves: a 26 element array made up of 26 nodes (corresponding to the 26 lowercase letters or None)
self.isEnd: boolean value, indicating if this character is the end of a complete word

# insert
iterate through the word and find the correct node to create a new branch. make isEnd=true for the final character

# search
go through the characters of the word one by one and see if each can find a node. if so and finalcharacter.isEnd==true, return true else false 

# startsWith
same as search except that finalcharacter.isEnd does not need to be true.

## requirements
1. write a python function, test it yourself, and put the code into implement_trie_prefix_tree.py
2. start with: class Trie:

    def __init__(self):
        

    def insert(self, word: str) -> None:
        

    def search(self, word: str) -> bool:
        

    def startsWith(self, prefix: str) -> bool:
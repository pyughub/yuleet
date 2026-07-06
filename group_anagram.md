# input
string array strs(length between 1 and 10^4, each string component between 0 and 100 lowercase letters long)

# output
a rearranged array made up of string arrays, putting the anagrams in groups

# steps 
1. iterate through the array and create a dictionary linking its alphabetically ordered version(key) to itself(value)
2. for each string, check if its alphabetically ordered version can match any of the keys in the dictionary. if so, put them together in a new array. in the end, a new array contains all the strings who are anagrams of each other.
3. integrate these new string arrays into one big array and return the big array

# requirements
1. write a python function and put the code into group_anagram.py
2. start with def groupAnagrams(self, strs: List[str]) -> List[List[str]]: 
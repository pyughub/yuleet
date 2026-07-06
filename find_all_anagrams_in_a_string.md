# input
two strings s and p containing lowercase letters; len(s) >=1; len(p) <= 3*10^4

# output
an integer array, containing all the starting indexes of substrings of s that are anagrams of p

# steps
1. ana_ind=[] if len(s)<len(p):                return ana_ind
2. iterate through s, check all substrings that are len(p) long and see if they are anagrams of p; if so then: ana_ind.append(the index of the first letter of the substring) (skip those that contain a letter not in p)
3. return ana_ind

# requirements
1. write a python function, test it yourself, and put the code into .py
2. start with:
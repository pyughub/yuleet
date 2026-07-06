# input
integer array nums(length between 0 and 10^5; integer between -10^9 and 10^9)

# output
an integer(the length of the longest consecutive sequence)

# steps
1. create a dictionary.
2.  FOR num in nums:
        IF num (>= any key & < value of the key):
            continue
        IF num==(value of an existing entry):
            (value of an existing entry)+=1 
        ELSE:
            create a new entry for it, linking it(key) to the number larger than it by one(value). 
            IF the new value==any existing key:
                merge the two entries, linking the existing key to the new value and remove the entry contaning the existing key; 
            ELSE:
                let it be as it is.
3. return the largest gap between every key and value

# requirements
1. write a python function and put the code into longest_consecutive_sequence.py
2. start with: def longestConsecutive(self, nums: List[int]) -> int:
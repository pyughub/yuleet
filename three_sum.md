# input
integer array nums(length between 3 and 3000; integers between -10^5 and 10^5)

# output
an array of three-integer arrays

# steps
1. sort nums in ascending order
2. i=0 j=len(nums)-1 three_sum=[]
3. while i<j and num[i]<=0:
    s=num[i]+num[j]
    for k in range(len(nums)):
        if k==i or k==j:
            continue
        if s>0:
            if -s == num[k]:
                three_sum.append([num[i],num[j],num[k]])
            j--
        else:
            if -s == num[k]:
                three_sum.append([num[i],num[j],num[k]]) 
    i++

4. remove identical arrays from three_sum, leave only one for each
5. return three_sum

# requirements
1. write a python function and put the code into three_sum.py
2. start with:def threeSum(self, nums: list[int]) -> list[list[int]]:
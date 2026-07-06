# input
integer array nums

# output
an integer array

# steps
1. products = []
2. iterate through the array, products.append(product) (product equals the product of nums[0] to nums[i-1] times the product of nums[i+1] to nums[len(nums)-1]; self-adapt to index border restrictions)
3. return products

# requirements
1. write a python function, test it yourself, and put the code into .py
2. start with:

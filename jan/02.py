# Good morning! Here's your coding interview problem for today.
# This problem was asked by Uber.
# Given an array of integers, return a new array such that each element at index i 
# of the new array is the product of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If 
# our input was [3, 2, 1], the expected output would be [2, 3, 6].
# Follow-up: what if you can't use division?

def product_of_array(arr):
    product = 1
    for i in arr:
        product *= i
    return [product // i for i in arr]

print(product_of_array([1, 2, 3, 4, 5]))
print(product_of_array([3, 2, 1]))

assert(product_of_array([3, 2, 1]) == [2, 3, 6])
assert(product_of_array([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24])
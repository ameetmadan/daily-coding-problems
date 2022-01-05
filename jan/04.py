# Good morning! Here's your coding interview problem for today.
# This problem was asked by Stripe.
# Given an array of integers, find the first missing positive integer in linear time and constant space. 
# In other words, find the lowest positive integer that does not exist in the array. The array can contain 
# duplicates and negative numbers as well.
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
# You can modify the input array in-place.

def find_missing_positive_integer(arr):
    # The idea is to use the array as a hash table and iterate through the array
    # to mark the position of the integer in the hash table.
    # If the integer is negative, ignore it.
    # If the integer is positive, mark it in the hash table.
    # If the integer is not in the hash table, return the integer.
    # If the integer is in the hash table, ignore it.
    # If the array is empty, return 1.
    if len(arr) == 0:
        return 1
    hash_table = {}
    for i in range(len(arr)):
        if arr[i] > 0:
            hash_table[arr[i]] = True
    for i in range(1, len(arr) + 2):
        if i not in hash_table:
            return i
    return len(arr) + 1

# print(find_missing_positive_integer([3, 4, -1, 1]))
assert(find_missing_positive_integer([3, 4, -1, 1]) == 2)
assert(find_missing_positive_integer([1, 2 ,0]) == 3)
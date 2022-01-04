# Good morning! Here's your coding interview problem for today.
# This problem was asked by Uber.
# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
# Follow-up: what if you can't use division?

def product_of_array(array):
    # create a new array with the same length as the input array
    new_array = [0] * len(array)
    # iterate through the input array
    for i in range(len(array)):
        # set the first element of the new array to 1
        if i == 0:
            new_array[i] = 1
        # set the last element of the new array to 1
        elif i == len(array) - 1:
            new_array[i] = 1
        # set the current element of the new array to the product of all the elements in the input array except the current element
        else:
            new_array[i] = array[i-1] * array[i+1]
    return new_array

print(product_of_array([1, 2, 3, 4, 5]))
assert(product_of_array([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24])
print(product_of_array([3, 2, 1]))
assert(product_of_array([3, 2, 1]) == [2, 3, 6])
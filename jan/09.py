# Good morning! Here's your coding interview problem for today.

# This problem was asked by Airbnb.

# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

# Follow-up: Can you do this in O(N) time and constant space?

def largest_sum(numbers):
    if len(numbers) == 0:
        return 0
    if len(numbers) == 1:
        return numbers[0]
    if len(numbers) == 2:
        return max(numbers[0], numbers[1])
    if numbers[0] > numbers[1]:
        return largest_sum(numbers[1:]) + numbers[0]
    else:
        return largest_sum(numbers[1:]) + numbers[1]

assert(largest_sum([2, 4, 6, 2, 5]) == 13)
print(largest_sum([2, 4, 6, 2, 5]))
assert(largest_sum([5, 1, 1, 5]) == 10)
print(largest_sum([5, 1, 1, 5]))
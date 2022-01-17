# Good morning! Here's your coding interview problem for today.

# This problem was asked by Amazon.

# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

def longest_substring(k, s):
    longest = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if len(set(s[i:j])) <= k:
                longest = max(longest, len(s[i:j]))
    return longest

print(longest_substring(2, "abcba"))
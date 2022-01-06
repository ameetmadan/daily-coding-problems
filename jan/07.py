# Good morning! Here's your coding interview problem for today.

# This problem was asked by Facebook.

# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

# You can assume that the messages are decodable. For example, '001' is not allowed.

def decode(s):
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    if len(s) == 2:
        if int(s) <= 26:
            return 2
        else:
            return 1
    if int(s[:2]) <= 26:
        return decode(s[1:]) + decode(s[2:])
    else:
        return decode(s[1:])

print(decode('111'))
assert(decode('111') == 3)
print(decode('12'))
print(decode('123'))
print(decode('1234'))
print(decode('12345'))
print(decode('123456'))
print(decode('1234567'))
print(decode('12345678'))
print(decode('123456789'))
print(decode('1234567890'))
print(decode('12345678901'))
print(decode('123456789012'))
print(decode('1234567890123'))
print(decode('12345678901234'))
print(decode('123456789012345'))
print(decode('1234567890123456'))
print(decode('12345678901234567'))
print(decode('123456789012345678'))
print(decode('1234567890123456789'))
print(decode('12345678901234567890'))
print(decode('123456789012345678901'))
print(decode('1234567890123456789012'))
print(decode('12345678901234567890123'))
print(decode('123456789012345678901234'))
print(decode('1234567890123456789012345'))
print(decode('12345678901234567890123456'))
print(decode('123456789012345678901234567'))
x = 11
# 11 in Binary is 1011

y = 5
# 5 in Binary is 0101

# Bitwise AND : both bits are 1 => 1 otherwise 0
a = x & y
# x = 1011
# y = 0101
# a = 0001
# a = 1

print(a)
# 1

# Bitwise OR : either bits are 1 => 1 otherwise 0
b = x | y
# x = 1011
# y = 0101
# b = 1111
# b = 15

print(b)
# 15

# Bitwise XOR : both bits MUST be different => 1 otherwise 0
c = x ^ y
# x = 1011
# y = 0101
# c = 1110
# c = 14

print(c)
# 14

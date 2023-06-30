def singleNumber(nums: list[int]) -> int:
    result = 0
    for num in nums:
        result ^= num
    return result


y = 10
y &= 4
print(y)

# a = 10 = 1010 (Binary)
# b = 4 =  0100 (Binary)

# a & b = 1010
#          &
#         0100
#       = 0000
#       = 0 (Decimal)

x = 10
x |= 4
print(x)
# a = 10 = 1010 (Binary)
# b = 4 =  0100 (Binary)

# a | b = 1010
#          |
#         0100
#       = 1110
#       = 14 (Decimal)


a = 10
# a = 10 = 1010 (Binary)
print(~a)
b = 2
print(~b)
# a = 10 = 1010 (Binary)

# In computers we usually represent numbers using 32 bits,
# so binary representation of 10 is (....0000 1010)[32 bits]

# ~a is basically 1's complement of a 
# i.e ~a should be ~10 = ~(....0000 1010) = (....1111 0101) = intermediate-result

# Since bitwise negation inverts the sign bit,
# we now have a negative number. And we represent a negative number
# using 2's complement.

# 2's complement of intermediate-result is:
# intermediate-res =  0101      //....1111 0101
      
#                      1010      //....0000 1010 -(1's complement)
#                          +1    
#                  -----------
#                    =  1011      //....0000 1011
#                   -----------
#                    =   -11 (Decimal)
                   
# thus ~a = -11

a = 10
b = 4
print(a ^ b)
# a = 10 = 1010 (Binary)
# b = 4 =  0100 (Binary)

# a ^ b = 1010
#          ^
#         0100
#       = 1110
#       = 14 (Decimal)
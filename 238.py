from functools import reduce
from math import prod
# # Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# # The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# # You must write an algorithm that runs in O(n) time and without using the division operation.

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]



    # sonuc listesi olusturcaz
    # tüm elemanlarin carpimini bir degere atariz
    # her elemana geldigimizde o elemana bölümü bize o haric tüm elemanlarin carpimini verir
    # eger sayi negatif veya kendisine esitse 0
    # degilse sonucu ekliyecek




def product_except_self(nums: list[int]) -> list[int]:
    # bölme olmasin dedigi icin prefix postfix yoluyla yapacagiz
    # 1,2,3,4: 
    # 1
    # 1,2
    # 1,2,3
    # 1,2,3,4
    # post:
    # 4,
    # 3,4
    # 2,3,4
    # 1,2,3,4
    
    
    n = len(nums)
    prefix = [1] * n
    suffix = [1] * n
    result = [1] * n

    # Önek çarpımlarını hesaplayın
    for i in range(1, n):
        prefix[i] = prefix[i - 1] * nums[i - 1]

    # Sonek çarpımlarını hesaplayın
    for i in range(n - 2, -1, -1):
        suffix[i] = suffix[i + 1] * nums[i + 1]

    # Sonuç listesini hesaplayın
    for i in range(n):
        result[i] = prefix[i] * suffix[i]

    return result
# print(product_except_self([1,2,3,4]))
# print(product_except_self([-1,1,0,-3,3]))

def perfect_productExceptSelf(nums: list[int]) -> list[int]:
    res = [1] * len(nums)
    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
    postfix = 1
    for i in range(len(nums)-1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    return res

print(perfect_productExceptSelf([1,2,3,4]))
print(perfect_productExceptSelf([-1,1,0,-3,3]))



def zero_or_sub(prod, val):
    if val != 0:
        return 0
    return prod

def productExceptSelf(nums: list[int]) -> list[int]:
    prod = 1
    prod_without_zeros = 1
    has_multiple_zeros = False
    has_one_zero = False

    for i in nums:
        if i == 0 and has_one_zero:
            has_multiple_zeros = True
        elif i == 0:
            has_one_zero = True
        else:
            prod_without_zeros *= i

        prod *= i

    if has_multiple_zeros:
        return [0 for i in nums]

    if has_one_zero:
        return [zero_or_sub(prod_without_zeros, i) for i in nums]
    
    return [int(prod / i) for i in nums]

print(productExceptSelf([1,2,3,4]))
print(productExceptSelf([-1,1,0,-3,3]))
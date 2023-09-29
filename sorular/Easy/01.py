# 1. Two Sum

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]


#! SOLUTION 1
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None


a = [2, 7, 11, 15]
b = 9
# print(twoSum(a, b))

a = [3, 2, 4]
b = 6
# print(twoSum(a, b))


#! SOLUTION 2


def twoSum2(nums, target):
    d = {}
    for i, v in enumerate(nums):
        diff = target - v
        if diff in d:
            return [d.get(diff), i]
        d[v] = i


print(twoSum2(a, b))

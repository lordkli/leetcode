# 53. Maximum Subarray

# Given an integer array nums, find the 
# subarray
#  with the largest sum, and return its sum.



# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

def maxSubArray(self, nums: List[int]) -> int:
        arr = []
        arr.append(nums[0])
        maxSum = arr[0]
        for i in range(1, len(nums)):
            arr.append(max(arr[i-1] + nums[i], nums[i]))
            # if arr[i] > maxSum then maxSum = arr[i].
            if arr[i] > maxSum:
                maxSum = arr[i]
        return maxSum       # Return the contiguous subarray which has the largest sum...
    
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
      maxV = nums[0]
      toplam = 0
      for i in nums:
          toplam += i
          #if max < toplam:
          #    max = toplam
          maxV = max(maxV, toplam)
          if toplam < 0:
              toplam = 0
      return maxV
# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.

def findMin(nums: list[int]) -> int:
    res = nums[0]
    l, r = 0, len(nums) - 1
    
    while l <= r:
        if nums[l] < nums[r]:
            res = min (res, nums[l])
            break
        
        m = (l + r) // 2
        res = min(res,nums[m])
        if nums[m] >= nums[l]:
            l = m + 1
        else:
            r = m - 1
    return res

print(findMin([3,4,5,1,2]))



def findMin2(nums: list[int]) -> int:
    # binary search 
    l, r = 0, len(nums) - 1

    while l < r:
        m = (l + r) // 2

        if nums[m] > nums[r]:
            # We know that the pivot must be to the right
            # 4 5 6 7 8 9 10 0 1 2 3
            #           m
            l = m + 1
            
        else:
                # We know that we're at the pivot, or the pivot is to the left
                r = m 

    return nums[l]    

print(findMin2([3,4,5,1,2]))
print(findMin2([11,13,15,17]))

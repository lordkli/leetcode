def maxSubArray(nums: list[int]) -> int:
    maxSub = nums[0]
    curSum = 0
    
    for n in nums:
        if curSum < 0:
            curSum = 0
        curSum += n
        maxSub = max(maxSub, curSum)
    return maxSub

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))



def maxSubArray2(nums: list[int]) -> int:

    s=0
    m=nums[0]
    for i in nums:
        s+=i
        if s>m:m=s
        if s<0: s=0
    return m

print(maxSubArray2([-2,1,-3,4,-1,2,1,-5,4]))
def maxProduct( nums: list[int]) -> int:
    # if all positives, multiply all numbers
    # if all negatives 
    #       an even number of the array, multiply all numbers
    # maintain max and min
    res = max(nums)
    curMin, curMax = 1, 1
    
    for n in nums:
        if n == 0:
            curMin, curMax = 1, 1
            continue
        tmp = curMax * n
        curMax = max(n * curMax, n * curMin, n)
        curMin = min(tmp, n * curMin, n)
        res = max(res, curMax)
    return res

print(maxProduct([2,3,-2,4]))
print(maxProduct([-2,0,-1]))
print(maxProduct([-4,-3,-2]))
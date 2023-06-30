# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

    #! explain the approach
    # ilk elemandan baslayarak sogaindaki elemanlarla tek tek toplamak
    # toplamlari targeta esitse 
    # o elemanlarin indexini listeye eklemek

def twoSum(nums: list[int], target: int) -> list[int]:
    prevMap = {} # val : index
    
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i
    return

print(twoSum([2,7,11,15], 9))


def twoSum2(nums: list[int], target: int) -> list[int]:
    for i, n in enumerate(nums):
        for j, m in enumerate(nums[i+1:]): 
            if n + m == target:
                return [i, j+i+1]
    return

print(twoSum2([2,7,11,15], 9))

def twoSum3(nums: list[int], target: int) -> list[int]:
    myHashMap = {}
    for ix, num in enumerate(nums):
        diff = target - num
        if diff in myHashMap:
            return [myHashMap[diff], ix]
        myHashMap[num] = ix
    return

print(twoSum3([2,7,11,15], 9))
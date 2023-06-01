def findDuplicate(self, nums: list[int]) -> int:
    slowPointer = 0
    fastPointer = 0
    
    while True:
        slowPointer = nums[slowPointer]
        fastPointer = nums[nums[fastPointer]]
        if slowPointer == fastPointer:
            break
    
    slowPointer = 0
    while True:
        slowPointer = nums[slowPointer]
        fastPointer = nums[fastPointer]
        if slowPointer == fastPointer:
            return slowPointer
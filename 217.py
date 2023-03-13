def containsDuplicate(nums: list[int]) -> bool:
    setim = set()
    for i in nums:
        if i in setim:
            return True
        setim.add(i)
    return False

print(containsDuplicate([1,2,3,1]))
print(containsDuplicate([1,2,3,4]))

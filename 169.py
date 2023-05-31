def majorityElement(nums: list[int]) -> int:
    number = {}
    res = 0
    max_counter = 0
    for i in nums:
        if i not in number:
            number[i] = 1
        else:
            number[i] += 1
    for key, value in number.items():
        if value > max_counter:
            max_counter = value
            res = key
    return res

print(majorityElement([3,2,3]))
print(majorityElement([2,2,1,1,1,2,2]))
print(majorityElement([1]))


def boyerMoore(nums: list[int]) -> int:
    result = 0
    count = 0
    
    for num in nums:
        if count == 0:
            result = num
        count += 1 if num == result else -1
        # if num == result:
        #     count += 1
        # else:
        #     count -= 1
    return result

print(boyerMoore([3,2,3]))
print(boyerMoore([2,2,1,1,1,2,2]))
print(boyerMoore([1]))

def majorityElementWithSort(nums: list[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
    
print(majorityElement([3,2,3]))
print(majorityElement([2,2,1,1,1,2,2]))
print(majorityElement([1]))
    # nums = [1,3,0,0,2,0,0,4]
    # nums = [0,0,0,2,0,0]
    # nums = [2,10,2019]
    # kümeler = []
    # c = 0
    # for i in nums:
    #     if i == 0:
    #         c += 1
    #     else:
    #         kümeler.append(c)
    #         c = 0
    # kümeler.append(c)

    # print(kümeler)
    # 1
    # toplam = 0
    # for i in kümeler:
    #     toplam += (i * (i+1)) // 2

    # print(toplam)
    
    

def zeroFilledSubarray(nums: list[int]) -> int:
    ans, count = 0, 0
    for num in nums:
        if num:
            count = 0
        else:
            count += 1
        ans += count
    
    return ans

print(zeroFilledSubarray([1,3,0,0,2,0,0,4]))
print(zeroFilledSubarray([0,0,0,2,0,0]))
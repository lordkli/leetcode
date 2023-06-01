def leastBricks2(wall: list[list[int]]) -> int:
    myHashMap = {}
    for row in wall:
        sum = 0
        for i in range(len(row) - 1):
            sum += row[i]
            myHashMap[sum] = myHashMap.get(sum, 0) + 1
    return len(wall) - max(myHashMap.values(), default=0)

def leastBricks(wall: list[list[int]]) -> int:
    myHashMap = {0: 0} #key: ix, value -> gap
    
    for row in wall:
        gapIndex = 0
        for brick in row[:-1]:
            gapIndex += brick
            myHashMap[gapIndex] += 1 + myHashMap.get(gapIndex, 0)
    maximumGapNumber = max(myHashMap.values(), default=0)
    rowNumber = len(wall)
    return rowNumber - maximumGapNumber
    
print(leastBricks([[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]))


def leastBricks(self, wall: list[list[int]]) -> int:
        countGap = {0 : 0}

        for r in wall:
            total = 0

            for b in r[:-1]:
                total += b

                countGap[total] = 1 + countGap.get(total, 0)

        return len(wall) - max(countGap.values())
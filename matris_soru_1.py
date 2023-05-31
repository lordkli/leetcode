def solution(sayi:int)-> list[list[int]]:
    deger = 10
    temp = deger
    azalis = 2
    matris = [[0 for x in range(4)] for y in range(sayi)]
    for i in range(sayi):
        for j in range(4):
            matris[i][j] = temp
            temp -= azalis
        deger += 10
        temp = deger
        azalis += 1
    return matris

print(solution(6))

# matris = [[4,5,2,1,3], [3,4,5,2,1], [2,3,4,5,2],[7,2,3,4,5]]
matris = [[4,5,2,1,3], [3,4,5,2,1], [2,3,4,5,2],[7,2,3,4,5]]

# print(len(matris))      4
# print(len(matris[0]))   5
res = bool
for i in range(len(matris)-1):
    for j in range(len(matris[0])-1):
        if matris[i][j] == matris[i+1][j+1]:
            res = True
        else:
            res = False

print(res)

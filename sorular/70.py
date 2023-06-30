import math
n = 8
res = 0

for i in range(n//2 + 1):
    res += math.comb(n-i,i)

print(res)
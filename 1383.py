n = 7
speed =      [1,4,1,9,4,4,4]
efficiency = [8,2,1,7,1,8,4]
k = 6

def solution(n,speed,efficiency,k):
    # max = sum(speed)/min(efficiency)
    # max = 0
    indis = 0
    removed = []
    gmax = 0
    while(len(removed)<n-1):
        max = 0
        indis = 0
        for i in [j for j in range(n) if j not in removed]:
            a = parcaSonuc(removed+[i], speed, efficiency)
            if a > max: 
                max = a
                indis = i
                if (n-len(removed)-1)<=k and gmax < max:
                    gmax = max
                    
        removed.append(indis)
        print(max)
        print(removed)
    
    return gmax
    
def parcaSonuc(list, speed, efficiency):
    summation = 0
    for i in range(len(speed)):
        if i not in list:
            summation+=speed[i]
    
    return summation * min([efficiency[i] for i in range(len(efficiency)) if i not in list])

print(solution(n,speed,efficiency,k))
# print(parcaSonuc([0,2,3,5], speed, efficiency))
def calculateFunction(x):
    if x == 0:
        return 1
    else:
        return x * calculateFunction(x-1)

print(calculateFunction(5))

def calculateContigiousSum(num):
    if num == 0:
        return 0
    else:
        return num + calculateContigiousSum(num-1)
    
print(calculateContigiousSum(5))
print(calculateContigiousSum(7))
print(calculateContigiousSum(8))
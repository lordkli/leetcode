def fib(n):
    x, y = 0, 1
    for i in range(n):
        x, y = y, x + y
    return x

memo ={}

def memoizationSolution(n):
    if n not in memo:
        memo[n] = fib(n)
    return memo[n]

numList = [5, 10, 15, 5, 20, 15,5,10,5,100,100,15,5,10]

for num in numList:
    memoizationSolution(num)

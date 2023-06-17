# 1 1 2 3 5 8 13

def f(n):
    if n == 0 or n == 1:
        return n
    else:
        return f(n-1) + f(n-2)

print(f(4))
print(f(6))
print(f(7))

def iterativfibbonacci(n):
    x, y = 0, 1
    for i in range(n):
        x, y = y, x + y
    return x

print(iterativfibbonacci(4))
print(iterativfibbonacci(6))
print(iterativfibbonacci(7))
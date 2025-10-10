# n tane girilen sayinin ekokunu bulma

def ebob(x, y):
    # 12, 6  6 12
    # 6, 12  6 12
    # 3, 13  1 39
    while y:
        temp = x
        x = y
        y = temp % y
    return x

# print(ebob(12, 6))
# print(ebob(6, 12))
# print(ebob(3, 13))
# print(ebob(2,4))

def ekok(x, y):
    return (x * y) / ebob(x,y)

def main(n):
    ls = []
    for i in range(n):
        inp = input(str(i + 1) + ". sayiyi giriniz= ")
        ls.append(int(inp))
    
    result = ls[0]
    
    for i in range(1, len(ls)):
        result = ekok(result, ls[i])
    
    return result

print(main(3))




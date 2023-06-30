input = ["h","e","l","l","o"]
# output = ["o","l","l","e","h"]

result = []
i = len(input) - 1
while i >= 0:
    result += input[i]
    i -= 1

print(result)

def reverseRucursive(s, start:int, end:int):
    if start > end:
        return
    s[start], s[end] = s[end], s[start]
    reverseRucursive(s, start +1 , end -1)

(reverseRucursive(input, 0, len(input)-1))
print(input)

mylist = ["e", "r", "e", "n"]
reverseRucursive(mylist, 0, len(mylist) -1)
print(mylist)

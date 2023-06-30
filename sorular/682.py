def calPoints(operations: list[str]) -> int:
    myStack = []
    for op in operations:
        if op == "C":
            myStack.pop()
        elif op == "D":
            myStack.append((myStack[-1])*2)
        elif op == "+":
            myStack.append((myStack[-1])+(myStack[-2]))
        else:
            myStack.append(int(op))
    return sum(myStack)

ops = ["5","2","C","D","+"]
print(calPoints(ops))
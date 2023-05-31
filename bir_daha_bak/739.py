def dailyTemperatures(temperatures: list[int]) -> list[int]:
    result = [0] * len(temperatures)
    myStack = []
    for i, t in enumerate(temperatures):
        while myStack and t > temperatures[myStack[-1]]:
            cur = myStack.pop()
            result[cur] = i - cur
        myStack.append(i)
    return result


# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
temp = [73,74,75,71,69,72,76,73]
print(dailyTemperatures(temp))


def dailyTemperatures2(temperatures: list[int]) -> list[int]:
    result = [0] * len(temperatures)
    myStack = []
    for i, t in enumerate(temperatures):
        while myStack and t > myStack[-1][0]:
            stackTemp, stackIndex = myStack.pop()
            result[stackIndex] = i - stackIndex
        myStack.append([t, i])
    return result

print(dailyTemperatures2(temp))

# class MyStack:

#     def __init__(self):
#         self.items = []

#     def push(self, x: int) -> None:
#         self.items.append(x)

#     def pop(self) -> int:
#         self.items.pop()

#     def top(self) -> int:
#         return self.items[-1]

#     def empty(self) -> bool:
#         self.items == []

from collections import deque


class MyStack:

    def __init__(self):
        self.myQueue = deque()

    def push(self, x: int) -> None:
        self.myQueue.append(x)

    def pop(self) -> int:
        for i in range(len(self.myQueue)-1):
            self.push(self.myQueue.popleft())
        return self.myQueue.popleft()
    
    def top(self) -> int:
        return self.myQueue[-1]

    def empty(self) -> bool:
        return len(self.myQueue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
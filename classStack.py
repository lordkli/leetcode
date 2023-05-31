class Stack():
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def isEmpty(self):
        return self.items == []
    
    def showLast(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

myStack = Stack()
print(myStack.isEmpty())
myStack.push(10)
myStack.push(20)
myStack.push(40)

print(myStack.showLast())

myStack.push("a")
print(myStack.showLast())

print(myStack.size())
print(myStack.pop())
print(myStack.size())
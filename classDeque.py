'''
Deque()
addFront(item)
addRear(item)
removeFront()
removeRear()
isEmpty()
size()
'''

class Deque():
    def __init__(self):
        self.items = []
    
    def addFront(self, item):
        self.items.insert(0,item)
    
    def addRear(self, item):
        self.items.append(item)
    
    def removeFront(self):
        return self.items.pop(0)
    
    def removeRear(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)

myDeque = Deque()
print(myDeque.isEmpty())
myDeque.addRear(4)
myDeque.addRear('dog')
myDeque.addFront('cat')
myDeque.addFront(True)
print(myDeque.size())
print(myDeque.isEmpty())
myDeque.addRear(8.4)
# True cat 4 dog 8.4
print(myDeque.removeRear())
# True cat 4 dog
print(myDeque.removeFront())
# cat 4 dog
print(myDeque.items)


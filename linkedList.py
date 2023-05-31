# Node -> Linked List

# Singly Linked List

class Node:
    def __init__(self, value):
        self.value = value
        self.nextNode = None

firstNode = Node(10)
secondNode = Node(20)
thirdNode = Node(30)
firstNode.nextNode = secondNode
secondNode.nextNode = thirdNode
print(firstNode.nextNode.nextNode.value)

# Doubly Linked List

class Node:
    def __init__(self, value):
        self.value = value
        self.nextNode = None
        self.previousNode = None

firstNode = Node(10)
secondNode = Node(20)
thirdNode = Node(30)
firstNode.nextNode = secondNode
secondNode.nextNode = thirdNode
secondNode.previousNode = firstNode
thirdNode.previousNode = secondNode
print(firstNode.nextNode.nextNode.previousNode.value)
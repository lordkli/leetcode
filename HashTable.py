# print(hash("apple"))
# print(hash("banana"))
# print(hash(12))
# print(hash(12.3))
# print(hash(True))
# print(hash(False))
# print(hash(None))
# print(hash("apple") % 8)
# print(hash("banana") % 8)
# print(hash(12) % 8)
# print(hash(12.3) % 8)
# print(hash(True) % 8)
# print(hash(False) % 8)
# print(hash(None) % 8)
# print(hash("apple") % 8)

def hash_function(key):
    return sum([ord(c) for c in key]) % 8

def hash_function2(key):
    return sum(index * ord(character) for index, character in enumerate(repr(key).lstrip("'"), 1))

class HashTable:
    
    def __init__(self, size = 13):
        self.dataMap = [None] * size
        
    def hashFunction(self,key):
        myHash = 0
        for letter in key:
            myHash = (myHash + ord(letter) * 19) % len(self.dataMap)
        return myHash
    
    def setItem(self, key, value):
        index = self.hashFunction(key)
        if self.dataMap[index] is None:
            self.dataMap[index] = []
        self.dataMap[index].append([key, value])
    
    def getItem(self, key):
        index = self.hashFunction(key)
        if self.dataMap[index] is not None:
            for i in range(len(self.dataMap[index])):
                if self.dataMap[index][i][0] == key:
                    return self.dataMap[index][i][1]
        return None
# [None, None, None, None, ["apple",200],["banana",400],["orange",600], None, None, None, None, None, None, None, None, None, None]

    def getKeys(self):
        keys = []
        for i in range(len(self.dataMap)):
            if self.dataMap[i] is not None:
                for j in range(len(self.dataMap[i])):
                    keys.append(self.dataMap[i][j][0])
        return keys

    def printTable(self):
        for index, value in enumerate(self.dataMap):
            print(index, "->", value)

myHashTable = HashTable()
myHashTable.setItem("apple", 200)
myHashTable.setItem("banana", 400)
myHashTable.setItem("orange", 600)
myHashTable.setItem("mango", 800)
myHashTable.setItem("grapes", 1000)
myHashTable.setItem("pineapple", 1200)
myHashTable.setItem("watermelon", 1400)
myHashTable.setItem("strawberry", 1600)

myHashTable.printTable()
# 0 -> None
# 1 -> [['banana', 400]]
# 2 -> [['pineapple', 1200]]
# 3 -> [['watermelon', 1400]]
# 4 -> [['grapes', 1000]]
# 5 -> None
# 6 -> None
# 7 -> [['orange', 600]]
# 8 -> [['apple', 200], ['mango', 800]]
# 9 -> None
# 10 -> None
# 11 -> [['strawberry', 1600]]
# 12 -> None

print(myHashTable.getKeys())
# ['banana', 'pineapple', 'watermelon', 'grapes', 'orange', 'apple', 'mango', 'strawberry']
print(myHashTable.getItem("apple")) # 200
print(myHashTable.getItem("mango")) # 800
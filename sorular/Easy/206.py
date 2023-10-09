# 206. Reverse Linked List

# Given the head of a singly linked list, reverse the list, and return the reversed list.

# 1-> 2-> 3
# 1<- 2<- 3



    # Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def createLinkedList(nodes):
    if not nodes:
        return None
    head = ListNode(nodes[0])
    current = head
    for value in nodes[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def printLinkedList(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

# Verilen liste
nodes = [1, 2, 3, 4, 5]

# Singly linked list oluştur
head = createLinkedList(nodes)

# Oluşturulan linked list'i yazdır
print("Original Linked List:")
printLinkedList(head)

# Linked list'i tersine çevir
new_head = reverseList(head)

# Tersine çevrilen linked list'i yazdır
print("Reversed Linked List:")
printLinkedList(new_head)


head = [1, 2, 3, 4, 5]
print(reverseList(head))

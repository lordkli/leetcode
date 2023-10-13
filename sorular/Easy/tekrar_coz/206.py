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

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    
head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

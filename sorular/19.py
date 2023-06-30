# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


def removeNthFromEnd(head: Optional[list], n: int) -> Optional[list]:
    leftPointer = head
    rightPointer = head
    
    while n > 0 and rightPointer:
        rightPointer = rightPointer.next
        n -= 1
        
    while rightPointer and rightPointer.next:
        leftPointer = leftPointer.next
        rightPointer = rightPointer.next
    
    if leftPointer == head and rightPointer == None:
        return head.next
    
    leftPointer.next = leftPointer.next.next
    
    return head
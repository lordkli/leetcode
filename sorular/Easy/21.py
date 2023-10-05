# 21. Merge Two Sorted Lists

# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]


def mergeTwoLists(list1, list2):
    i1, i2 = 0, 0
    len1, len2 = len(list1), len(list2)
    resultList = []

    while i1 < len1 or i2 < len2:
        if i1 < len1 and list1[i1] <= list2[i2]:
            resultList.append(list1[i1])
            i1 += 1
        else:
            resultList.append(list2[i2])
            i2 += 1
    return resultList


list1 = [1, 2, 4]
list2 = [1, 3, 4]
print(mergeTwoLists(list1, list2))


def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy = ListNode()
        # tail = dummy

        # while list1 and list2:
        #     if list1.val < list2.val:
        #         tail.next = list1
        #         list1 = list1.next
        #     else:
        #         tail.next = list2
        #         list2 = list2.next
        #     tail = tail.next
        # if list1:
        #     tail.next = list1
        # elif list2:
        #     tail.next = list2
        
        # return dummy.next

        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        while list1:
                tail.next = list1
                list1 = list1.next
                tail = tail.next
        
        while list2:
            tail.next = list2
            list2 = list2.next
            tail = tail.next
        return dummy.next
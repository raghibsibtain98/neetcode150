# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        prev = None
        while temp:
            current = temp
            nex = current.next
            current.next = prev
            prev = current
            temp = nex
    
        return prev


# 0-> 1-> 2-> 3
         



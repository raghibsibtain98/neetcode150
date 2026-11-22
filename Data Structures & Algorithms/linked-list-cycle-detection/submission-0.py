# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        exists = []

        temp = head
        while temp:
            if temp in exists:
                return True
            exists.append(temp)
            temp = temp.next
        
        return False


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        forward,backward = head,dummy


        while n>0:
            forward = forward.next
            n-=1

        while forward:
            backward, forward = backward.next, forward.next
        
        backward.next = backward.next.next

        return dummy.next

        

        
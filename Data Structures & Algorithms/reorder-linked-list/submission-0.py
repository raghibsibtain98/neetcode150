# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1,2,3,4,5
# s,s,s
# f, ,f, ,f
#
# 1,2,3,4,5
# f,
#  , , ,s
# 1,5,2,


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        first_part,second_part = head,slow.next

        prev = slow.next = None

        while second_part:
            tmp = second_part.next
            second_part.next = prev
            prev = second_part
            second_part = tmp
        
        second_part = prev

        while second_part :
            tmp1, tmp2 = first_part.next, second_part.next
            first_part.next = second_part
            second_part.next = tmp1
            second_part = tmp2
            first_part = tmp1









# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = l1,l2
        newHead = ListNode(0)
        pointer = newHead

        carryForward = 0
        while curr1 and curr2:
            val1,val2 = curr1.val,curr2.val
            digitSum = (val1+val2+carryForward) % 10
            carryForward = (val1+val2+carryForward) // 10

            pointer.next = ListNode(digitSum)
            pointer = pointer.next
            curr1,curr2 = curr1.next, curr2.next
        
        while curr1:
            val1 = curr1.val
            digitSum = (val1+carryForward) % 10
            carryForward = (val1+carryForward) // 10

            pointer.next = ListNode(digitSum)
            pointer = pointer.next
            curr1 = curr1.next

        while curr2:
            val2 = curr2.val
            digitSum = (val2+carryForward) % 10
            carryForward = (val2+carryForward) // 10

            pointer.next = ListNode(digitSum)
            pointer = pointer.next
            curr2 = curr2.next

        if carryForward>0:
            pointer.next = ListNode(carryForward)
        
        return newHead.next
        




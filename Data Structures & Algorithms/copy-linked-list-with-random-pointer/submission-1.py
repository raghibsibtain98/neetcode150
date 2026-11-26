"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        nodeMap = {}
        tmp = head
        while tmp:
            newNode = Node(tmp.val)
            nodeMap[tmp] = newNode
            tmp = tmp.next
        
        curr = head
        newHead = nodeMap[head] if head else None
        newCurr = newHead

        while curr:
            newCurr.next = nodeMap[curr.next] if curr.next else None
            newCurr.random = nodeMap[curr.random] if curr.random else None
            newCurr,curr = newCurr.next,curr.next
        
        return newHead

        
        
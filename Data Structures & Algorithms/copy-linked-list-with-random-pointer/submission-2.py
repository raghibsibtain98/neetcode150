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
        if not head :
            return None

        nodeMap = {}
        tmp = head
        while tmp:
            newNode = Node(tmp.val)
            nodeMap[tmp] = newNode
            tmp = tmp.next
        
        curr = head
        newHead = nodeMap[head]
        newCurr = newHead

        while curr:
            newCurr.next = nodeMap.get(curr.next)
            newCurr.random = nodeMap.get(curr.random)
            newCurr,curr = newCurr.next,curr.next
        
        return newHead

        
        
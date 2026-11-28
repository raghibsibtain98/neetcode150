class Node:
    def __init__(self,key,val):
        self.key,self.val = key,val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.leastRecent = Node(-1,-1) 
        self.mostRecent = Node(-1,-1)
        self.leastRecent.next , self.mostRecent.prev = self.mostRecent , self.leastRecent
        self.cache = {}


    def remove(self, node: Node):
        prevNode, nextNode = node.prev, node.next
        prevNode.next, nextNode.prev = nextNode, prevNode
        node.prev = node.next = None

    def add(self, node: Node):
        prevNode = self.mostRecent.prev
        node.next, node.prev = self.mostRecent,prevNode
        self.mostRecent.prev = prevNode.next = node 


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        newNode = Node(key,value)

        self.cache[key] = newNode
        self.add(newNode)

        if len(self.cache) > self.capacity:
            toRemove = self.leastRecent.next
            self.cache.pop(toRemove.key)
            self.remove(toRemove)


        

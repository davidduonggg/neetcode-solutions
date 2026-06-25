class Node:
    def __init__(self, key, val, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    # if the capacity causes the cache to exceed its capacity, remove the least recently used key
    # i feel like a really good thing for this is a deque()?
    # we definitely use a hashmap for avg O(1) lookup
    # removal and update is also O(1)
    # the tricky part is, how do we manage the lifecycle of the keys
    # the brute force method is that we maintain some sort of deque
    # and then we scan the stack for the value that we used and we put it at the back of the queue
    # that would be O(n) because we have to look for the value to put it in the back of the queue
    # can we have like a map that maps the value to the node?
    # that way, we can just check to see if we already have it? if we don't then move it to the front of the queue
    # i think this is the right approach
    # any restraints? capacity > 0, key and val dont really matter

    def __init__(self, capacity: int):
        self.cap = capacity
        self.front = Node(-1, -1)
        self.rear = Node(-1, -1)
        
        self.front.next, self.rear.prev = self.rear, self.front
        self.nodes = {} # key : node

    def splice(self, n: Node):
        n.prev.next, n.next.prev = n.next, n.prev # splice out of list

    def refresh(self, n: Node) -> None:
        # wire new
        n.prev, n.next = self.rear.prev, self.rear
        self.rear.prev.next, self.rear.prev = n, n


    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
                
        # do the refresh method
        self.splice(self.nodes[key])
        self.refresh(self.nodes[key])
        return self.nodes[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            self.nodes[key].val = value
            self.splice(self.nodes[key])
            self.refresh(self.nodes[key])
            return

        # key not in nodes, create a new one
        # this is where we may have to delete
        self.nodes[key] = Node(key, value)
        self.refresh(self.nodes[key])

        self.cap -= 1
        if self.cap < 0:
            # delete node
            # the least used will be next to front
            least = self.front.next
            self.splice(least)
            self.cap += 1
            self.nodes.pop(least.key, least)
            


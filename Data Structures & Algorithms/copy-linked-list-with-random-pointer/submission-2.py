"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # given the head of ll len n
        # each node contains an additional pointer random
        # create a deep copy of the list

        # n < 100
        # node values are not guaranteed to be unique
        
        # the only identifying thing is the memory location itself
        # because values are not unique

        # we can create a mapping consisting of 
        # old nodes : new nodes
        # and then we can loop through the LL again and change all of the wiring
        # notes: n can be zero
        
        # lets think about doing the copying first
        hashmap = {}

        prev = dummy = Node(0)
        curr = head    
        while curr:
            n = Node(curr.val, None, curr.random)
            prev.next = n

            hashmap[curr] = n

            prev, curr = prev.next, curr.next

        curr = dummy.next
        while curr:
            if curr.random:
                curr.random = hashmap[curr.random]
            curr = curr.next

        return dummy.next

        
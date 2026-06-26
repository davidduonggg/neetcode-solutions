# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getKth(self, curr, n):
        while curr and n > 0:
            curr = curr.next
            n -= 1

        return curr

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # given the head of a SLL
        # reverse every k nodes
        # if there are fewer than k nodes left, leave the nodes

        # this looks pretty simple
        
        # the constraints don't seem interesting, k is guaranteed to be less than n (obv)

        # slow on first node, fast traverse n nodes nodes
        # when slow == head break, then begin

        # okay, so the algo is:
        # start at node prev, then traverse k times
        # the k-th node is the new head, reverse k - 1 times
        

        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth: break

            groupNext = kth.next
            prev, curr = groupNext, groupPrev.next
            while curr != groupNext:
                t = curr.next
                curr.next = prev
                prev, curr = curr, t

            t = groupPrev.next
            groupPrev.next = kth
            groupPrev = t

            
        return dummy.next

            

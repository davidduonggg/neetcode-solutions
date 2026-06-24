# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # given the head of a linkedlist, remove the nth node from the end of the list
        
        # can we use a slow pointer, and a fast pointer?

        # n <= sz

        fast = slow = head
        prev = None

        for _ in range(n):
            fast = fast.next

        while fast:
            fast = fast.next
            prev = slow
            slow = slow.next

        # slow is now at the nth node
        if prev:
            prev.next = slow.next
        else: # its the head
            head = head.next
            
        del slow

            

        return head
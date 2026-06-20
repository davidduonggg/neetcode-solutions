# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # given the head of a SLL
        
        # 0, n-1, 1, n-2, 2, n-3, ..
        # cannot reorder the nodes themselves
        
        # len(head) > 0
        # head may be null

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev, second = None, slow.next
        slow.next = None
        while second:
            t = second.next
            second.next = prev
            prev, second = second, t

        l1, l2 = head, prev
        while l2:
            t1, t2 = l1.next, l2.next
            l1.next = l2
            l2.next = t1
            l1 = t1
            l2 = t2
            
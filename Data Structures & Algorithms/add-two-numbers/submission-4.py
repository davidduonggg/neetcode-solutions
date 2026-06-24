# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # two non-empty LL
        # l1, l2, each represent a non-negative int
        # return the sum of the two numbers as a linked list
        
        # the hard part is carrying over in reverse

        # the brute force is just reversing both lists 
        # and then actually doing the addition

        # O(n + m) O() auxillary space
        # O(n + m), O(n + m) space


        num1 = ""
        while l1:
            num1 += str(l1.val)
            l1 = l1.next

        num2 = ""
        while l2:
            num2 += str(l2.val)
            l2 = l2.next

        total = int(num1[::-1]) + int(num2[::-1])
        
        dummy = ListNode()
        prev = dummy
        for c in str(total)[::-1]:
            n = ListNode(int(c), None)
            prev.next = n
            prev = prev.next

        return dummy.next
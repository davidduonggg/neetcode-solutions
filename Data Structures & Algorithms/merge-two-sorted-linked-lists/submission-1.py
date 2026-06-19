# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # merge two sorted linked lists

        # merge the two lists into one sorted linked list
        # new list should be made up of nodes from l1 and l2

        # an easy way to generalize edge cases is to have a dummy node
        
        # the general algorithm is, at every node, connect the next node to the one thats smaller
        # we can say like while l1 and l2
        # and then we can attach the rest of the list to the remaining node

        dummy = ListNode()
        curr = dummy
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                curr = list1
                list1 = list1.next
            else:
                curr.next = list2
                curr = list2
                list2 = list2.next

        if list1: curr.next = list1
        else: curr.next = list2


        return dummy.next

        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # given an array of k linked lists, where each list is sorted in ascending order
        # return the sorted linked list that is the result of merging all of the individual linked lists
        
        # for every ll, merge them together
        # O(N^2) worst case, we can optimize it by doing it somewhat like a merge sort
        
        def mergeLists(l1, l2):
            dummy = ListNode()
            curr = dummy

            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next

                curr = curr.next

            if l1: curr.next = l1
            else: curr.next = l2

            return dummy.next

        q = deque(lists)
        while len(q) > 1:
            for i in range(1, len(q), 2):
                l1, l2 = q.popleft(), q.popleft()
                q.append(mergeLists(l1, l2))

        return q[0] if q else None

            

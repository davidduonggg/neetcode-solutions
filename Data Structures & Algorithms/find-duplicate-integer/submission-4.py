class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # given an array of integers
        # exactly one repeated integer, every other integers
        
        # tortiose and hare?
        # the obvious brute force is to just use a hashset
        
        # an O(nlogn) solution would be just to sort it 
        # [1, n] each num is in this range
        # nums has n + 1 integers
        # we can map numbers to indices?
        
        # just treat every number as a pointer to something in the list
        
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: break

        begin = 0
        while begin != slow:
            begin = nums[begin]
            slow = nums[slow]

        return begin
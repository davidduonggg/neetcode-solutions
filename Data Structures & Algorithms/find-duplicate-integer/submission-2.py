class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # given an array of integers
        # exactly one repeated integer, every other integers
        
        # tortiose and hare?
        # the obvious brute force 
        seen = set()
        for num in nums:
            if num in seen:
                return num

            seen.add(num)

        return -1
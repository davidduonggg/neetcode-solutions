class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # given an integer array nums
        # return true if we can reach the last index starting from 0

        # we can easily do this with dp, and it would be O(n) time and
        # O(n) space

        # is there any way we can do this in constant memory

        # 1. take the largest jump possible?
        # [3, 5, 2, 5, 2, 0, 0, 1]
        if len(nums) == 1: return True
        i = 0
        maxReach = 0
        while i < len(nums):
            if i > maxReach: return False

            for j in range(i, i + nums[i] + 1):
                if j >= len(nums) - 1: return True
                
                maxReach = max(maxReach, j + nums[j])
                
            i += 1

        return maxReach >= len(nums) - 1

            
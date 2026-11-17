class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # given an integer array nums
        # return true if we can reach the last index starting from 0

        # we can easily do this with dp, and it would be O(n) time and
        # O(n) space

        # is there any way we can do this in constant memory

        # 1. take the largest jump possible?
        # [3, 5, 2, 5, 2, 0, 0, 1]

        canJump = 0

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= canJump:
                canJump = i

        return canJump == 0

            
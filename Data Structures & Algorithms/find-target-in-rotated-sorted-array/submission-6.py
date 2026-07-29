class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1

        while L <= R:
            M = (L + R) // 2

            if nums[M] == target:
                return M

            if nums[L] <= nums[M]:
                # this is the sorted half
                if target > nums[M] or target < nums[L]:
                    L = M + 1
                else:
                    R = M - 1
            else:
                # this is the sorted half 
                if target < nums[M] or target > nums[R]:
                    R = M - 1
                else:
                    L = M + 1

        return -1

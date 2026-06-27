class Solution:
    def findMin(self, nums: List[int]) -> int:
        # return the minimum element of this array

        L, R = 0, len(nums) - 1
        while L <= R:
            mid = (L + R) // 2
            if nums[mid] < nums[R]:
                R = mid
            else:
                L = mid + 1
        
        return nums[R]

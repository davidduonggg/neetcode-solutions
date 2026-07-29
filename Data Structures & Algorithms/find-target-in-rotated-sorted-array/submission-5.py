class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # given an array of length n
        # originally sorted in ascending order
        # the rotation is taking the first element and appending it to the back

        # given an integer target, return the index of target, else -1

        # all the elements in nums are unique
        # O(log n) == binary search

        L, R = 0, len(nums) - 1
        
        while L < R:
            mid = (L + R) // 2
            if nums[mid] > nums[R]:
                L = mid + 1
            else:
                R = mid

        bp = R
        if target < nums[0]:
            L, R = bp, len(nums) - 1
        else:
            L, R = 0, bp

        if bp <= 0:
            L, R = 0, len(nums) - 1

        while L <= R:
            mid = (L + R) // 2
            if nums[mid] < target:
                L = mid + 1
            elif nums[mid] > target:
                R = mid - 1
            else:
                return mid

        return -1


        
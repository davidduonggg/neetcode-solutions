class Solution:
    def findMin(self, nums: List[int]) -> int:
        # given an array of length n
        # originally sorted in ascending order
        # it has now been rotated between 1 and n times
        
        # all elements in the rotated sorted array are unique
        
        L, R = 0, len(nums) - 1
        minN = 0

        while L < R:
            # return the minimum element
            mid = (L + R) // 2
            print(mid)

            if nums[mid] > nums[R]: # this is the unsorted half
                L = mid + 1
            else:
                R = mid

        return nums[R]
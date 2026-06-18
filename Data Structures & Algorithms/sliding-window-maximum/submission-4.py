class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # sliding window of size k that starts at the left edge of the array
        # slides until it reaches the right edge of the array
        # return a list that contains the maximum element in the window at each step
        
        if len(nums) == 1: return nums


        # brute force:
        # at every possible window, recompute the maximum at that window
        # k * (n - k)
        # can we get an O(n) solution?
        res = []
        L = 0
        for R in range(k-1, len(nums)):
            res.append(max(nums[L: R + 1]))
            L += 1

        return res

            

            
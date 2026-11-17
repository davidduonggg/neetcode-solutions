class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # given an array of integers nums
        # find the subarray with the largest sum

        # nums[i] can be negative
        # the brute force is, for every idx i, we calculate the
        # subarray that begins at that index. 
        # O(n^2) time
        
        # is there a way we can do this in O(n) time?
        # we can think about it like this:
        # at the ith index, what is the best subarray ending at this time
        # at a given index i, what is the largest sum seen
        self.maxSum = float("-inf")
        def dfs(i):
            if i < 0: return 0

            begin = nums[i]
            cont = nums[i] + dfs(i - 1)

            self.maxSum = max(self.maxSum, begin, cont)
            return max(begin, cont)
            
        dfs(len(nums) - 1)
        return self.maxSum
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
        dp = [0] * (len(nums) + 1)
        dp[len(nums)] = float("-inf")

        maxSum = float("-inf")
        for i in range(len(nums) - 1, -1, -1):
            dp[i] = max(
                nums[i],
                nums[i] + dp[i + 1]
            )

            maxSum = max(maxSum, dp[i])

        return maxSum

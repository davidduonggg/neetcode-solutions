class Solution:
    def jump(self, nums: List[int]) -> int:
        # given an array of integers nums
        # return the minimum number of jumps to reach the last position
        # in the array
        # i would do this with dp, but im not sure how greedy would work

        # one approach i would have is to just brute force the entire problem
        # with recursion, we could just explore all possible routes
        # 2^n time, n space (call stack)

        # we can also probably do this with dynamic programming
        # at a given index i, what's the minimum number of jumps to get there
        # n time, n space

        # we could think of the problem in terms of ranges
        # at the first step, what's the range of steps etc
        # similar to a sliding window problem
        # there is always a valid answer

        # [2, 4, 1, 1, 1]

        L, R = 0, 0
        steps = 0
        while R < len(nums) - 1:
            steps += 1
            newL, newR = R + 1, 0

            for i in range(L, R + 1):
                newR = max(newR, i + nums[i])

            L, R = newL, newR

        return steps

class Solution:
    def climbStairs(self, n: int) -> int:
        # we can climb with either 1 or two steps
        # return the number of distinct ways to climb to the top of the staircase

        # the brute force would be to solve this through recursion
        # we start at n, and we either move back 1 or two steps
        # but we would recompute work: the distinct ways to climb at n steps would always be the same
        # so, we use dp to solve this problem
        if n == 1:
            return 1
        first = 1
        second = 2

        for i in range(2, n):
            nextStep = first + second
            first = second
            second = nextStep

        return second
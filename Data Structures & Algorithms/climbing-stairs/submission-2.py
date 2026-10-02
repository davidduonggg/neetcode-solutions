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
            
        arr = [0] * n
        arr[0] = 1
        arr[1] = 2

        for i in range(2, n):
            arr[i] = arr[i-1] + arr[i-2]

        return arr[n-1]
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # array of distinct integers
        # target integer
        # return a list of all unique combinations of nums
        # where the chosen numbers sum to target

        # the same number can be chosen an unlimited number of times
        # return combinations in any order, order of numbers in any order

        # all elements of nums are distinct

        # return an empty list if it can't be summed up

        res = []

        def dfs(i, target, arr):
            if i >= len(nums) or target < 0: return

            if target == 0: 
                res.append(arr[:])
                return 

            # choose number again
            arr.append(nums[i])
            dfs(i, target - nums[i], arr)
            arr.pop()

            dfs(i + 1, target, arr)

        dfs(0, target, [])

        return res

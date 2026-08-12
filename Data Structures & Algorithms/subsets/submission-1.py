class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # given an array nums of unique integers
        # return all possible subsets of nums
        # the solution must not contain duplicate subsets

        # uniqueness of integers 
        
        res = []

        def dfs(i, arr):
            if i >= len(nums): 
                res.append(arr[:])
                return

            # skip
            dfs(i + 1, arr)

            arr.append(nums[i])
            dfs(i + 1, arr)
            arr.pop()

        dfs(0, [])
        return res
                

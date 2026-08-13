class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # integer array, may contain duplicates
        # return all unique subsets
        # we can return in any order

        # first, let's read through the test cases to understand
        # if there are duplicate elements, we can still have two of them
        # but we can't have [7], [7] for example
        
        # the main problem here is, how do we account for or how do we exclude those cases where a duplicate subset might be generated?
        # we can do it by just sorting the input array, and if we choose to exclude, then we exclude the rest of the numbers
        # 7, 7, 7
        # [], [7], [7, 7], [7, 7, 7]

        nums.sort()
        res = []

        def dfs(i, path):
            if i >= len(nums):
                res.append(path[:])
                return

            # skip or add
            path.append(nums[i])
            dfs(i + 1, path)
            path.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            dfs(i + 1, path)

        dfs(0, [])
        return res
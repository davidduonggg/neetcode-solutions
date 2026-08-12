class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # candidates, which may contain duplicates
        # target integer 

        # reutrn all unique combinations of candidates that sum to target
        # return in any order combination in any order

        # element chosen at MOST ONCE
        res = []

        candidates.sort()

        def dfs(i, num, arr):
            if num == 0: 
                res.append(arr[:])
                return

            if i >= len(candidates) or num < 0: 
                return

            arr.append(candidates[i])
            dfs(i + 1, num - candidates[i], arr)
            arr.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, num, arr)



        dfs(0, target, [])

        return res




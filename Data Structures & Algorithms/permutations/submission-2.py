class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # unique integers
        # return all possible permutations, 
        # return in any order

        # nums >= 1, <= 6

        # shuffling all numbers around
        
        # O(n ^ 2), O(n) for the path, O(n) function call stack

        seen = set()
        res = []

        def dfs(path):
            if len(path) == len(nums): 
                res.append(path[:])
                return

            for num in nums:
                if num in seen: continue

                path.append(num)
                seen.add(num)
                dfs(path)
                path.pop()
                seen.remove(num)


        dfs([])

        return res
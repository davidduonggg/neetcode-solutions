class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # given a string digits made up of digits from 2 to 9 inclusive

        # each digit is mapped to a set of characterrs
        # return all possible letter combinations that digits could represent

        # reutrn answer in any order

        # from reading the problem, it seems like we just need to return every combination
        # we can do that easily with a recursive problem

        mapping = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        res = []

        if not digits: return []

        def dfs(i, comb):
            if i >= len(digits): # we have a combination
                res.append(comb)
                return

            for ch in mapping[digits[i]]:
                dfs(i + 1, comb + ch)

        dfs(0, "")
        return res
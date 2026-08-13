class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # return all well formed parenthesis strings that we can generate
        # with n pairs of parentheses

        # how do we generate a valid parentheses string
        # try every single possible combination of parentheses, and then use a function to verify whether or not its valid
        res = []

        def dfs(l, r, s):
            if len(s) >= (2*n):
                if l == r and r == 0: res.append(s)
                return 

            # how do we know if a string is valid or not
            # let's think about what makes a parenthesis valid
            # when we're building it, if there are more right than left it is impossible
            # for it to be a valid parenthesis
            # however, if there are left parenthesis, we can always add more right

            if r > l: dfs(l, r - 1, s + ")")
            if l > 0: dfs(l - 1, r, s + "(")


        dfs(n, n, "")

        return res
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # return all well formed parenthesis strings that we can generate
        # with n pairs of parentheses

        # how do we generate a valid parentheses string
        # try every single possible combination of parentheses, and then use a function to verify whether or not its valid
        res = []

        def isValid(s: str):
            stk = []

            for ch in s:
                if ch == '(':
                    stk.append(ch)
                else:
                    if not stk: return False
                    stk.pop()

            return stk == []

        def dfs(s):
            if len(s) >= (2*n):
                if isValid(s): res.append(s)
                return 

            dfs(s + "(")
            dfs(s + ")")


        dfs("")

        return res
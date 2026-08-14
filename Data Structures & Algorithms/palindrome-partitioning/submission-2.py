class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # given a string s
        # split s into substrings where every substring is a palindrome

        # a single letter is also a palindrome

        # checking if a string is a palindrome is trivial
        # the real problem is: how do we ensure that we try every
        # possible partition of the string, without duplicating work?

        # lets draw out the decision tree first

        # we can keep track of the indices, and if we alreadu visite dthe indices before
        # we can just return
        res = []

        def isPalin(L, R):
            while L < R:
                if s[L] != s[R]:
                    return False

                L += 1
                R -= 1

            return True

        def dfs(i, path):
            if i >= len(s): 
                res.append(path[:])
                return

            for j in range(i, len(s)):
                if isPalin(i, j):
                    path.append(s[i:j + 1])
                    dfs(j + 1, path)
                    path.pop()
            
        dfs(0, [])
        return res

            
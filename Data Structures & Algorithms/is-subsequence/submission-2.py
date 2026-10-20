class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # given two string s and t
        # recursive solution
        N, M = len(s), len(t)

        cache = {}

        def isSub(i, j):
            if i == N:
                return True

            if j == M:
                return False

            include = False
            if s[i] == t[j]:
                include = isSub(i + 1, j + 1)

            skip = isSub(i, j + 1)

            return include or skip

        return isSub(0, 0)
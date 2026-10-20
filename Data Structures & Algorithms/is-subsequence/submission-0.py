class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # given two string s and t
        # recursive solution
        N, M = len(s), len(t)

        def isSub(i, j):
            if i == N:
                return True

            if j == M:
                return False

            if s[i] == t[j]:
                return isSub(i + 1, j + 1)
            else:
                return isSub(i, j + 1)

        return isSub(0, 0)
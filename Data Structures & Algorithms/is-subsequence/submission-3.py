class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # given two string s and t
        # recursive solution
        N, M = len(s), len(t)

        cache = defaultdict(bool)

        def isSub(i, j):
            if i == N:
                cache[(i, j)] = True
                return True

            if j == M:
                cache[(i, j)] = False
                return False

            
            if s[i] == t[j]:
                cache[(i, j)] = isSub(i + 1, j + 1)

            cache[(i, j)] = cache[(i, j)] or isSub(i, j + 1)

            return cache[(i, j)]

        return isSub(0, 0)
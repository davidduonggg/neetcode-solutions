class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # given two string s and t
        # recursive solution
        N, M = len(s), len(t)
        dp = [[False] * len(t) for _ in range(len(s))]

        if not s and not t:
            return True
        elif not s:
            return True
        elif not t:
            return False

        for j in range(M):
            dp[N-1][j] = True

        for i in range(N - 2, -1, -1):
            for j in range(M - 2, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = dp[i][j + 1]


        return dp[0][0]

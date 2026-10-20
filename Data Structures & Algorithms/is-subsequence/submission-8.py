class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # given two string s and t
        # recursive solution
        N, M = len(s), len(t)
        dp = [[False] * (M + 1) for _ in range(N + 1)]

        for j in range(M + 1):
            dp[N][j] = True

        for i in range(N - 1, -1, -1):
            for j in range(M - 1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = dp[i][j + 1]


        return dp[0][0]

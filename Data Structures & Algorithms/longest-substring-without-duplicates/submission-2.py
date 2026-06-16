class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # given a string s, find the length of the longest substring
        # without dupliate characters

        # substring without duplicate characters
        # hashset, O(1) average lookup and deletion and add time

        # how do we find the longest substring?
        # grow the window while window is valid, without duplicate characters
        # if the window is invalid, then we shrink the window until its valid
        # that's how we progress through the problem

        seen = set()
        L = 0
        res = 0
        for R in range(len(s)):
            while s[R] in seen:
                seen.remove(s[L])
                L += 1

            res = max(res, R - L + 1)
            seen.add(s[R])

        return res
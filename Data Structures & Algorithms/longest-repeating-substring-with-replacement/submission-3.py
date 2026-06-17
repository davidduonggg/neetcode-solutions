class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # given a string s 
        # choose up to k characters of the string and replace them with any other character
        # after performing at most k replacements, return the length of the longest substring
        # which contains only one distinct character

        totalChars = 0
        chars = [0] * 26
        maxLen = 0

        # the question is, how do we keep track of the maximum from the hashmap
        L = 0
        for R in range(len(s)):
            chars[ord(s[R]) - ord('A')] += 1
            totalChars += 1
            if totalChars - max(chars) <= k:
                maxLen = max(maxLen, R - L + 1)
            else:
                while totalChars - max(chars) > k:
                    chars[ord(s[L]) - ord('A')] -= 1
                    totalChars -= 1
                    L += 1

        return maxLen
            




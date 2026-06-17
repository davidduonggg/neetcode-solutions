class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # given a string s 
        # choose up to k characters of the string and replace them with any other character
        # after performing at most k replacements, return the length of the longest substring
        # which contains only one distinct character

        chars = defaultdict(int)
        maxLen = 0
        maxChar = 0

        # the question is, how do we keep track of the maximum from the hashmap
        L = 0
        for R in range(len(s)):
            chars[s[R]] += 1
            maxChar = max(maxChar, chars[s[R]])
            
            if (R - L + 1) - maxChar <= k:
                maxLen = max(maxLen, R - L + 1)
            else:
                while (R - L + 1) - maxChar > k:
                    chars[s[L]] -= 1
                    L += 1

        return maxLen
            




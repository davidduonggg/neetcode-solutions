class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s2 contains a permutation of s1
        # if a permutaiton of s1 exists as a substring of s2, return true
        
        # for every index, expand to the right all the way and see if a subset exists
        # brute force
        # O(n^2) approach

        # < linear time?

        # traverse the string
        # if current char coun
        
        perm = [0] * 26
        for c in s1:
            perm[ord(c) - ord('a')] += 1

        chars = [0] * 26
        L = 0
        for R in range(len(s2)):
            chars[ord(s2[R]) - ord('a')] += 1

            while (R - L + 1) > len(s1):
                chars[ord(s2[L]) - ord('a')] -= 1
                L += 1

            print(chars, perm)
            if chars == perm: return True

        
        return False
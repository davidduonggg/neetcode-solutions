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
        
        perm = defaultdict(int)
        for c in s1:
            perm[c] += 1

        for L in range(len(s2)):
            chars = defaultdict(int)
            for R in range(L, len(s2)):
                chars[s2[R]] += 1
                if chars == perm: return True

        return False
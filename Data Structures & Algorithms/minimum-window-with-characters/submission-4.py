class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # substring of s, 
        # every character in t, including duplicates

        # variable sliding window
        # contiguous subset of s
        
        # how do we compare a substring to the actual string itself
        # hashmap, array store the characters

        # for every index i, travel to the end of the array
        # we check, is it valid? if its valid, stop and we try another index
        # track minLength

        # while window is not valid, grow window from R
        # while window is valid, shrink L until its not valid anymore
        
        # tricky part of this algorithm
        # given a substring, how can we compare it to another substring
        # s and t consist of uppercase and lowercase english letters
        # expansion on the previous problem. if its greater than s[t], then match = 0

        target = Counter(t)
        
        minLen = float("inf")
        res = ""
        chars = defaultdict(int)

        L, curr = 0, 0
        for R in range(len(s)):
            chars[s[R]] += 1
            if chars[s[R]] == target[s[R]]:
                curr += 1
            
            while curr >= len(target) and L <= R: # valid window
                if R - L + 1 < minLen: 
                    res = s[L:R+1] 
                    minLen = R - L + 1
                chars[s[L]] -= 1
                if s[L] in target and chars[s[L]] < target[s[L]]:
                    curr -= 1
                L += 1

        return res

            

            
                

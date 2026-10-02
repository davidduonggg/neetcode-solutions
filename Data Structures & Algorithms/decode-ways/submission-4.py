class Solution:
    def numDecodings(self, s: str) -> int:
        # to decode a message, digits must be grouped and then mapped
        # there may be multiple ways to decode a message
        # grouping 01 is invalid because it cannot be mapped into a letter
        # given a string s of digits, return the number of ways to decode it

        # decoding the string
        # every letter can be 1 or two characters wide
        # subproblem: trying every combination to see if its a valid decoding
        # at every index, we can choose either 1 or 2 digits to see if its a valid combination

        # recursion: at every step, we can either choose 1 or two digits and then 
        # recurse further until we reach the end of the string. if we reach the end of the string, 
        # its a valid decoding

        # we can check if a number is a valid letter in O(1) time with a hashmap
        decode = set()
        for i in range(1, 27):
            decode.add(str(i))

        cache = defaultdict(int)

        # there are overlapping subproblems
        # at every index i: there will always be the same
        # number of ways to reach it

        def dfs(i):
            if i in cache:  return cache[i]
            if i > len(s):  return 0
            if i == len(s): return 1

            if s[i] in decode:
                cache[i] += dfs(i + 1)
            if s[i:i+2] in decode:
                cache[i] += dfs(i + 2)

            return cache[i]

        dfs(0)
        print(cache)
        return cache[0]
            
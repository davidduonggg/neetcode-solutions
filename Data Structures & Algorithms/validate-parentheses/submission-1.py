class Solution:
    def isValid(self, s: str) -> bool:
        # given a string consisting of ( { [ ]})

        # every open bracket is closed by the same type of closed bracket
        # open brackets are closed
        
        chars = {
            '}': '{',
            ')': '(',
            ']':'['
        }

        stk = []

        for c in s:
            if c in chars:
                if not stk or stk[-1] != chars[c]:
                    return False
                stk.pop()
            else:
                stk.append(c)

        return len(stk) == 0

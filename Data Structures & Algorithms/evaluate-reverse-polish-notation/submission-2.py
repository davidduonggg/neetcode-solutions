class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # given an array of strings tokens
        # return the integer that represents the evaluation of the expression
        
        # we've done this in class before
        # maintain a stack of the operands, perform the operations
        # tokens is a valid expression
        
        # division between integers always truncates towards zero

        stk = []
        ops = {'+', '*', '/', '-'}
        for t in tokens:
            if t not in ops:
                stk.append(int(t))
                print(stk)
                continue

            b = stk.pop()
            a = stk.pop()
            if t == '+':
                stk.append(a + b)
            elif t == '*':
                stk.append(a * b)
            elif t == '-':
                stk.append(a - b)
            else:
                stk.append(int(a / b))
                
            print(stk)

        return stk[0]

class MinStack:
    # will always be called on non-empty stacks

    def __init__(self):
        self.stk = []
        self.minimum = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        
        if self.minimum: 
            minVal = min(val, self.minimum[-1])
        else:
            minVal = val

        self.minimum.append(minVal)


    def pop(self) -> None:
        self.stk.pop()
        self.minimum.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        # this should be O(1) time, constant
        # if you pop off, then it might be wrong
        return self.minimum[-1]

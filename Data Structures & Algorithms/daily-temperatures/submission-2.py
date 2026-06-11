class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # given an array of integers temperatures
        # result[i] is the number of days after the ith day before a warmer temperature 

        # for every temperature, we scan right until we find the next warmer day
        # O(n squared) time, O(1) space
        
        # warmer temperature
        # next thing thats bigger
        # order does matter for the input
        # we definitely can't sort, and we can't exploit the inputs structure
        # to use something like two pointers
        # not a queue either because we're not processing anything
        # its a monotonic stack, pretty straightforward
        # monotonically decreasing stack, if we find an element larger
        # we keep popping until the top of the stack is warmer

        res = [0] * len(temperatures)
        stk = [] # just store indexes

        # traverse through the array
        for i in range(len(temperatures)):
            # processing step
            while stk and temperatures[stk[-1]] < temperatures[i]:
                oldday = stk.pop()
                res[oldday] = i - oldday
            
            stk.append(i)

        for i in stk:
            res[i] = 0

        return res

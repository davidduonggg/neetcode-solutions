class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # given an integer array heights[i]
        # choose two bars, return the maximum amount

        # positions are important
        # no sorting
        
        # ith bar, best jth bar O(n^2) solution
        # stack? i think a monotonic stack is the right approach?
        # no, because the middle bars don't matter
        # and we can do it in O(1) space


        # start with a maximized length
        # slowly decrement and see which has the best height
        # we don't need to check for the bars behind the current pointers

        # input is never invalid, max height of 2
        # 0, 0, max area of 0
        L, R = 0, len(heights) - 1
        maxArea = 0

        while L < R:
            maxArea = max(maxArea, (R - L) * min(heights[L], heights[R]))
            
            # either decrement R or decrement L
            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1

        return maxArea
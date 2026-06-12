class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # given an array of integers heights, where heights[i] represents the height
        # return the area of the largest rectangle that can be formed


        # what is the intution
        # if we find a new height that's smaller than the height at the top of the stack
        # that's the biggest area we can calculate. anything else will just
        # be sliced

        # what if the input is like [2, 1, 2, 1]
        # we need to also store the new index
        # because for example, if we pop off 

        # monotonic increasing and the smaller heights index is updated 
        # to the previous heights index because its smaller so it fit in there
        # its like repushed back onto the stack?

        stk = [] # (height, index)
        maxArea = 0

        for i in range(len(heights)):
            new_idx = i
            while stk and heights[i] < stk[-1][0]:
                h, idx = stk.pop()
                new_idx = idx
                maxArea = max(maxArea, h * (i - idx))

            stk.append((heights[i], new_idx))


        for h, i in stk:
            maxArea = max(maxArea, h * (len(heights) - i))


        return maxArea
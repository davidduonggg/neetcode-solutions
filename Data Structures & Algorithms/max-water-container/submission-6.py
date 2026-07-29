class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # maximize the area
        
        L, R = 0, len(heights) - 1
        maxArea = 0

        while L < R:
            w = R - L
            h = min(heights[R], heights[L])
            maxArea = max(w * h, maxArea)

            if heights[R] <= heights[L]: R -= 1
            else: L += 1

        return maxArea
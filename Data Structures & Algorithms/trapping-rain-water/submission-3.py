class Solution:
    def trap(self, height: List[int]) -> int:
        # height[i] is non negative, less than 1000
        # length of height is >= 1, no null arrays

        # height[i] represents the height of a bar, width of 1
        
        # what would the brute force be?
        
        # every index i 
        # what is the highest height on the left
        # what is the highest height on the right
        # possible height of the water is the min(left height, right height)
        # subtracted by the height of the index itself
        
        # area[i] = min(max left height, max right height) - height[i]

        # brute force approach
        # for every index: find the max left height and the max right height
        
        # one possible approach we can do in O(n) time is to precompute 
        # the left and the right max heights in one pass for each index

        # and then we can just do one final pass through the array
        # time: 3n space: 2n 
        
        # we can try and optimize a better approach later

        left = []
        currMax = 0
        for i in range(len(height)):
            left.append(currMax)
            currMax = max(currMax, height[i])

        right = [0] * len(height)
        currMax = 0
        for i in range(len(height) - 1, -1, -1):
            right[i] = currMax
            currMax = max(currMax, height[i])

        res = 0
        for i in range(len(height)):
            water = min(left[i], right[i]) - height[i]
            if water > 0:
                res += water

        return res
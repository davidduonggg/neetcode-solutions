class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        stk = []

        for i in range(len(height)):
            while stk and height[stk[-1]] <= height[i]:
                h = stk.pop()
                if stk:
                    l = stk[-1]
                    area = (min(height[l], height[i]) - height[h]) * (i - l - 1)
                    res += area

            stk.append(i)

        return res 
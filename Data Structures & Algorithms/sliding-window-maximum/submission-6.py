class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # sliding window of size k that starts at the left edge of the array
        # slides until it reaches the right edge of the array
        # return a list that contains the maximum element in the window at each step
        
        if len(nums) == 1: return nums


        # brute force:
        # at every possible window, recompute the maximum at that window
        # k * (n - k)
        # can we get an O(n) solution?
        # we have to have some data structure that will let us get the maximum in constant time
        # and we need to keep it sorted
        # the only data structure i can think of is a monotonic stack
        # i think if the stk is empty then look for the maximum of the current window
        # else use a prior maximum?

        res = []
        q = deque()

        L = 0
        for R in range(k-1, len(nums)):
            while q and q[0] < L:
                q.popleft()
            if not q:
                maxNum = float("-inf")
                idx = -1
                for i in range(L, R + 1):
                    if nums[i] > maxNum:
                        maxNum = nums[i]
                        idx = i

                    q.append(idx)
            elif nums[R] > nums[q[-1]]:
                q.append(R)


            res.append(nums[q[-1]])
            L += 1

        return res

            

            
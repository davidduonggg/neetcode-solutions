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

        # monotonically decreasing queue
        # why does this work?
        # because every potential number can be a potential maximum
        # UNLESS a bigger one comes after. then every single number in the queue
        # will be obsolete because the new big number will always dominate the older numbers

        res = []
        q = deque()

        L = 0
        for R in range(len(nums)):
            while q and q[0] < L:
                q.popleft()

            while q and nums[R] > nums[q[-1]]:
                q.pop()

            
            q.append(R)

            if (R + 1) >= k: 
                res.append(nums[q[0]])
                L += 1

        return res

            

            
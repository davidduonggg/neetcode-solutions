class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # h, which represents the number of hours we have to eat all bananas
        # decide bananas eating rate of k
        # if pile has less than k bananas, we can eat the pile but we can't eat from another pile
        # return the minimum integer k such that we can eat all the bananas within h hours

        def helper(k): # basically we simulate the problem, O(n)
            hours = 0
            for pile in piles:
                h = math.ceil(pile / k)
                hours += h

            print("hours", hours)
            return hours
        
        # now we find the min k where we can eat bananas within h hours
        # we have to search through the solution space
        k = 0
        L, R = 1, max(piles)
        while L <= R:
            mid = (L + R) // 2
            print(mid)
            if helper(mid) <= h:
                k = mid
                R = mid - 1
            else:
                L = mid + 1

        return k
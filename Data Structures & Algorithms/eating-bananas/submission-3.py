class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # given an integer array piles, where piles[i] is the number of bananas in the ith pile
        # given an intger h, represents # hours to eat all bananas
        
        # decide k
        # each hour, you may choose a pile of bananas and eats k bananas

        def eat(k):
            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(pile / k)

            return True if totalTime <= h else False

        # now we do binary search on the solution space
        L, R = 1, max(piles)
        while L < R:
            mid = (L + R) // 2
            if eat(mid) == True:
                R = mid
            else:
                L = mid + 1

        return L
                
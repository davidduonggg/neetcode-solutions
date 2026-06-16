class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # given an integer array prices
        # prices[i] is the price of NeetCoin
        # choose a single day to buy one neetcoin and choose a different day in the future to sell it
        # return the maximum profit you can achieve
        
        # profit >= 0
        # constraints don't seem interesting

        # what would the brute force solution be?
        # we can only choose a single day to buy one neet coin
        #  for everyday, we can check the rest of the array for the best way to sell it
        # this is an O(n^2) approach

        # the best time to buy a stock is when it is cheapest
        # the best time to sell a stock is when it is most expensive
        low = prices[0]
        maxProfit = 0
        for i in range(len(prices)):
            low = min(low, prices[i])
            maxProfit = max(prices[i] - low, maxProfit)

        return maxProfit
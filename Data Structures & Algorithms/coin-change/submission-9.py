class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # recursive solution
        # the state is the amount of coins, and the target
        # base case, if the amount is greater, than return -1
        # if the target is 0, return the minimum
        numCoins = [float("inf")] * (amount + 1)
        numCoins[0] = 0



        for i in range(len(numCoins)):
            for coin in coins:
                if i - coin >= 0:
                    numCoins[i] = min(numCoins[i], numCoins[i - coin] + 1)

        return numCoins[amount] if numCoins[amount] != float("inf") else -1

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # given an integer array coins
        # return the number of distinct combinations that total up to amount

        # now we do dp
        # the only state here is how much we have
        combinations = [0] * (amount + 1)
        combinations[0] = 1
        for coin in coins:
            for i in range(amount + 1):
                if i - coin >= 0:
                    combinations[i] = combinations[i] + combinations[i - coin] 

        print(combinations)
        return combinations[amount]


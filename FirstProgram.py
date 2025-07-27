class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # dp[i] will store the minimum number of coins needed for amount i
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0 # 0 coins needed for amount 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1

# Test Cases
print(f"Coin Change for coins=[1,2,5], amount=11: {Solution().coinChange([1,2,5], 11)}") # Expected: 3
print(f"Coin Change for coins=[2], amount=3: {Solution().coinChange([2], 3)}") # Expected: -1
print(f"Coin Change for coins=[1], amount=0: {Solution().coinChange([1], 0)}") # Expected: 0
print(f"Coin Change for coins=[186,419,83,408], amount=6249: {Solution().coinChange([186,419,83,408], 6249)}") # Expected: 20
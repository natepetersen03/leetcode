'''
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
 

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104

If dealing with amounts of money/sums, dp[] should track total quantity
from 0, 1, 2, 3, ... rather than sum of first coin, second coin, ...
'''




class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0]
        for a in range(1, amount + 1):
            dp.append(-1)
            for b in range(len(coins)):
                if a - coins[b] >= 0:
                    if dp[a - coins[b]] != -1:
                        if dp[a] == -1:
                            dp[a] = 1 + dp[a - coins[b]]
                        else:
                            dp[a] = min(dp[a], 1 + dp[a - coins[b]])
        return dp[amount]          
            
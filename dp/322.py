# 2023年4月17日19:02:53-->2023年4月17日19:11:10
"""
给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。

计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。

你可以认为每种硬币的数量是无限的。

"""
import numpy as np


class Solution:
    def coinChange(self, coins: list[int], amount: int):
        # base case
        dp = [0] * (amount + 1)
        # transform : dp[i] = min{dp[i-coins]} +1
        for i in range(1, (amount + 1)):
            dp_i_min = np.inf
            for each in coins:
                if i - each < 0:
                    continue
                else:
                    dp_i_min = min(dp[i - each], dp_i_min)
            dp[i] = dp_i_min + 1
        return dp[amount] if dp[amount] != np.inf else -1

    def test(self, coins: list, amount: int, ans: int):
        x = self.coinChange(coins, amount)
        if x == ans:
            print('True')
        else:
            print('False')


if __name__ == '__main__':
    Solution().test([1, 2, 5], 11, 3)
    Solution().test([2], 3, -1)
    Solution().test([1], 0, 0)
    Solution().test([186, 419, 83, 408], 6249, 10)

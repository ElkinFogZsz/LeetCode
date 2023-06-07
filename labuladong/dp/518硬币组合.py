"""
给你一个整数数组 coins 表示不同面额的硬币，另给一个整数 amount 表示总金额。

请你计算并返回可以凑成总金额的硬币组合数。如果任何硬币组合都无法凑出总金额，返回 0 。

假设每一种面额的硬币有无限个。

题目数据保证结果符合 32 位带符号整数。

2023年4月18日15:31:06 -> 2023年4月18日15:42:26，确定现有方法不可行。
"""
import numpy as np


class Solution:
    def change(self, amount: int, coins: list[int]):
        dp = [[0 if j != 0 else 1 for j in range(amount + 1)] for i in range(len(coins) + 1)]
        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):
                if j - coins[i - 1] < 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]
        return dp[len(coins)][amount]

    def test(self, amout, coins: list[int], ans):
        if self.change(amout, coins) == ans:
            print('√')
        else:
            print('×')


class Solution2(object):
    def change(self, amount: int, coins: list[int]) -> int:
        n = len(coins)
        if amount == 0 or n == 0:
            return 1
        dp = [[0 for j in range(amount)] for i in range(n)]
        for j in range(amount):
            dp[0][j] = 1 if (j+1) % coins[0] ==0 else 0
        for i in range(1, n):
            for j in range(amount):
                max_coins_nums = int((j + 1) / coins[i])
                sum_res = 0
                for k in range(max_coins_nums + 1):
                    if j + 1 - k * coins[i] == 0:
                        sum_res += 1
                    else:
                        if dp[i - 1][j - k * coins[i]] > 0:
                            sum_res += dp[i - 1][j - k * coins[i]]
                        else:
                            sum_res += 0
                dp[i][j] = sum_res
        return dp[n - 1][amount - 1]

    def test(self, amout, coins: list[int], ans):
        if self.change(amout, coins) == ans:
            print('√')
        else:
            print('×')


if __name__ == '__main__':
    s = Solution2()
    s.test(5, [1, 2, 5], 4)
    s.test(3, [2], 0)
    s.test(10, [10], 1)

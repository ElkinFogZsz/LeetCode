"""
2023年4月17日19:19:19
给你一个整数数组 coins 表示不同面额的硬币，另给一个整数 amount 表示总金额。

请你计算并返回可以凑成总金额的硬币组合数。如果任何硬币组合都无法凑出总金额，返回 0 。

假设每一种面额的硬币有无限个。

题目数据保证结果符合 32 位带符号整数。
"""

import numpy as np


class Solution:
    count = 0

    def coinChange(self, coins: list[int], amount: int):
        Solution.count = 0
        coins = np.sort(coins)[::-1]
        self.travel(coins, amount)
        return Solution.count

    def travel(self, coins: list[int], amount: int):
        if amount < min(coins):
            # 已经凑不齐了
            return False
        else:
            for each in coins:
                if amount - each == 0:
                    Solution.count += 1
                elif amount - each < 0:
                    continue
                else:
                    self.travel(coins, amount - each)

    def test(self, coins: list, amount: int, ans: int):
        x = self.coinChange(coins, amount)
        if x == ans:
            print('True')
        else:
            print('False')


if __name__ == '__main__':
    Solution().test([1, 2, 5], 5, 4)
    Solution().test([2], 3, 0)
    Solution().test([10], 10, 1)

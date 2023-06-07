# 零钱兑换问题、递归版本，LEETCODE时间不通过
"""
给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。

计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。

你可以认为每种硬币的数量是无限的。

"""

import numpy as np


class Solution:
    min_coins_number = np.inf

    def coinChange(self, coins: list[int], amount: int):
        Solution.min_coins_number = np.inf
        coins = np.sort(coins)[::-1]
        if self.travel(coins, amount, 0):
            return Solution.min_coins_number
        elif amount == 0:
            return 0
        else:
            return -1

    def travel(self, coins: list[int], amount: int, count: int):
        if amount < min(coins):
            # 已经凑不齐了
            return False
        else:
            for each in coins:
                if amount - each == 0:
                    Solution.min_coins_number = min(Solution.min_coins_number, count + 1)
                    return True
                else:
                    if self.travel(coins, amount - each, count + 1):
                        return True

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

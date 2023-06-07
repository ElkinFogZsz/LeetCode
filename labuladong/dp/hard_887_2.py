"""
给你 k 枚相同的鸡蛋，并可以使用一栋从第 1 层到第 n 层共有 n 层楼的建筑。

已知存在楼层 f ，满足 0 <= f <= n ，任何从 高于 f 的楼层落下的鸡蛋都会碎，从 f 楼层或比它低的楼层落下的鸡蛋都不会破。

每次操作，你可以取一枚没有碎的鸡蛋并把它从任一楼层 x 扔下（满足 1 <= x <= n）。如果鸡蛋碎了，你就不能再次使用它。如果某枚鸡蛋扔下后没有摔碎，则可以在之后的操作中 重复使用 这枚鸡蛋。

请你计算并返回要确定 f 确切的值 的 最小操作次数 是多少？
2023年4月19日11:41:39 2023年4月19日12:25:15 Failure，我不想使用dp，我认为一个二分就可以了。

100层楼，2个鸡蛋，二分，最差是51次，实际上若第一个鸡蛋十分，则不超过20次就可以确定。这是一个很难的思路问题。我的状态转移方程没有写对。
"""
import numpy as np


class Solution:
    def superEggDrop(self, k: int, n: int):
        dp = [[i if j == 0 else 0 for j in range(k)] for i in range(n + 1)]
        for j in range(1, k):
            for i in range(1, n + 1):
                mid = (1+i) // 2
                # 先投一次
                dp[i][j] += 1
                # 如果碎了，向下投，如果无法下投，则找到了
                broken = dp[mid-1][j - 1]
                # 如果没碎，向上投，如果无法上投，则找到了
                not_broken = dp[i-mid][j]
                dp[i][j] += max(broken, not_broken)
        return dp[n][k - 1]

    def test(self, k: int, n: int, ans: int):
        if self.superEggDrop(k, n) == ans:
            print('√')
        else:
            print('×')


if __name__ == '__main__':
    sol = Solution()
    sol.test(1, 2, 2)
    sol.test(2, 6, 3)
    sol.test(3, 14, 4)
    sol.test(2, 2, 2)
    sol.test(2,9,5)

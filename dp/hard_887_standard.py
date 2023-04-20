"""
给你 k 枚相同的鸡蛋，并可以使用一栋从第 1 层到第 n 层共有 n 层楼的建筑。

已知存在楼层 f ，满足 0 <= f <= n ，任何从 高于 f 的楼层落下的鸡蛋都会碎，从 f 楼层或比它低的楼层落下的鸡蛋都不会破。

每次操作，你可以取一枚没有碎的鸡蛋并把它从任一楼层 x 扔下（满足 1 <= x <= n）。如果鸡蛋碎了，你就不能再次使用它。如果某枚鸡蛋扔下后没有摔碎，则可以在之后的操作中 重复使用 这枚鸡蛋。

请你计算并返回要确定 f 确切的值 的 最小操作次数 是多少？
2023年4月19日11:41:39 2023年4月19日12:25:15 Failure，我不想使用dp，我认为一个二分就可以了。
"""
import numpy as np


class Solution:
    def superEggDrop(self, k: int, n: int):
        memo = dict()

        def dp(k, n):
            # base
            if k == 1:
                return n
            if n == 0:
                return 0
            # memo
            if (k, n) in memo:
                return memo[(k, n)]

            # logistical core
            res = np.inf
            low, high = 1, n
            while low <= high:
                mid = (low + high) // 2
                # 中点投一次，假定碎了,获得最小次数
                broken = dp(k - 1, mid - 1)
                # 没碎，获得最小次数
                not_broken = dp(k, n - mid)
                # 最坏情况发生在broken
                if broken > not_broken:
                    high = mid - 1
                    res = min(res, broken + 1)
                else:
                    low = mid + 1
                    res = min(res, not_broken + 1)

            memo[(k, n)] = res
            return res

        return dp(k, n)

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

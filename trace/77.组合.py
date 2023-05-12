"""
给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
你可以按 任何顺序 返回答案。
示例 1：
输入：n = 4, k = 2
输出：
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
示例 2：
输入：n = 1, k = 1
输出：[[1]]
"""

import numpy as np


class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []
        path = []

        def dfs(j) -> None:
            # 树中的第j层，从j+1开始选
            if len(path) == k:
                res.append(path.copy())
            else:
                if path is None or len(path) == 0:
                    start_pos = 1
                else:
                    start_pos = path[len(path) - 1] + 1
                for i in range(start_pos, n + 1):
                    if n - i + 1 < k - len(path):  # 还剩下的元素 < 还需要的元素
                        return
                    else:
                        path.append(i)
                        dfs(j + 1)
                        path.pop()
        dfs(0)
        return res


if __name__ == '__main__':
    test1 = Solution().combine(4, 2)
    test2 = Solution().combine(1, 1)
    test3 = Solution().combine(3, 3)
    wt = True

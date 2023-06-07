"""
按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。
n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
"""

import numpy as np


class Solution:
    # 存储结果的类变量
    result = []

    def solveNQueens(self, n: int) -> list[list[str]]:
        Solution.result.clear()
        if n == 0:
            return []
        flag = np.array([[False for j in range(n)] for i in range(n)])
        self.nQueensCore(0, n, flag)
        return self.convertFlag(n)

    def findPos(self, row, n, flag):
        result = []
        for j in range(n):
            if any(flag[:, j]):  # 竖行有
                continue
            # 对角线有，此时会被左上和右上攻击
            can_pos = True
            for k in range(min(row, j) + 1):
                # (i,n)的左上是(i-k,n-k)
                if flag[row - k][j - k]:
                    can_pos = False
            for k in range(row + 1):
                if j + k < n and flag[row - k][j + k]:
                    can_pos = False
            if can_pos:
                result.append(j)
        return result

    def convertFlag(self, n):
        result = []
        for each in Solution.result:
            temp = []
            for i in range(len(each)):
                temp.append('')
                for j in range(len(each)):
                    if each[i][j]:
                        temp[len(temp) - 1] += 'Q'
                    else:
                        temp[len(temp) - 1] += '.'
            result.append(temp)
        return result

    def nQueensCore(self, i: int, n: int, flag):
        position = self.findPos(i, n, flag)
        for j in position:
            flag[i][j] = True
            if i == n - 1:
                Solution.result.append(flag.copy())
            else:
                self.nQueensCore(i + 1, n, flag)
            flag[i][j] = False


if __name__ == '__main__':
    Solution().solveNQueens(4)

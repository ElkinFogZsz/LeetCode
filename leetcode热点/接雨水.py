"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
"""

import numpy as np


class Solution:
    def trap(self, height: list[int]) -> int:
        """ min(max左，max右）-自己"""
        sum = 0
        left_max_list = []
        maxV = -np.inf
        for i in range(len(height)):
            if height[i] > maxV:
                maxV = height[i]
            left_max_list.append(maxV)

        maxV = -np.inf
        right_max_list = []
        for i in range(len(height) - 1, -1, -1):
            if height[i] > maxV:
                maxV = height[i]
            right_max_list.append(maxV)
        right_max_list.reverse()
        for i in range(1, len(height) - 1):
            left_max = left_max_list[i - 1]
            right_max = right_max_list[i + 1]
            sum += max((min(left_max, right_max) - height[i]), 0)
        return sum


if __name__ == '__main__':
    test1 = Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    test2 = Solution().trap([4, 2, 0, 3, 2, 5])
    test3 = Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    pass

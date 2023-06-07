"""
给定 m 个数组，每个数组都已经按照升序排好序了。现在你需要从两个不同的数组中选择两个整数（每个数组选一个）并且计算它们的距离。
两个整数 a 和 b 之间的距离定义为它们差的绝对值 |a-b| 。你的任务就是去找到最大距离
两个不同的数组
示例 1：
输入：
[[1,2,3],
 [4,5],
 [1,2,3]]
输出： 4
解释：
一种得到答案 4 的方法是从第一个数组或者第三个数组中选择 1，同时从第二个数组中选择 5 。
"""
import numpy as np


class Solution:
    def maxDistance(self, arrays: list[list[int]]) -> int:
        if arrays is None or len(arrays) < 2:
            return -1
        interval = (min(arrays[0]), max(arrays[0]))
        distance = -np.inf
        for i in range(1, len(arrays)):
            each = (min(arrays[i]), max(arrays[i]))
            temp = max(abs(interval[0] - each[1]), abs(interval[1] - each[0]))
            distance = max(temp, distance)
            interval = (min(each[0], interval[0]), max(each[1], interval[1]))

        return distance


if __name__ == '__main__':
    print(Solution().maxDistance([[1, 2, 3], [4, 5], [1, 2, 3]]))

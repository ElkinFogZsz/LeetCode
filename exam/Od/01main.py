"""
和为sum的最长连续子序列长度
"""

import sys


class Solution(object):
    def main(self, data: list) -> int:
        if len(data[0])==0:
            return -1
        if len(data[0])==1:
            if sum(data[0]) == data[1][0]:
                return 1
            else:
                return -1
        """维护一个窗口"""
        target = data[1][0]
        data = data[0]
        n = len(data)
        min_window_size = -1
        for i in range(n):
            for j in range(i + 1, n):
                if sum(data[i:j + 1]) < target:
                    continue
                elif sum(data[i:j + 1]) == target:
                    min_window_size = max(min_window_size, j - i + 1)
                else:
                    break

        return min_window_size

    def read(self) -> list:
        data = []
        for i in range(2):
            # 读取每一行
            line = sys.stdin.readline().strip()
            # 把每一行的数字分隔后转化成int列表
            values = list(map(int, line.split(',')))
            data.append(values)
        return data


if __name__ == '__main__':
    print(Solution().main(Solution().read()))

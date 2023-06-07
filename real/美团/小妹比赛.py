"""
小美在参加送外卖比赛。比赛共有n个人参加，其中第 i 人的能力值为 i 。
每个人有颜色黄或蓝。如果不同颜色对决，则能力大者赢。如果相同颜色对决，则能力小者赢。
所有人都会两两比赛，请给出每个人能赢多少场。
输入
2

3
0 0 1

4
1 0 1 0
输出
1 0 2
1 2 1 2
"""
"""
小美有两个数字，其中第一个数字是任意的正整数，第二个数字是一位仅可能为0到9间的整数。

小美希望能将第二个插入第一个数字中，以得到最大的数字。具体可参见输入输出样例。
"""
"""
时间限制： 4000MS
内存限制： 557056KB
题目描述：
数列的定义如下： 数列的第一项为n，以后各项为前一项的平方根，求数列的前m项的和。
输入描述
输入数据有多组，每组占一行，由两个整数n（n<10000）和m(m<1000)组成，n和m的含义如前所述。
输出描述
对于每组输入数据，输出该数列的和，每个测试实例占一行，要求精度保留2位小数。
样例输入
81 4    第一项为81,第二项9,第三项3，第四项1.73
2 2
样例输出
94.73
3.41
"""

import math


class Solution(object):
    def maxValue(self):
        data = self.read_multi_line()
        if len(data)==0:
            return
        n = data[0][0]
        for i in range(1,n+1):
            arr = data[2*i]
            res = ''
            for i in range(len(arr)):
                if arr[i] ==0:
                    #统计左侧1的个数 + 右侧0的个数
                    win = str(sum(arr[0:i]) + (len(arr)-i-1) - sum(arr[i+1:len(arr)]))
                else:
                    win = str(sum(arr[i+1:]) + i - sum(arr[0:i]))
                res = res + win + ' '
            print(res)

    def read_multi_line(self):
        n = int(input().strip())
        arr = []
        arr.append([n])
        for i in range(n*2):
            arr.append(list(map(int, input().strip().split())))
        return arr

if __name__ == '__main__':
    Solution().maxValue()

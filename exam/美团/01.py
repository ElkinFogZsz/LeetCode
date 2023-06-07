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
    def sumArray(self):
        data = self.read_multi_line()
        for each in data:
            temp = each[0]
            sum = 0.00
            for i in range(each[1]):
                sum += temp
                temp = math.sqrt(temp)
            print("%.2f" % sum)

    def read_multi_line(self):
        arr = []
        while 1:
            s = input()

            if s != "":
                arr.append(list(map(int, s.split())))
            else:
                break
        return arr


if __name__ == '__main__':
    Solution().sumArray()

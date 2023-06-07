"""
输入描述
输入数据有多组，每组占一行，包括两个整数m和n（100<=m<=n<=999）。
输出描述
对于每个测试实例，要求输出所有在给定范围内的水仙花数，就是说，输出的水仙花数必须大于等于m,并且小于等于n，如果有多个，
则要求从小到大排列在一行内输出，之间用一个空格隔开; 如果给定的范围内不存在水仙花数，则输出no; 每个测试实例的输出占一行。
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
    def exam02(self):
        data = self.read_multi_line()
        for each in data:
            res = ''
            for i in range(each[0], each[1] + 1):
                if self.is_special_number(i):
                    res = res + ' ' + str(i)
            if res == '':
                res = 'no'
            print(res)

    def is_special_number(self, i):
        k = i
        sum = 0
        while i >= 10:
            temp = i % 10
            sum += temp ** 3
            i = int(i / 10)
        sum += i ** 3
        if sum == k:
            return True
        else:
            return False

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
    Solution().exam02()

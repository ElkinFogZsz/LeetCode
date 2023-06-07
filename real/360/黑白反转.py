"""
题目描述：
有n个黑白棋子，它们的一面是黑色，一面是白色。
它们被排成一行，位置可以用标号1~n来表示。
一开始，所有的棋子都是黑色向上，有q次操作，每次操作将位置标号在区间[L, R]内的所有棋子翻转（原来黑色变白色，原来白色变黑色）。
请在每次操作后，求这n个棋子中，黑色向上的棋子个数。
输入描述
第一行两个整数 n, q，1 <= n <= 1018, q <= 300;
后面q行，每行两个整数 L,R，1 <= L <=R <= n。
输出描述
q行，每行一个整数，表示每次操作后黑色向上的棋子个数。
样例输入
100 2
1 30
21 40
样例输出
70
70
"""


class Solution(object):
    def main(self, data):
        is_black = [[1, data[0][0]]]
        for i in range(1, data[0][1] + 1):
            re_start, re_end = data[i]
            new_black = []
            for i in range(len(is_black)):
                each = is_black[i]
                if each[0] > re_end or each[1] < re_start:  # 这个黑色区间没被反转
                    continue
                else:
                    if each[0] <= re_start and each[1] >= re_end:  # 全包围
                        if each[0] < re_start:
                            new_black.append([each[0], re_start - 1])
                        if each[1] > re_end:
                            new_black.append([re_end + 1, each[1]])
                    elif each[0] <= re_start and each[1] < re_end:  # 右冒头
                        if each[0] < re_start:
                            new_black.append([each[0], re_start - 1])
                    elif each[0] > re_start and each[1] >= re_end:  # 左冒头
                        if each[1] > re_end:
                            new_black.append([re_end + 1, each[1]])
                    else:  # 被全包围，传入空集
                        continue
            is_black = new_black
            count = 0
            for each in new_black:
                count += (each[1] - each[0] + 1)
            print(count)

    def read_data(self):
        data = []
        m, n = list(map(int, input().strip().split()))
        data.append([m, n])
        for i in range(n):
            data.append(list(map(int, input().strip().split())))
        return data


if __name__ == '__main__':
    data = Solution().read_data()
    Solution().main(data)

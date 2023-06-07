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
    def main(self):
        n, q = [int(x) for x in input().split()]
        flips = [0, n]
        for _ in range(q):
            L, R = [int(x) for x in input().split()]
            flips = sorted(flips + [L - 1, R])
            ans = 0
            for i in range(0, len(flips), 2):
                ans += flips[i + 1] - flips[i]
            print(ans)


if __name__ == '__main__':
    data = Solution().main()

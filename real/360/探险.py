"""
题目描述：
小X在一片大陆上探险，有一天他发现了一个洞穴，洞穴里面有n道门，打开每道门都需要对应的钥匙，
编号为i的钥匙能用于打开第i道门，而且只有在打开了第i (i≥1)道门之后，才能打开第i+1道门，一开始只能打开第1道门。
幸运的是，小X在外面探索的途中，每天都能发现一把能打开这n道门中其中一道门的钥匙，
每天找完钥匙后他都会去打开所有能打开的门。
现在给出他每天找到的钥匙编号，请问每道门分别在哪一天被打开。

输入描述
第一行包含一个正整数n ，表示门的数量。
接下来一行包含n个正整数a1，a2，...，an，其中ai表示第i天他找到的钥匙的编号，能够打开第ai道门，数据保证a1-an为1-n的一个排列。
输出描述
输出一行n个数s1，s2，...，sn，其中si表示第i道门在第si天被打开。
样例输入
5
5 3 1 2 4
样例输出
3 4 4 5 5
"""
import math


class Solution(object):
    def main(self):
        n = int(input())
        nums = [int(x) for x in input().split()]
        doors = [0] * n
        p = 0
        ans = [-1] * n
        for i in range(n):
            doors[nums[i] - 1] = 1
            while p < n and doors[p] == 1:
                ans[p] = i + 1
                p += 1
        print(str(ans)[1:-1].replace(',', ''))


if __name__ == '__main__':
    print(0.498/math.log(2))

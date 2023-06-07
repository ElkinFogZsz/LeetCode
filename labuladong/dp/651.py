"""
假设你有一个特殊的键盘包含下面的按键：

A：在屏幕上打印一个 'A'。
Ctrl-A：选中整个屏幕。
Ctrl-C：复制选中区域到缓冲区。
Ctrl-V：将缓冲区内容输出到上次输入的结束位置，并显示在屏幕上。
现在，你可以 最多 按键 n 次（使用上述四种按键），返回屏幕上最多可以显示 'A' 的个数 。

"""


class Solution:
    def maxA(self, n: int) -> int:
        dp = [0 for i in range(n + 1)]
        for i in range(1, n + 1):
            # 按A
            dp[i] = dp[i - 1] + 1
            # 把任意一个从j开始换成  cA cC cV，此时粘贴板中有dp[j-1]个，粘贴i-j次
            for j in range(2, i):
                dp[i] = max(dp[i], dp[j - 1] * (i - j))
        return dp[n]

    def test(self, n, ans):
        if self.maxA(n) == ans:
            print('√')
        else:
            print('×')


if __name__ == '__main__':
    soul = Solution()
    soul.test(3, 3)
    soul.test(7, 9)

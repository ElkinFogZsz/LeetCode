"""
给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数  。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符
2023年4月18日21:24:01 16mins 无思路。
2023年4月18日21:44:41
"""


class Solution:
    def minDistance(self, word1: str, word2: str):
        m, n = len(word1) + 1, len(word2) + 1
        dp = [[j if i == 0 else 0 for j in range(n)] for i in range(m)]
        for i in range(len(dp)):
            dp[i][0] = i
        for i in range(1, m):
            for j in range(1, n):
                if word1[-i] == word2[-j]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i - 1][j - 1] + 1,
                        dp[i - 1][j] + 1,
                        dp[i][j - 1] + 1
                    )
        return dp[m - 1][n - 1]

    def test(self, word1, word2, ans):
        if self.minDistance(word1, word2) == ans:
            print('√')
        else:
            print('×')


if __name__ == '__main__':
    sol = Solution()
    sol.test('horse', 'ros', 3)
    sol.test('intention', 'execution', 5)
    sol.test('a', '', 1)

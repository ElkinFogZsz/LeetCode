"""
给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。

子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。
"""


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s2 = s[::-1]
        n = len(s)
        dp = [[0 for j in range(n + 1)] for i in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[n][n]

    def test(self, s: str, answer: int):
        if self.longestPalindromeSubseq(s) == answer:
            print('√')
        else:
            print('×')


if __name__ == '__main__':
    soul = Solution()
    soul.test('bbbab', 4)
    soul.test('cbbd', 2)

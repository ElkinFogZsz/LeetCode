"""
给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。

一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。

例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。

2023年4月19日19:24:14 ，×，我可以通过本地的测试用例，但是思考问题不全面。
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [[0 for j in range(m + 1)] for i in range(n + 1)]
        for j in range(1, m + 1):
            for i in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        res = 0
        for each in dp:
            res = max(max(each), res)
        return res

    def test(self, text1, text2, ans):
        if self.longestCommonSubsequence(text1, text2) == ans:
            print('√')
        else:
            print('×')


if __name__ == '__main__':
    sol = Solution()
    sol.test('abcde', 'ace', 3)
    sol.test('abc', 'abc', 3)
    sol.test('abc', 'def', 0)
    sol.test('bl', 'yby', 1)

"""
给你一个字符串 s，找到 s 中最长的回文子串。
如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。
示例 1：

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
示例 2：

输入：s = "cbbd"
输出："bb"
"""
import numpy as np


class Solution(object):
    def main(self, s: str) -> int:
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


if __name__ == '__main__':
    Solution().main('abcde', 'ace')

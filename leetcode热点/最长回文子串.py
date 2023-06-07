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


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[0 if j != i else 1 for j in range(n)] for i in range(n)]

        for k in range(1, n):
            for i in range(n - 1):
                j = i + k
                if j > n - 1:
                    continue
                else:
                    if s[i] == s[j]:
                        if j -i == 1:  # 两个元素
                            dp[i][j] = 2
                        else:
                            if dp[i + 1][j - 1] != 0:
                                dp[i][j] = dp[i + 1][j - 1] + 2
                            else:
                                dp[i][j] = 0
                    else:
                        dp[i][j] = 0

        max_len = max(map(max, dp))
        for i in range(n):
            for j in range(n):
                if dp[i][j] == max_len:
                    return s[i:j + 1]


if __name__ == '__main__':
    test1 = Solution().longestPalindrome('babad')
    test2 = Solution().longestPalindrome('cbbd')
    test3 = Solution().longestPalindrome('cb')
    test4 = Solution().longestPalindrome('aacabdkacaa')
    pass

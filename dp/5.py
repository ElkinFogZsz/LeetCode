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


class Solution:
    def longestPalindrome(self, s: str) -> str:
        return ""

    def test(self, s: str, ans: str):
        if self.test(s) == ans:
            print('√')
        else:
            print('×')


if __name__ == '__main__':
    Solution().test('babad', 'bab')
    Solution().test('cbbd', 'bb')

"""
给你两个字符串 haystack 和 needle ，
请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0 开始）。
如果 needle 不是 haystack 的一部分，则返回  -1 。
 """


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n1, n2 = len(haystack), len(needle)
        i, j = 0, 0
        while i < n1 and j < n2:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == n2 - 1:
                    return i-j
                continue
            else:
                temp, j = self.next(haystack[i - j:i])
                i = i - temp
        return -1

    def next(self, text):
        """找到最长（前缀=后缀），移动到后缀的位置"""
        for ti in range(0, len(text)):
            if text[ti] == text[-ti]:
                continue
            else:
                return ti, ti
        return len(text), 0

    def test(self, haystack, needle, ans):
        if self.strStr(haystack, needle) == ans:
            print('√')
        else:
            print('×')


if __name__ == '__main__':
    # Solution().test('sadbutsad', 'sad')
    # Solution().test('sadbutsad', 'sae')
    Solution().test('ABBABBABAAB', 'ABBABAAB',3)

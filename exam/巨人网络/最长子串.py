class Solution(object):
    def main(self, str1: str) -> int:
        n = len(str1)
        max_len = -1
        for i in range(n):
            for j in range(i, n):
                if len(set(str1[i:j + 1])) <= 2:
                    max_len = max(max_len, j - i + 1)
                else:
                    continue
        return max_len

    def read(self):
        import sys
        input_data = sys.stdin.readline().strip()
        return input_data


if __name__ == '__main__':
    data = Solution().read()
    print(Solution().main(data))

class Solution(object):
    def main(self, k, n):
        memo = {}

        def dp(k, n):
            if k == 1:
                memo[(k, n)] = n
                return n
            elif k == 0 or n == 0:
                return 0
            elif (k, n) in memo.keys():
                return memo[(k, n)]
            else:
                low, high = 1, n
                res = 99999
                while low <= high:
                    mid = (low + high) // 2
                    # 假设挑战失败，则继续试探下面楼层
                    false_time = dp(k - 1, mid - 1)
                    # 假设挑战成功，则继续试探上面楼层
                    succes_time = dp(k, n - mid)
                    # 最坏情况发生在挑战失败
                    if false_time > succes_time:
                        high = mid - 1
                        res = min(res, false_time + 1)
                    else:
                        low = mid + 1
                        res = min(res, succes_time + 1)
                memo[(k, n)] = res
                return memo[(k, n)]

        dp(k, n)
        return memo[(k, n)]

    def read(self):
        import sys
        a = sys.stdin.readline().strip().split()

        return int(a[0]), int(a[1])


if __name__ == '__main__':
    data = Solution().read()
    print(Solution().main(data[0], data[1]))

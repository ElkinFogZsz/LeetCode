class Solution:
    def canPartition(self, nums: list[int]):
        sum_all = sum(nums)
        if sum_all % 2 != 0:
            return False
        else:
            n = len(nums)
            m = int(sum_all / 2)
            dp = [[False for j in range(m)] for i in range(n)]
            for j in range(m):
                if j == nums[0]:
                    dp[0][j] = True
                else:
                    dp[0][j] = False
            for i in range(n):
                for j in range(m):
                    if dp[i - 1][j - nums[i]] or dp[i - 1][j]:
                        dp[i][j] = True
                    else:
                        dp[i][j] = False
        return dp[n - 1][m - 1]

    def test(self, nums, ans):
        if self.canPartition(nums) == ans:
            print('√')
        else:
            print('×')


if __name__ == '__main__':
    Solution().canPartition([1, 5, 11, 5], True)

# 2023-4-18 14:13:26 2023年4月18日14:31:19，×
# 2023年4月18日14:38:23 2023年4月18日14:55:27 ，一遍A。
"""
给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
解题思路：DP,和另一背包实际上是一致的。
"""


class Solution:
    def canPartition(self, nums: list[int]):
        if sum(nums) % 2 != 0:
            return False
        dp = [[False if j != 0 else True for j in range(int(sum(nums) / 2) + 1)] for i in range(len(nums) + 1)]
        for k in range(1, len(nums) + 1):
            for n in range(1, int(sum(nums) / 2) + 1):
                if dp[k - 1][n] or (n - nums[k - 1] >= 0 and dp[k - 1][n - nums[k - 1]]):
                    dp[k][n] = True
                else:
                    dp[k][n] = False
        return dp[len(nums)][int(sum(nums) / 2)]

    @staticmethod
    def test(nums, ans):
        if ans == Solution().canPartition(nums):
            print('√')
        else:
            print('×')


if __name__ == '__main__':
    Solution.test([1, 5, 11, 5], True)
    Solution.test([1, 2, 3, 5], False)

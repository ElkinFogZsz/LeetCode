# 2023年4月18日13:26:41 -> 2023年4月18日13:36:57 A。
"""
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
"""


class Solution:
    def lengthOfLIS(self, nums: list[int]):

        """
            x:数组下标
            dp[x]:以当前为结尾的最长
                dp[x] = max(dp[i])+1 if dp[i]<dp[x] and i<x
        """
        dp = [1] * len(nums)
        for x in range(len(nums)):
            for i in range(0, x):
                if nums[i] < nums[x]:
                    dp[x] = max(dp[x], dp[i] + 1)
        return max(dp)


    @staticmethod
    def test(nums, ans):
        if Solution().lengthOfLIS(nums) == ans:
            print('√')
        else:
            print('×')


if __name__ == '__main__':
    Solution().test([10, 9, 2, 5, 3, 7, 101, 18], 4)
    Solution().test([0, 1, 0, 3, 2, 3], 4)
    Solution().test([7, 7, 7, 7, 7, 7, 7], 1)

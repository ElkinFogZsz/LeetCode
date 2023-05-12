"""
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，
这意味着第一个房屋和最后一个房屋是紧挨着的。
同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。
给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，今晚能够偷窃到的最高金额。
示例 1：
输入：nums = [2,3,2]
输出：3
解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
示例 2：
输入：nums = [1,2,3,1]
输出：4
解释：你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 3：
输入：nums = [1,2,3]
输出：3
"""

import numpy as np


class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        result = -np.inf
        for i in range(n):
            # 构造新的数组
            if i != 0:
                temp = nums[min(i + 2, n):n]  # 先取右侧
            else:
                temp = nums[min(i + 2, n - 1):n - 1]  # 先取右侧
            if i != n - 1:
                temp.extend(nums[0:max(0, i - 2)])  # 再取左侧
            else:
                temp.extend(nums[1:max(0, i - 2)])
            result = max(result, nums[i] + self._rob_no_loop(temp))
        return result

    def _rob_no_loop(self, nums: list[int]):
        if len(nums) == 0:
            return 0
        dp = [[0, 0] for i in range(len(nums) + 1)]
        dp[1] = [0, nums[0]]
        for i in range(2, len(nums) + 1):
            dp[i][0] = max(max(dp[0:i]))
            dp[i][1] = dp[i - 1][0] + nums[i - 1]
        return max(dp[len(nums)])

    def test(self, nums, ans):
        if self.rob(nums) == ans:
            print('√')
        else:
            print('×')


if __name__ == '__main__':
    Solution().test([2, 3, 2], 3)
    Solution().test([1, 2, 3, 1], 4)
    Solution().test([1, 2, 3], 3)

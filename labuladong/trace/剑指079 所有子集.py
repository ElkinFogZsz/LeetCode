"""
给定一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
示例 1：
输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
示例 2：
输入：nums = [0]
输出：[[],[0]]
"""


class Solution:
    result = []

    def subsets(self, nums: list[int]) -> list[list[int]]:
        Solution.result.clear()
        self.traceCore(0, nums, [])
        return Solution.result

    def traceCore(self, i: int, nums: list[int], last: list[int]):
        if i == len(nums):
            Solution.result.append(last)
            return
        else:
            for j in range(2):
                if j == 0:
                    temp = last.copy()
                    self.traceCore(i + 1, nums, temp)
                else:
                    temp = last.copy()
                    temp.append(nums[i])
                    self.traceCore(i + 1, nums, temp)


if __name__ == '__main__':
    test1 = Solution().subsets([1, 2, 3])
    test2 = Solution().subsets([0])

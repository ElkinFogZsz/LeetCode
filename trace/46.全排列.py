"""
46. 全排列
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
示例 1：
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
示例 2：
输入：nums = [0,1]
输出：[[0,1],[1,0]]
示例 3：
输入：nums = [1]
输出：[[1]]
"""


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans, path = [], []

        def dfs(level) -> None:
            if level == len(nums):
                ans.append(path.copy())
            else:
                for i in range(0, len(nums)):
                    if nums[i] not in path:
                        path.append(nums[i])
                        dfs(level + 1)
                        path.pop()

        dfs(0)
        return ans


if __name__ == '__main__':
    test1 = Solution().permute([1, 2, 3])
    test2 = Solution().permute([1])
    wt = True

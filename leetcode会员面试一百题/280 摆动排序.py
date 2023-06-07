"""
给你一个的整数数组 nums, 将该数组重新排序后使 nums[0] <= nums[1] >= nums[2] <= nums[3]...
输入数组总是有一个有效的答案。
示例 1:
输入：nums = [3,5,2,1,6,4]
输出：[3,5,1,6,2,4]
解释：[1,6,2,5,3,4]也是有效的答案
示例 2:
输入：nums = [6,6,5,6,3,8]
输出：[6,6,5,6,3,8]
"""


class Solution:
    def wiggleSort(self, nums: list[int]) -> None:
        nums.sort()
        n = len(nums)
        middle_num = 1 + n // 2
        for i in range(middle_num):


if __name__ == '__main__':
    test = [3, 5, 2, 1, 6, 4]
    Solution().wiggleSort(test)
    print(test)

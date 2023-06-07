"""
和为sum的最长连续子序列长度
"""

import sys


class Solution(object):
    def main(self, data: list) -> list:
        k, n = data[0]
        nums = data[1]
        if nums is None or len(nums) == 0 or len(nums) != n:
            return data
        for i in range(k, -1, -1):
            # target 为正向数组的和
            if (sum(nums) + i) % 2 == 0:
                target = int((sum(nums) + i) / 2)
            else:
                target = int((sum(nums) + i - 1) / 2)
            remain_nums = nums.copy()
            up_nums = []
            res = self.trace(remain_nums, up_nums, target, n)
            if res[0]:
                up_nums, remain_nums = res[2], res[1]
                up_nums.sort()
                up_nums.reverse()
                remain_nums.sort()
                remain_nums.reverse()
                res = []
                for j in range(len(remain_nums)):
                    res.append(up_nums[j])
                    res.append(remain_nums[j])
                if len(remain_nums) < len(up_nums):
                    res.append(up_nums[-1])
                return res
            else:
                continue
        return nums

    def trace(self, remain_nums: list, up_nums: list, target, n):
        if len(up_nums) == int(int(n + 1) / 2) and sum(up_nums) == target:
            return True, remain_nums, up_nums
        elif len(up_nums) >= int(int(n + 1) / 2):
            return False, remain_nums, up_nums
        else:
            for i in range(len(remain_nums)):
                temp = [remain_nums.copy(), up_nums.copy()]
                chosen_num = remain_nums[i]
                remain_nums.remove(chosen_num)
                up_nums.append(chosen_num)
                res = self.trace(remain_nums, up_nums, target, n)
                if res[0]:
                    return res
                else:
                    remain_nums, up_nums = temp
        return False, remain_nums, up_nums

    def read(self) -> list:
        data = []
        for i in range(2):
            # 读取每一行
            line = sys.stdin.readline().strip()
            # 把每一行的数字分隔后转化成int列表
            values = list(map(int, line.split()))
            data.append(values)
        return data


if __name__ == '__main__':
    res_list = Solution().main(Solution().read())
    res = ""
    for each in res_list:
        res = res + str(each) + ' '
    print(res.strip())

from typing import Optional

import numpy as np


# 2023年4月17日16:26:39 - 2023-4-17 17:26:18  一个小时反复写了四遍，if else写不明白。
# 有感，if-else保证覆盖所有情况,for/while/travel注意边界值处理

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    max_path_sum = -np.inf

    def maxPathSum(self, root: Optional[TreeNode]):
        Solution.max_path_sum = -np.inf
        self.travel_tree(root)
        return Solution.max_path_sum

    def travel_tree(self, root: TreeNode):
        # 返回经过该节点且可以向上延伸最大路径和，即只取左右一个方向
        if root is None:
            return -np.inf
        max_left = self.travel_tree(root.left)
        max_right = self.travel_tree(root.right)
        if max_left == -np.inf:
            # 没有左子，最大值可能为 自己，自己和右子，右子
            Solution.max_path_sum = max(Solution.max_path_sum, root.val, max_right, max_right + root.val)
            return max(root.val, root.val + max_left, root.val + max_right)
        else:
            # 有左子，最大值可能为 左，中，右，左中，右中，左中右，
            Solution.max_path_sum = max(Solution.max_path_sum, max_left, max_right, root.val,
                                        max(max_left, max_right) + root.val, max_right + max_left + root.val)
            return max(root.val, root.val + max_left, root.val + max_right)

    @staticmethod
    def test1_maxPathSum():
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        if Solution.maxPathSum(Solution(), root) == 6:
            print('True')
        else:
            print('False')

    @staticmethod
    def test2_maxPathSum():
        root = TreeNode(-10)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        if Solution.maxPathSum(Solution(), root) == 42:
            print('True')
        else:
            print('False')

    @staticmethod
    def test3_maxPathSum():
        root = TreeNode(-3)
        if Solution.maxPathSum(Solution(), root) == -3:
            print('True')
        else:
            print('False')


if __name__ == '__main__':
    Solution.test1_maxPathSum()
    Solution.test2_maxPathSum()
    Solution.test3_maxPathSum()

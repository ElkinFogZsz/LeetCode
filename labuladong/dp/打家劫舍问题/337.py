"""
小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为 root 。
除了 root 之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果 两个直接相连的房子在同一天晚上被打劫 ，房屋将自动报警。
给定二叉树的 root 。返回 在不触动警报的情况下 ，小偷能够盗取的最高金额 。
T1:
输入: root = [3,2,3,null,3,null,1]
输出: 7
解释: 小偷一晚能够盗取的最高金额 3 + 3 + 1 = 7
T2:
输入: root = [3,4,5,1,3,null,1]
输出: 9
解释: 小偷一晚能够盗取的最高金额 4 + 5 = 9
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional
import numpy as np


class Solution:
    MEMORY = {}
    def rob(self, root: Optional[TreeNode]) -> int:
        return max(self._rob(root))

    def _rob(self, root: Optional[TreeNode]) -> list[int]:
        if root is None:
            return [0, 0]
        if root not in Solution.MEMORY.keys():
            result = [max(self._rob(root.left)) + max(self._rob(root.right)),
                      root.val + self._rob(root.left)[0] + self._rob(root.right)[0]
                      ]
            Solution.MEMORY[root] = result
            return result
        else:
            return Solution.MEMORY[root]

    def test(self, root: Optional[TreeNode], ans):
        if self.rob(root) == ans:
            print('√')
        else:
            print('×')


if __name__ == '__main__':
    # test1 = TreeNode(3)
    # test1.left = TreeNode(2)
    # test1.right = TreeNode(3)
    # test1.left.right = TreeNode(3)
    # test1.right.right = TreeNode(1)
    # Solution().test(test1, 7)
    test2 = TreeNode(3)
    test2.right = TreeNode(1)
    test2.right.left = TreeNode(2)
    Solution().test(test2, 5)

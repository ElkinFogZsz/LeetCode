# BST，有两个节点被错误的交换，不改变结构将其改变
# 2023年4月17日15:50 ， 2023-4-17 16:09:24，一遍A掉。
# 先写一个中序遍历，然后填东西，很快就解决掉了。
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    node_mid_list = []
    val_mid_list = []

    def travel(self, root: TreeNode):
        if root.left is not None:
            self.travel(root.left)
        Solution.node_mid_list.append(root)
        Solution.val_mid_list.append(root.val)
        if root.right is not None:
            self.travel(root.right)

    def recoverTree(self, root: Optional[TreeNode]):
        """
        Do not return anything, modify root in-place instead.
        """
        Solution.node_mid_list, Solution.val_mid_list = [], []
        self.travel(root)
        for i in range(len(Solution.node_mid_list)):
            min_val = min(Solution.val_mid_list[i + 1:])
            min_index = Solution.val_mid_list.index(min_val)
            if Solution.val_mid_list[i] > min_val:
                Solution.node_mid_list[i].val, Solution.node_mid_list[min_index].val = \
                    Solution.node_mid_list[min_index].val, Solution.node_mid_list[i].val
                return root


def test1():
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(2)
    return root


if __name__ == '__main__':
    root = test1()
    root = Solution().recoverTree(root)

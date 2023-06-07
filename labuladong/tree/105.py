# 从前序与中序遍历序列构造二叉树
# 2023-4-17 16:09:24 ， 2023年4月17日16:26:39，15分钟一遍A掉。
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]):
        return self.travel_tree(preorder, inorder)

    def travel_tree(self, preorder: list[int], inorder: list[int]):
        if len(preorder) == 0:
            return None
        root_val = preorder[0]
        root_index_in = inorder.index(root_val)
        root = TreeNode(root_val)
        root.left = self.travel_tree(preorder[1:root_index_in + 1], inorder[0:root_index_in])
        root.right = self.travel_tree(preorder[root_index_in + 1:], inorder[root_index_in + 1:])
        return root


class Solution_Test(object):
    @staticmethod
    def buildTree_test01():
        root = Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
        wt = True


if __name__ == '__main__':
    Solution_Test.buildTree_test01()

# 输入两棵二叉树A，B，判断B是不是A的子结构。
#
# 我们规定空树不是任何树的子结构。
#
# 样例
# 树A：
#
#      8
#     / \
#    8   7
#   / \
#  9   2
#     / \
#    4   7
# 树B：
#
#    8
#   / \
#  9   2
# 返回 true ,因为B是A的子结构。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasSubtree(self, pRoot1, pRoot2):
        """
        :type pRoot1: TreeNode
        :type pRoot2: TreeNode
        :rtype: bool
        """
        if not pRoot1 or not pRoot2:
            return False

        return self.isSubtree(pRoot1, pRoot2) or \
               self.hasSubtree(pRoot1.left, pRoot2) or \
               self.hasSubtree(pRoot1.right, pRoot2)

    def isSubtree(self, pRoot1, pRoot2):
        if not pRoot2:
            return True

        if not pRoot1 or pRoot1.val != pRoot2.val:
            return False

        return self.isSubtree(pRoot1.left, pRoot2.left) and \
               self.isSubtree(pRoot1.right, pRoot2.right)

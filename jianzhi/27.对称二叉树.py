# 请实现一个函数，用来判断一棵二叉树是不是对称的。
#
# 如果一棵二叉树和它的镜像一样，那么它是对称的。
#
# 样例
# 如下图所示二叉树[1,2,2,3,4,4,3,null,null,null,null,null,null,null,null]为对称二叉树：
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
#
# 如下图所示二叉树[1,2,2,null,4,4,3,null,null,null,null,null,null]不是对称二叉树：
#     1
#    / \
#   2   2
#    \ / \
#    4 4  3

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.judge(root.left, root.right)

    def judge(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val == root2.val:
            return self.judge(root1.left, root2.right) and self.judge(root1.right, root2.left)
        return False
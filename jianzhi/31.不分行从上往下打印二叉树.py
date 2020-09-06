# 从上往下打印出二叉树的每个结点，同一层的结点按照从左到右的顺序打印。
#
# 样例
# 输入如下图所示二叉树[8, 12, 2, null, null, 6, null, 4, null, null, null]
#     8
#    / \
#   12  2
#      /
#     6
#    /
#   4
#
# 输出：[8, 12, 2, 6, 4]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution:
    def printFromTopToBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        res = []
        q = deque()
        q.append(root)
        while q:
            t = q.popleft()
            res.append(t.val)
            if t.left:
                q.append(t.left)
            if t.right:
                q.append(t.right)
        return res

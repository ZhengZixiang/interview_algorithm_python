# 从上到下按层打印二叉树，同一层的结点按从左到右的顺序打印，每一层打印到一行。
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
# 输出：[[8], [12, 2], [6], [4]]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution(object):
    def printFromTopToBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        res = [[]]
        q = deque()
        q.append(root)
        layer_num = 1
        while q:
            t = q.popleft()
            res[-1].append(t.val)
            if t.left:
                q.append(t.left)
            if t.right:
                q.append(t.right)

            layer_num -= 1
            if layer_num == 0 and len(q) != 0:
                res.append([])
                layer_num = len(q)
        return res
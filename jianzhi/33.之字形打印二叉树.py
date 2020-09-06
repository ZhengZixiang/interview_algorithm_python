# 请实现一个函数按照之字形顺序从上向下打印二叉树。
#
# 即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。
#
# 样例
# 输入如下图所示二叉树[8, 12, 2, null, null, 6, 4, null, null, null, null]
#     8
#    / \
#   12  2
#      / \
#     6   4
# 输出：[[8], [2, 12], [6, 4]]

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
        flag = True
        while q:
            t = q.popleft()
            res[-1].append(t.val)
            if t.left:
                q.append(t.left)
            if t.right:
                q.append(t.right)

            layer_num -= 1
            if layer_num == 0 and len(q) != 0:
                layer_num = len(q)
                if not flag:
                    res[-1] = res[-1][::-1]
                res.append([])
                flag = not flag
        if not flag:
            res[-1] = res[-1][::-1]
        return res

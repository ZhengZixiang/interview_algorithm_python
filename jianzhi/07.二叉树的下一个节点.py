# 给定一棵二叉树的其中一个节点，请找出中序遍历序列的下一个节点。
#
# 注意：
#
# 如果给定的节点是中序遍历序列的最后一个，则返回空节点;
# 二叉树一定不为空，且给定的节点一定不是空节点；
# 样例
# 假定二叉树是：[2, 1, 3, null, null, null, null]， 给出的是值等于2的节点。
#
# 则应返回值等于3的节点。
#
# 解释：该二叉树的结构如下，2的后继节点是3。
#   2
#  / \
# 1   3

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.father = None
class Solution(object):
    def inorderSuccessor(self, q):
        """
        :type q: TreeNode
        :rtype: TreeNode
        """
        while q.right:
            q = q.right
            while q.left:
                q = q.left
            return q

        while q.father and q == q.father.right:
            q = q.father
        return q.father

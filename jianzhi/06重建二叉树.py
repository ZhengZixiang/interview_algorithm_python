# 输入一棵二叉树前序遍历和中序遍历的结果，请重建该二叉树。
#
# 注意:
#
# 二叉树中每个节点的值都互不相同；
# 输入的前序遍历和中序遍历一定合法；
# 样例
# 给定：
# 前序遍历是：[3, 9, 20, 15, 7]
# 中序遍历是：[9, 3, 15, 20, 7]
#
# 返回：[3, 9, 20, null, null, 15, 7, null, null, null, null]
# 返回的二叉树如下所示：
#     3
#    / \
#   9  20
#     /  \
#    15   7

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        ridx = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:ridx + 1], inorder[:ridx])
        root.right = self.buildTree(preorder[ridx + 1:], inorder[ridx + 1:])
        return root

# 输入一棵二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
#
# 从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
#
# 样例
# 给出二叉树如下所示，并给出num=22。
#       5
#      / \
#     4   6
#    /   / \
#   12  13  6
#  /  \    / \
# 9    1  5   1
#
# 输出：[[5,4,12,1],[5,6,6,5]]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.ans = []
        self.path = []

    def findPath(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.dfs(root, sum)
        return self.ans

    def dfs(self, root, sum):
        if not root:
            return None
        self.path.append(root.val)
        sum -= root.val
        if not root.left and not root.right and sum == 0:
            self.ans.append(self.path.copy())
        self.dfs(root.left, sum)
        self.dfs(root.right, sum)
        self.path.pop(-1)

# 请实现两个函数，分别用来序列化和反序列化二叉树。
#
# 您需要确保二叉树可以序列化为字符串，并且可以将此字符串反序列化为原始树结构。
#
# 样例
# 你可以序列化如下的二叉树
#     8
#    / \
#   12  2
#      / \
#     6   4
#
# 为："[8, 12, 2, null, null, 6, 4, null, null, null, null]"
# 注意:
#
# 以上的格式是AcWing序列化二叉树的方式，你不必一定按照此格式，所以可以设计出一些新的构造方式。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.index = -1
        self.li = []

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return 'null,'
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        return str(root.val) + ',' + left + right

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        self.index += 1
        if self.index == 0:
            self.li = data.split(',')
        root = None
        if self.li[self.index] != 'null':
            root = TreeNode(int(self.li[self.index]))
            root.left = self.deserialize(data)
            root.right = self.deserialize(data)
        return root

# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
#
# 如果是则返回true，否则返回false。
#
# 假设输入的数组的任意两个数字都互不相同。
#
# 样例
# 输入：[4, 8, 6, 12, 16, 14, 10]
#
# 输出：true

class Solution:
    def verifySequenceOfBST(self, sequence):
        """
        :type sequence: List[int]
        :rtype: bool
        """
        if not sequence:
            return True
        return self.dfs(0, len(sequence) - 1, sequence)

    def dfs(self, l, r, sequence):
        if l >= r:
            return True
        k = l
        root = sequence[r]
        while k < r and sequence[k] < root:
            k += 1
        for i in range(k, r):
            if sequence[i] < root:
                return False
        return self.dfs(l, k - 1, sequence) and self.dfs(k, r - 1, sequence)

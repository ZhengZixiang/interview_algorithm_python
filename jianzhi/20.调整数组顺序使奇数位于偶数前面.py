# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序。
#
# 使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分。
#
# 样例
# 输入：[1,2,3,4,5]
#
# 输出: [1,3,5,2,4]

class Solution(object):
    def reOrderArray(self, array):
        """
        :type array: List[int]
        :rtype: void
        """
        i, j = 0, len(array) - 1
        while i <= j:
            while i <= j and array[i] % 2 == 1:
                i += 1
            while i <= j and array[j] % 2 == 0:
                j -= 1
            if i < j:
                array[i], array[j] = array[j], array[i]

# 在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
#
# 请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
#
# 样例
# 输入数组：
#
# [
#   [1,2,8,9]，
#   [2,4,9,12]，
#   [4,7,10,13]，
#   [6,8,11,15]
# ]
#
# 如果输入查找数值为7，则返回true，
#
# 如果输入查找数值为5，则返回false。

class Solution(object):
    def searchArray(self, array, target):
        """
        :type array: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not array or not array[0]:
            return False

        i, j = 0, len(array[0]) - 1
        while i < len(array) and j >= 0:
            if array[i][j] == target:
                return True
            elif array[i][j] > target:
                j -= 1
            else:
                i += 1
        return False

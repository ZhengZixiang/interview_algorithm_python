# 输入一个 非空 整型数组，数组里的数可能为正，也可能为负。
#
# 数组中一个或连续的多个整数组成一个子数组。
#
# 求所有子数组的和的最大值。
#
# 要求时间复杂度为O(n)。
#
# 样例
# 输入：[1, -2, 3, 10, -4, 7, 2, -5]
#
# 输出：18


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s, res = 0, float('-inf')
        for x in nums:
            s = x + max(0, s)
            res = max(res, s)
        return res


class Solution2(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res, s = float('-inf'), 0
        for x in nums:
            if s < 0:
                s = 0
            s += x
            res = max(res, s)
        return res

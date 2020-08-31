# 输入一个数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。
#
# 如果有多对数字的和等于s，输出任意一对即可。
#
# 你可以认为每组输入中都至少含有一组满足条件的输出。
#
# 样例
# 输入：[1,2,3,4] , sum=7
#
# 输出：[3,4]


class Solution(object):
    def findNumbersWithSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        st = set()
        for x in nums:
            if target - x in nums:
                return x, target - x
            st.add(x)

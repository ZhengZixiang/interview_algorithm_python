# 给定一个长度为 n 的整数数组 nums，数组中所有的数字都在 0∼n−1 的范围内。
#
# 数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。
#
# 请找出数组中任意一个重复的数字。
#
# 注意：如果某些数字不在 0∼n−1 的范围内，或数组中不包含重复数字，则返回 -1；
#
# 样例
# 给定 nums = [2, 3, 5, 4, 3, 2, 6, 7]。
#
# 返回 2 或 3。

class Solution(object):
    def duplicateInArray(self, nums):
        """
        :type nums: List[int]
        :rtype int
        """
        n = len(nums)
        for x in nums:
            if x < 0 or x >= n:
                return -1
        for i in range(n):
            while i != nums[i] and nums[nums[i]] != nums[i]:
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
            if i != nums[i] and nums[nums[i]] == nums[i]:
                return nums[i]
        return -1

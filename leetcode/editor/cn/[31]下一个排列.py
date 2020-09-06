# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。 
# 
#  如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。 
# 
#  必须原地修改，只允许使用额外常数空间。 
# 
#  以下是一些例子，输入位于左侧列，其相应输出位于右侧列。 
# 1,2,3 → 1,3,2 
# 3,2,1 → 1,2,3 
# 1,1,5 → 1,5,1 
#  Related Topics 数组 
#  👍 642 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = len(nums) - 1
        while k > 0 and nums[k - 1] >= nums[k]:
            k -= 1
        if k <= 0:
            nums[:] = nums[::-1]
        else:
            t = k
            while t < len(nums) and nums[t] > nums[k - 1]:
                t += 1
            nums[t - 1], nums[k - 1] = nums[k - 1], nums[t - 1]
            nums[k:] = nums[k:][::-1]
        return nums

# leetcode submit region end(Prohibit modification and deletion)

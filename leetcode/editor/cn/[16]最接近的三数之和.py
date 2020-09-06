# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和
# 。假定每组输入只存在唯一答案。 
# 
#  
# 
#  示例： 
# 
#  输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  3 <= nums.length <= 10^3 
#  -10^3 <= nums[i] <= 10^3 
#  -10^4 <= target <= 10^4 
#  
#  Related Topics 数组 双指针 
#  👍 560 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        minv = float('inf')
        res = -1
        for i in range(0, len(nums)):
            k = len(nums) - 1
            for j in range(i + 1,  k):
                while k - 1 > j and nums[i] + nums[j] + nums[k - 1] >= target:
                    k -= 1
                s = nums[i] + nums[j] + nums[k]
                if abs(s - target) < minv:
                    minv = abs(s - target)
                    res = s
                if k - 1 > j:
                    s = nums[i] + nums[j] + nums[k - 1]
                    if abs(s - target) < minv:
                        minv = abs(s - target)
                        res = s
        return res

# leetcode submit region end(Prohibit modification and deletion)

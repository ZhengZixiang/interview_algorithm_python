zx# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
# 
#  你的算法时间复杂度必须是 O(log n) 级别。 
# 
#  如果数组中不存在目标值，返回 [-1, -1]。 
# 
#  示例 1: 
# 
#  输入: nums = [5,7,7,8,8,10], target = 8
# 输出: [3,4] 
# 
#  示例 2: 
# 
#  输入: nums = [5,7,7,8,8,10], target = 6
# 输出: [-1,-1] 
#  Related Topics 数组 二分查找 
#  👍 576 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return -1, -1

        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + r >> 1
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1

        if nums[r] != target:
            return -1, -1

        start, l, r = r, r, len(nums) - 1
        while l < r:
            mid = l + r + 1 >> 1
            if nums[mid] <= target:
                l = mid
            else:
                r = mid - 1

        return start, r
# leetcode submit region end(Prohibit modification and deletion)

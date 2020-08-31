# 给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。 
# 
#  请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。 
# 
#  你可以假设 nums1 和 nums2 不会同时为空。 
# 
#  
# 
#  示例 1: 
# 
#  nums1 = [1, 3]
# nums2 = [2]
# 
# 则中位数是 2.0
#  
# 
#  示例 2: 
# 
#  nums1 = [1, 2]
# nums2 = [3, 4]
# 
# 则中位数是 (2 + 3)/2 = 2.5
#  
#  Related Topics 数组 二分查找 分治算法 
#  👍 3120 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        total = len(nums1) + len(nums2)
        if total % 2 == 0:
            left = self.find(nums1, nums2, total // 2)
            right = self.find(nums1, nums2, total // 2 + 1)
            return (left + right) / 2
        else:
            return self.find(nums1, nums2, total // 2 + 1)

    def find(self, nums1, nums2, k):
        if len(nums1) > len(nums2):
            return self.find(nums2, nums1, k)

        if k == 1:
            if not nums1:
                return nums2[0]
            else:
                return min(nums1[0], nums2[0])

        if not nums1:
            return nums2[k - 1]

        si, sj = min(len(nums1), k // 2), k - k // 2
        if nums1[si - 1] > nums2[sj - 1]:
            return self.find(nums1, nums2[sj:], k - sj)
        else:
            return self.find(nums1[si:], nums2, k - si)

# leetcode submit region end(Prohibit modification and deletion)

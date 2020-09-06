# 实现 strStr() 函数。 
# 
#  给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如
# 果不存在，则返回 -1。 
# 
#  示例 1: 
# 
#  输入: haystack = "hello", needle = "ll"
# 输出: 2
#  
# 
#  示例 2: 
# 
#  输入: haystack = "aaaaa", needle = "bba"
# 输出: -1
#  
# 
#  说明: 
# 
#  当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。 
# 
#  对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。 
#  Related Topics 双指针 字符串 
#  👍 554 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# next[i] 所有p[1-i]的相等的前缀和后缀中长度最长的是

class Solution:
    def strStr(self, s: str, p: str) -> int:
        if not p:
            return 0

        n, m = len(s), len(p)
        s, p = ' ' + s, ' ' + p
        next = [0] * (m + 1)
        j = 0
        for i in range(2, m + 1):
            while j > 0 and p[i] != p[j + 1]:
                j = next[j]
            if p[i] == p[j + 1]:
                j += 1
            next[i] = j

        j = 0
        for i in range(1, n + 1):
            while j > 0 and s[i] != p[j + 1]:
                j = next[j]
            if s[i] == p[j + 1]:
                j += 1
            if j == m:
                return i - m  # i - m + 1 - 1

        return -1

# leetcode submit region end(Prohibit modification and deletion)

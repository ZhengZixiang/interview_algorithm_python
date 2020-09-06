# 编写一个函数来查找字符串数组中的最长公共前缀。 
# 
#  如果不存在公共前缀，返回空字符串 ""。 
# 
#  示例 1: 
# 
#  输入: ["flower","flow","flight"]
# 输出: "fl"
#  
# 
#  示例 2: 
# 
#  输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
#  
# 
#  说明: 
# 
#  所有输入只包含小写字母 a-z 。 
#  Related Topics 字符串 
#  👍 1241 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''

        res = ''
        i = 0
        while True:
            if i < len(strs[0]):
                c = strs[0][i]
            else:
                break
            flag = False
            for s in strs[1:]:
                if i >= len(s) or c != s[i]:
                    flag = True
                    break
            if flag:
                break
            else:
                res += c
                i += 1
        return res
# leetcode submit region end(Prohibit modification and deletion)

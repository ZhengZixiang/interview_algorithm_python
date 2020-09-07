# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。 
# 
#  示例 1: 
# 
#  输入: "(()"
# 输出: 2
# 解释: 最长有效括号子串为 "()"
#  
# 
#  示例 2: 
# 
#  输入: ")()())"
# 输出: 4
# 解释: 最长有效括号子串为 "()()"
#  
#  Related Topics 字符串 动态规划 
#  👍 948 👎 0

# leetcode submit region begin(Prohibit modification and deletion)
# 1. 左右括号数量相等
# 2. 任意前缀中左括号数量大于等于右括号数量

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        res, start = 0, -1
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                if stack:
                    stack.pop(-1)
                    if stack:
                        res = max(res, i - stack[-1])
                    else:
                        res = max(res, i - start)
                else:
                    start = i
        return res
# leetcode submit region end(Prohibit modification and deletion)

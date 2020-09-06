# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。 
# 
#  
# 
#  示例： 
# 
#  输入：n = 3
# 输出：[
#        "((()))",
#        "(()())",
#        "(())()",
#        "()(())",
#        "()()()"
#      ]
#  
#  Related Topics 字符串 回溯算法 
#  👍 1280 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 1. 任意前缀中左括号数量大于等于右括号数量
# 2. 左右括号数量相等

class Solution:
    def __init__(self):
        self.res = []
        self.n = -1

    def generateParenthesis(self, n: int) -> List[str]:
        self.n = n
        self.dfs(0, 0, '')
        return self.res

    def dfs(self, lc, rc, seq):
        if lc == self.n and rc == self.n:
            self.res.append(seq)
        else:
            if lc < self.n:
                self.dfs(lc + 1, rc, seq + '(')
            if lc > rc and rc < self.n:
                self.dfs(lc, rc + 1, seq + ')')

# leetcode submit region end(Prohibit modification and deletion)

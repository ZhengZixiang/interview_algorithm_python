# 将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。 
# 
#  比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下： 
# 
#  L   C   I   R
# E T O E S I I G
# E   D   H   N
#  
# 
#  之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。 
# 
#  请你实现这个将字符串进行指定行数变换的函数： 
# 
#  string convert(string s, int numRows); 
# 
#  示例 1: 
# 
#  输入: s = "LEETCODEISHIRING", numRows = 3
# 输出: "LCIRETOESIIGEDHN"
#  
# 
#  示例 2: 
# 
#  输入: s = "LEETCODEISHIRING", numRows = 4
# 输出: "LDREOEIIECIHNTSG"
# 解释:
# 
# L     D     R
# E   O E   I I
# E C   I H   N
# T     S     G 
#  Related Topics 字符串 
#  👍 811 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        res = ''
        step = 2 * numRows - 2
        for i in range(numRows):
            if i == 0 or i == numRows - 1:
                for j in range(i, len(s), step):
                    res += s[j]
            else:
                cnt = 1
                for j in range(i, len(s), step):
                    res += s[j]
                    k = cnt * step - i
                    if k < len(s):
                        res += s[k]
                    cnt += 1
        return res

# leetcode submit region end(Prohibit modification and deletion)

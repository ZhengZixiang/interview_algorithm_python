# 请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100"、"5e2"、"-123"、"3.1416"、"-1E-16"、"012
# 3"都表示数值，但"12e"、"1a3.14"、"1.2.3"、"+-5"及"12e+5.4"都不是。 
# 
#  
#  Related Topics 数学 
#  👍 90 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if s == '':
            return False

        if s[0] == '+' or s == '-':
            s = s[1:]
        if s == '' or s == '.':
            return False

        i, dot, e = 0, 0, 0
        while i < len(s):
            if '0' <= s[i] <= '9':
                i += 1
            elif s[i] == '.':
                dot += 1
                if dot > 1 or e > 0:
                    return False
                i += 1
            elif s[i] == 'e' or
# leetcode submit region end(Prohibit modification and deletion)

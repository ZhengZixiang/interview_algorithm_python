# 请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
#
# 例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。
#
# 但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
#
# 注意:
#
# 小数可以没有整数部分，例如.123等于0.123；
# 小数点后面可以没有数字，例如233.等于233.0；
# 小数点前面和后面可以有数字，例如233.666;
# 当e或E前面没有数字时，整个字符串不能表示数字，例如.e1、e1；
# 当e或E后面没有整数时，整个字符串不能表示数字，例如12e、12e+5.4;
# 样例：
# 输入: "0"
#
# 输出: true

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        if s == '':
            return False

        if s[0] == '+' or s[0] == '-':
            s = s[1:]
        if s == '' or s == '.':  # +, -, .
            return False

        i, dot, e = 0, 0, 0
        while i < len(s):
            if '0' <= s[i] <= '9':
                i += 1
            elif s[i] == '.':
                dot += 1
                if dot > 1 or e > 0:  # 3213.231.12  123e213.123
                    return False
                i += 1
            elif s[i] == 'e' or s[i] == 'E':
                e += 1
                if i == 0 or i + 1 == len(s) or e > 1 or s[i - 1] == '.':  # e213, 2133e, 231e123e31
                    return False
                if s[i + 1] == '+' or s[i + 1] == '-':
                    if i + 2 == len(s):  # 1123e+
                        return False
                    i += 1
                i += 1
            else:
                return False
        return True

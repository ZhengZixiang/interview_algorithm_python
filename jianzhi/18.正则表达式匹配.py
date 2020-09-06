# 请实现一个函数用来匹配包括'.'和'*'的正则表达式。
#
# 模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（含0次）。
#
# 在本题中，匹配是指字符串的所有字符匹配整个模式。
#
# 例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配。
#
# 样例
# 输入：
#
# s="aa"
# p="a*"
#
# 输出:true

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        n, m = len(s), len(p)
        s, p = ' ' + s, ' ' + p
        f = [[False] * (m + 1) for _ in range(n + 1)]
        f[0][0] = True
        for i in range(0, n + 1):
            for j in range(1, m + 1):
                if j + 1 < len(p) and p[j + 1] == '*':
                    continue
                if i > 0 and p[j] != '*':
                    f[i][j] = f[i - 1][j - 1] and (s[i] == p[j] or p[j] == '.')
                elif p[j] == '*':
                    f[i][j] = f[i][j - 2] or i > 0 and f[i - 1][j] and (s[i] == p[j - 1] or p[j - 1] == '.')
        return f[n][m]

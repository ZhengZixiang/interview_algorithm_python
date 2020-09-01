# 实现函数double Power(double base, int exponent)，求base的 exponent次方。
#
# 不得使用库函数，同时不需要考虑大数问题。
#
# 注意：
#
# 不会出现底数和指数同为0的情况
# 当底数为0时，指数一定为正
# 样例1
# 输入：10 ，2
#
# 输出：100
# 样例2
# 输入：10 ，-2
#
# 输出：0.01

class Solution(object):
    def Power(self, base, exponent):
        """
        :type base: float
        :type exponent: int
        :rtype: float
        """
        res, abs_exp = 1, abs(exponent)
        while abs_exp > 0:
            if abs_exp & 1:
                res *= base
            base *= base
            abs_exp >>= 1
        if exponent < 0:
            return 1 / res
        else:
            return res

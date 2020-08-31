# 对于给定的整数序列 A={a1,a2,…,an}，找出两个不重合连续子段，使得两子段中所有数字的和最大。
#
# 我们如下定义函数 d(A)：
#
# d(A)=max1≤s1≤t1<s2≤t2≤n{∑i=s1t1ai+∑j=s2t2aj}
# 我们的目标就是求出 d(A)。
#
# 输入格式
# 第一行是一个整数 T，代表一共有多少组数据。
#
# 接下来是 T 组数据。
#
# 每组数据的第一行是一个整数，代表数据个数据 n，第二行是 n 个整数 a1,a2,…,an。
#
# 输出格式
# 每组数据输出一个整数，占一行，就是 d(A) 的值。
#
# 数据范围
# 1≤T≤30,
# 2≤n≤50000,
# |ai|≤10000
# 输入样例：
# 1
# 10
# 1 -1 2 2 3 -3 4 -4 5 -5
# 输出样例：
# 13
# 样例解释
# 在样例中，我们取{2,2,3,-3,4}和{5}两个子段，即可得到答案。

t = int(input())

for i in range(t):
    n = int(input())
    w = list(map(int, input().split()))

    g, h = [], []
    maxv, s = float('-inf'), 0
    for x in w:
        s = max(0, s) + x
        maxv = max(maxv, s)
        g.append(maxv)

    maxv, s = float('-inf'), 0
    for x in w[::-1]:
        s = max(0, s) + x
        maxv = max(maxv, s)
        h.append(maxv)

    res = float('-inf')
    for i in range(0, n - 1):
        res = max(res, g[i] + h[- i - 2])
    print(res)

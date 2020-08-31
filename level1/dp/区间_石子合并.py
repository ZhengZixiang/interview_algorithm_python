# -*- coding: utf-8 -*-
# 状态表示 集合：dp[i][j] 所有将第i堆石子到第j堆石子合并成一堆石子的合并方式
#          属性：min
# 状态计算
n = int(input().strip())
s = [0] * (n + 1)
w = list(map(int, input().strip().split()))
for i in range(len(w)):
    s[i + 1] = w[i]
    s[i + 1] += s[i]
dp = [[0] * (n + 1) for _ in range(n + 1)]

# 区间DP从2枚举长度
for length in range(2, n + 1):
    # 枚举左右端点
    for l in range(1, n + 2 - length):  # l + length -1 <= n
        r = l + length - 1
        dp[l][r] = float('inf')
        for k in range(l, r):
            dp[l][r] = min(dp[l][r], dp[l][k] + dp[k + 1][r] + s[r] - s[l - 1])

print(dp[1][n])
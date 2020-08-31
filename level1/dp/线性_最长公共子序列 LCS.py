# -*- coding: utf-8 -*-
# 状态表示 集合：所有在第一个序列前i个字母中出现，且在第二个序列前j个字母中出现的子序列
#          属性：max
# 状态计算 

n, m = list(map(int, input().strip().split()))
str_a = input().strip()
str_b = input().strip()

dp = [[0] * (len(str_b) + 1) for _ in range(len(str_a) + 1)]

for i in range(1, len(str_a) + 1):
    for j in range(1, len(str_b) + 1):
        if str_a[i - 1] == str_b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])

print(dp[-1][-1])
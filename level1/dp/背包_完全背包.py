# -*- coding: utf-8 -*-

n, v = list(map(int, input().strip().split()))
v_li, w_li = [], []
for i in range(n):
    v_i, w_i = list(map(int, input().strip().split()))
    v_li.append(v_i)
    w_li.append(w_i)
dp = [[0] * (v + 1) for _ in range(n + 1)]

for i in range(n + 1):
    for j in range(v + 1):
        if j >= v_li[i - 1]:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - v_li[i - 1]] + w_li[i - 1])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[-1][-1])

# 空间优化
n, v = list(map(int, input().strip().split()))
v_li, w_li = [], []
for i in range(n):
    v_i, w_i = list(map(int, input().strip().split()))
    v_li.append(v_i)
    w_li.append(w_i)
dp = [0] * (v + 1)

for i in range(n + 1):
    for j in range(v_li[i - 1], v + 1):
        dp[j] = max(dp[j], dp[j - v_li[i - 1]] + w_li[i - 1])

print(dp[-1])
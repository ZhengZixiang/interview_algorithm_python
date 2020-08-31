# -*- coding: utf-8 -*-
# 状态表示 集合：所有将a[1~i]变成b[1~j]的操作方式
#          属性：min
# 状态计算

n = int(input().strip())
str_a = input().strip()
m = int(input().strip())
str_b = input().strip()

dp = [[0] * (len(str_b) + 1) for _ in range(len(str_a) + 1)]

for i in range(1, len(str_a) + 1):
    dp[i][0] = i
for j in range(1, len(str_b) + 1):
    dp[0][j] = j

for i in range(1, len(str_a) + 1):
    for j in range(1, len(str_b) + 1):
        if str_a[i - 1] == str_b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

print(dp[-1][-1])

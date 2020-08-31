# -*- coding: utf-8 -*-
# 状态表示 dp[i][j] 集合：所有从起点走到i,j的路径 属性：max
# 状态计算 dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + a[i][j]

n = int(input().strip())
triangle = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    triangle[i][1:i + 1] = list(map(int, input().strip().split()))

dp = [[-10000] * (n + 1) for _ in range(n + 1)]  # 求最大，除顶点外初始化为负无穷
dp[1][1] = triangle[1][1]  # 顶点直接初始化
for i in range(2, n + 1):  # 从第二层开始计算
    for j in range(1, n + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]

print(max(dp[n]))
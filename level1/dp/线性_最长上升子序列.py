# -*- coding: utf-8 -*-
# 状态表示 集合：dp[i] 所有以第i个数结尾的上升子序列的属性：max
# 状态计算 dp[i] = max(dp[j] + 1) j = 0, 1, 2, ... , i - 1

n = int(input().strip())
lst = list(map(int, input().strip().split()))

dp = [0] * (n + 1)

for i in range(1, n + 1):
    for j in range(1, i):
        if lst[i - 1] > lst[j - 1]:
            dp[i] = max(dp[i], dp[j])
    dp[i] += 1

print(max(dp))

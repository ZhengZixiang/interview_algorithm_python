# -*- coding: utf-8 -*-
# 看成n个从1到n的数字物品，体积限制为n的每个数字可取无限次的完全背包问题
# 状态表示 dp[i][j] 集合：所有从1到i，总体积恰好是j的选法
#                   属性：count
# 状态计算 dp[i][j] = dp[i - 1][j] + dp[i - 1][j - i] + dp[i - 1][j - 2i] + ... + dp[i - 1][j - si]
#          dp[i][j - i] =            dp[i - 1][j - i] + dp[i - 1][j - 2i] + ... + dp[i - 1][j - si]
#          dp[i][j] = dp[i - 1][j] + dp[i][j - i]
#          dp[j] = dp[j] + dp[j - i]

n = int(input().strip())
dp = [0] * (n + 1)
dp[0] = 1
mod = 1e9 + 7

for i in range(1, n + 1):
    for j in range(i, n + 1):
        dp[j] = (dp[j] + dp[j - i]) % mod

print(int(dp[-1]))

# 状态表示 集合：所有总和是i，并且恰好表示成j个数的和的方案
#          属性：count
# 状态计算 dp[i, j] 拆分成最小值是1和最小值大于1
#                     dp[i-1, j-1]  dp[i-j, j]
#          dp[i, j] = dp[i - 1][j - 1] + dp[i - j, j]
#          res = dp[n, 1] + dp[n, 2] + ... + dp[n, n]
n = int(input().strip())
dp = [[0] * (n + 1) for _ in range(n + 1)]
mod = 1e9 + 7

dp[0][0] = 1
for i in range(1, n + 1):
    for j in range(1, i + 1):
        dp[i][j] = (dp[i - 1][j - 1] + dp[i - j][j]) % mod

res = sum(dp[n][1:n+1]) % mod
print(res)
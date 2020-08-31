# 给定一个包含 n 个正整数的序列，再给定一个正整数 m。
#
# 请你求出该序列的子序列的各元素之和对 m 取模的最大值。
#
# 输入格式
# 第一行包含两个整数 n 和 m。
#
# 第二行包含 n 个正整数。
#
# 输出格式
# 输出一个整数表示结果。
#
# 数据范围
# 1≤n≤34,
# 1≤ai≤109,
# 1≤m≤109
# 输入样例：
# 3 5
# 2 7 8
# 输出样例：
# 4

n, m = list(map(int, input().split()))
a = list(map(int, input().split()))


def dfs(u, k, s, way):
    if u == k:
        way.append(s)
    else:
        dfs(u + 1, k, s, way)
        dfs(u + 1, k, (s + a[u]) % m, way)


left, right = [], []
dfs(0, n // 2, 0, left)
dfs(n // 2, n, 0, right)
left, right = sorted(left), sorted(right)

res = (left[-1] + right[-1]) % m
j = len(right) - 1
for i in range(len(left)):
    while j >= 0 and left[i] + right[j] >= m:
        j -= 1
    if j >= 0:
        res = max(res, (left[i] + right[j]) % m)

print(res)

# 设有一棵二叉树（如下图），其中圈中的数字表示结点中居民的人口，圈边上数字表示结点编号。
#
# 现在要求在某个结点上建立一个医院，使所有居民所走的路程之和为最小，同时约定，相邻结点之间的距离为 1。
#
# 就本图而言，若医院建在 1 处，则距离和为 4+12+2×20+2×40=136；若医院建在 3 处，则距离和为 4×2+13+20+40=81。
#
# 11.png
#
# 输入格式
# 第一行一个整数 n，表示树的结点数。
#
# 接下来的 n 行每行描述了一个结点的状况，其中第 i 行，描述结点 i的具体状况，包含三个整数，整数之间用空格（一个或多个）分隔，其中：第一个数为居民人口数；第二个数为左链接结点编号，为 0 表示无链接；第三个数为右链接结点编号，为 0 表示无链接。
#
# 树的结点编号从 1 到 n。
#
# 输出格式
# 一个整数，表示最小距离和。
#
# 数据范围
# 1≤n≤100，
# 每个地点的居民人口数均不超过100。
#
# 输入样例：
# 5
# 13 2 3
# 4 0 0
# 12 4 5
# 20 0 0
# 40 0 0
# 输出样例：
# 81

def add(a, b):
    global idx
    e[idx], ne[idx], h[a] = b, h[a], idx
    idx += 1


def dfs(u, father, dist):
    s = cnt[u] * dist
    i = h[u]
    while i != -1:
        j = e[i]
        if j != father:
            s += dfs(j, u, dist + 1)
        i = ne[i]
    return s

N = 110
M = N * 2
h, e, ne = [-1] * N, [0] * M, [0] * M
idx = 0
cnt = [0] * N
n = int(input())
for i in range(1, n + 1):
    c, l, r = list(map(int, input().strip().split()))
    cnt[i] = c
    if l > 0:
        add(i, l)
        add(l, i)
    if r > 0:
        add(i, r)
        add(r, i)

res = float('inf')
for i in range(1, n + 1):
    res = min(res, dfs(i, -1, 0))
print(res)

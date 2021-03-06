# 给定一棵树，输出树的根root，孩子最多的结点max以及他的孩子。
#
# 输入格式
# 第一行：n，m，表示树的节点数和边数。
#
# 以下m行：每行两个结点x和y，表示y是x的孩子。
#
# 输出格式
# 第一行：树根：root；
#
# 第二行：孩子最多的结点max；
#
# 第三行：max的孩子（按编号由小到大输出）。
#
# 数据范围
# 1≤n≤100,
# m=n−1,
# 1≤x,y≤1000,
# 数据保证孩子最多的结点唯一。
#
# 输入样例1：
# 8 7
# 4 1
# 4 2
# 1 3
# 1 5
# 2 6
# 2 7
# 2 8
# 输出样例1：
# 4
# 2
# 6 7 8
# 输入样例2：
# 10 9
# 661 43
# 43 270
# 43 155
# 155 691
# 661 201
# 661 768
# 661 889
# 43 302
# 201 98
# 输出样例2：
# 661
# 661
# 43 201 768 889

N = 1010
n, m = list(map(int, input().strip().split()))
st = [False] * N  # 记录结点是否有父结点
g = {}
for i in range(m):
    x, y = list(map(int, input().strip().split()))
    st[y] = True
    if x in g:
        g[x].append(y)
    else:
        g[x] = [y]

node = -1
maxv = -1
for i in range(N):
    if not st[i] and i in g and len(g[i]) > 0:
        print(i)
    if i in g:
        if len(g[i]) > maxv:
            maxv = len(g[i])
            node = i
print(node)
print(' '.join(map(str, sorted(g[node]))))
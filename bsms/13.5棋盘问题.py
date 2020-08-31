# 在一个给定形状的棋盘（形状可能是不规则的）上面摆放棋子，棋子没有区别。
#
# 要求摆放时任意的两个棋子不能放在棋盘中的同一行或者同一列，请编程求解对于给定形状和大小的棋盘，摆放 k 个棋子的所有可行的摆放方案数目 C。
#
# 输入格式
# 输入含有多组测试数据。
#
# 每组数据的第一行是两个正整数 n,k，用一个空格隔开，表示了将在一个 n∗n 的矩阵内描述棋盘，以及摆放棋子的数目。当为-1 -1时表示输入结束。
#
# 随后的 n 行描述了棋盘的形状：每行有 n 个字符，其中 # 表示棋盘区域， . 表示空白区域（数据保证不出现多余的空白行或者空白列）。
#
# 输出格式
# 对于每一组数据，给出一行输出，输出摆放的方案数目 C （数据保证 C<231）。
#
# 数据范围
# n≤8,k≤n
# 输入样例：
# 2 1
# #.
# .#
# 4 4
# ...#
# ..#.
# .#..
# #...
# -1 -1
# 输出样例：
# 2
# 1

def dfs(u, s):
    if s == k:
        return 1
    if u == n:
        return 0

    res = dfs(u + 1, s)
    for i in range(n):
        if g[u][i] == '#' and not st[i]:
            st[i] = True
            res += dfs(u + 1, s + 1)
            st[i] = False
    return res


while True:
    n, k = list(map(int, input().strip().split()))
    if n == -1 and k == -1:
        break

    st = [False] * n
    g = []
    for i in range(n):
        g.append(list(input().strip()))

    print(dfs(0, 0))

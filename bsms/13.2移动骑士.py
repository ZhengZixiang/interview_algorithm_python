# 给定一个 n∗n 的棋盘，以及一个开始位置和终点位置。
#
# 棋盘的横纵坐标范围都是 0∼n。
#
# 将一个国际象棋中的骑士放置在开始位置上，请问将它移动至终点位置至少需要走多少步。
#
# 一个骑士在棋盘上可行的移动方式如下图所示：
#
# QQ截图20191016061524.png
#
# 输入格式
# 第一行包含整数 T，表示共有 T 组测试数据。
#
# 每组测试数据第一行包含整数 n，表示棋盘大小。
#
# 第二行包含两个整数 x,y 用来表示骑士的开始位置坐标 (x,y)。
#
# 第三行包含两个整数 x,y 用来表示骑士的终点位置坐标 (x,y)。
#
# 输出格式
# 每组数据输出一个整数，表示骑士所需移动的最少步数，每个结果占一行。
#
# 数据范围
# 4≤n≤300,
# 0≤x,y≤n
# 输入样例：
# 3
# 8
# 0 0
# 7 0
# 100
# 0 0
# 30 50
# 10
# 1 1
# 1 1
# 输出样例：
# 5
# 28
# 0

from collections import deque


def bfs(x, y):
    q = deque()
    q.append([x, y])

    dx, dy = [-2, -1, 1, 2, 2, 1, -1, -2], [1, 2, 2, 1, -1, -2, -2, -1]
    while len(q) > 0:
        t = q.popleft()
        for i in range(8):
            a = t[0] + dx[i]
            b = t[1] + dy[i]
            if a < 0 or a >= n or b < 0 or b >= n:
                continue
            if dist[a][b] != -1:
                continue
            dist[a][b] = dist[t[0]][t[1]] + 1
            if a == ex and b == ey:
                return dist[a][b]
            q.append([a, b])
    return 0


t = int(input())
for _ in range(t):
    n = int(input())
    sx, sy = list(map(int, input().strip().split()))
    ex, ey = list(map(int, input().strip().split()))
    dist = [[-1] * n for _ in range(n)]
    dist[sx][sy] = 0
    print(bfs(sx, sy))

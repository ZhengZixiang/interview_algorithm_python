# 少年李逍遥的婶婶病了，王小虎介绍他去一趟仙灵岛，向仙女姐姐要仙丹救婶婶。
#
# 叛逆但孝顺的李逍遥闯进了仙灵岛，克服了千险万难来到岛的中心，发现仙药摆在了迷阵的深处。
#
# 迷阵由M×N个方格组成，有的方格内有可以瞬秒李逍遥的怪物，而有的方格内则是安全。
#
# 现在李逍遥想尽快找到仙药，显然他应避开有怪物的方格，并经过最少的方格，而且那里会有神秘人物等待着他。
#
# 现在要求你来帮助他实现这个目标。
#
# 下图显示了一个迷阵的样例及李逍遥找到仙药的路线。
#
# 11.png
#
# 输入格式
# 输入有多组测试数据。
#
# 每组测试数据以两个非零整数 M 和 N 开始。M 表示迷阵行数, N 表示迷阵列数。
#
# 接下来有 M 行, 每行包含 N 个字符,不同字符分别代表不同含义:
#
# 1) ‘@’：少年李逍遥所在的位置；
# 2) ‘.’：可以安全通行的方格；
# 3) ‘#’：有怪物的方格；
# 4) ‘*’：仙药所在位置。
#
# 当在一行中读入的是两个零时，表示输入结束。
#
# 输出格式
# 对于每组测试数据，分别输出一行，该行包含李逍遥找到仙药需要穿过的最少的方格数目(计数包括初始位置的方块)。
#
# 如果他不可能找到仙药, 则输出 -1。
#
# 数据范围
# 1≤N,M≤300
# 输入样例：
# 8 8
# .@##...#
# #....#.#
# #.#.##..
# ..#.###.
# #.#...#.
# ..###.#.
# ...#.*..
# .#...###
# 6 5
# .*.#.
# .#...
# ..##.
# .....
# .#...
# ....@
# 9 6
# .#..#.
# .#.*.#
# .####.
# ..#...
# ..#...
# ..#...
# ..#...
# #.@.##
# .#..#.
# 0 0
# 输出样例：
# 10
# 8
# -1

from collections import deque


def bfs(start):
    q = deque()
    q.append(start)
    dist[start[0]][start[1]] = 0

    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    while len(q) > 0:
        t = q.popleft()
        for i in range(4):
            x, y = t[0] + dx[i], t[1] + dy[i]
            if x < 0 or x >= m or y < 0 or y >= n:
                continue
            if g[x][y] == '#':
                continue
            if dist[x][y] != -1:
                continue
            dist[x][y] = dist[t[0]][t[1]] + 1
            if g[x][y] == '*':
                return dist[x][y]
            q.append([x, y])
    return -1


while True:
    try:
        m, n = list(map(int, input().strip().split()))
        if m == 0 or n == 0:
            break
    except:
        break

    dist = [[-1] * n for _ in range(m)]
    g = []
    for i in range(m):
        g.append(list(input().strip()))

    for i in range(m):
        for j in range(n):
            if g[i][j] == '@':
                start = [i, j]
                break

    print(bfs(start))

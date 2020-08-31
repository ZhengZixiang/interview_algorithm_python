# 在一个 4×4 的棋盘上有 8 个黑棋和 8 个白棋，当且仅当两个格子有公共边，这两个格子上的棋是相邻的。
#
# 移动棋子的规则是交换相邻两个棋子。
#
# 给出一个初始棋盘和一个最终棋盘，请找出一个最短的移动序列使初始棋盘变为最终棋盘。
#
# 输入格式
# 第一行到第四行，每行 4 个数字（0 或者 1），描述了初始棋盘；
#
# 接着是一个空行；
#
# 第六行到第九行，每行 4 个数字（0 或者 1），描述了最终棋盘。
#
# 数字 0 表示白棋，数字 1 表示黑棋。
#
# 输出格式
# 输出一个整数，表示最少的移动步数。数据保证有解。
#
# 输入样例:
# 1111
# 0000
# 1110
# 0010
#
# 1010
# 0101
# 1010
# 0101
# 输出样例：
# 4

from collections import deque


def read():
    s = ''
    for i in range(4):
        s += input().strip()
    state = 0
    for i in range(16):
        if s[i] == '1':
            state += 2 ** i
    return state


def bit_swap(state, x, y):
    a, b = state >> x & 1, state >> y & 1
    if a ^ b != 1:  # 若数字相同，那交换没什么意义
        return state
    state -= a << x
    state -= b << y
    state += a << y
    state += b << x
    return state


def bfs(start, end):
    if start == end:
        return 0

    q = deque()
    q.append(start)
    dist[start] = 0

    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    while len(q) > 0:
        t = q.popleft()
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    x = i + dx[k]
                    y = j + dy[k]
                    if x >= 0 and x < 4 and y >= 0 and y < 4:
                        # 交换i,j和x,y两个格子的棋子
                        state = bit_swap(t, i * 4 + j, x * 4 + y)
                        if dist[state] == -1:
                            dist[state] = dist[t] + 1
                            if state == end:
                                return dist[state]
                            q.append(state)

    return -1


N = 1 << 16
dist = [-1] * N
start = read()
input()
end = read()
print(bfs(start, end))

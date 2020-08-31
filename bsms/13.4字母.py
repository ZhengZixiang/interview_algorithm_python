# 给定一个 R×S 的大写字母矩阵，你的起始位置位于左上角，你可以向上下左右四个方向进行移动，但是不能移出边界，或者移动到曾经经过的字母（左上角字母看作第一个经过的字母）。
#
# 请问，你最多可以经过几个字母。
#
# 输入格式
# 第一行包含两个整数 R 和 S，表示字母矩阵的行和列。
#
# 接下来 R 行，每行包含一个长度为 S 的大写字母构成的字符串，共同构成字母矩阵。
#
# 输出格式
# 输出一个整数，表示最多能够经过的字母个数。
#
# 数据范围
# 1≤R,S≤20
# 输入样例：
# 3 6
# HFDFFB
# AJHGDH
# DGAGEH
# 输出样例：
# 6

def dfs(x, y):
    st.add(g[x][y])
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    sum_ = 0
    for i in range(4):
        a, b = x + dx[i], y + dy[i]
        if a >= 0 and a < r and b >= 0 and b < s:
            if g[a][b] not in st:
                sum_ = max(sum_, dfs(a, b))

    st.remove(g[x][y])
    return sum_ + 1

r, s = list(map(int, input().strip().split()))
g = []
for i in range(r):
    g.append(list(input().strip()))
st = set()
print(dfs(0, 0))

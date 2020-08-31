# 小招正在玩一款修塔游戏，系统中有 n 座高塔，每座高塔由若干个高度相同的方块堆砌而成，修塔游戏的规则为：
#
# 每次从最高塔的塔尖拿走一个方块
# 每次在最低塔的塔尖堆砌一个方块
# 小招每次只能完成上述两个动作中的一个动作。
#
# 游戏的目标是使 n 座高塔中至少有 k 座高塔的高度相同，请问小招最少需要多少次才能完成游戏。
#
# 输入格式
# 输入共有 2 行，第一行为 n 和 k，第二行为 n 座塔的高度组成的数组 a1,a2,…an。
#
# 输出格式
# 输出值为最少需要多少次动作才能完成游戏。
#
# 数据范围
# 1≤k≤n≤200000,
# 1≤aj≤10000
# 输入样例：
# 6 5
# 1 2 2 4 2 3
# 输出样例：
# 3

N = 10010
c, s = [0] * N, [0] * N
n, k = list(map(int, input().strip().split()))
a = list(map(int, input().strip().split()))
max_cnt = 0
for i in range(n):
    c[a[i]] = c[a[i]] + 1
    max_cnt = max(max_cnt, c[a[i]])

if max_cnt >= k:
    print(0)
    exit()

for i in range(1, 10001):
    s[i] = s[i - 1] + i * c[i]

res = 2e9
cnt = 0
for i in range(1, 10001):
    left = cnt * i - s[i - 1]
    right = s[10000] - s[i] - (n - cnt - c[i]) * i
    if cnt + c[i] >= k:
        res = min(res, left - (cnt + c[i] - k))
    if n - cnt >= k:
        res = min(res, right - (n - cnt - k))
    res = min(res, left + right - (n - k))
    cnt += c[i]

print(res)

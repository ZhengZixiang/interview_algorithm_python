# 高二数学《绿色通道》总共有 n 道题目要抄，编号 1,2,…,n，抄第 i 题要花 ai 分钟。
#
# 小 Y 决定只用不超过 t 分钟抄这个，因此必然有空着的题。
#
# 每道题要么不写，要么抄完，不能写一半。
#
# 下标连续的一些空题称为一个空题段，它的长度就是所包含的题目数。
#
# 这样应付自然会引起马老师的愤怒，最长的空题段越长，马老师越生气。
#
# 现在，小 Y 想知道他在这 t 分钟内写哪些题，才能够尽量减轻马老师的怒火。
#
# 由于小 Y 很聪明，你只要告诉他最长的空题段至少有多长就可以了，不需输出方案。
#
# 输入格式
# 第一行为两个整数 n,t。
#
# 第二行为 n 个整数，依次为 a1,a2,…,an。
#
# 输出格式
# 输出一个整数，表示最长的空题段至少有多长。
#
# 数据范围
# 0<n≤5×104,
# 0<ai≤3000,
# 0<t≤108
# 输入样例：
# 17 11
# 6 4 5 2 5 3 4 5 2 3 4 5 2 3 6 3 5
# 输出样例：
# 3

N = 50010
n, t = list(map(int, input().split()))
a = [0] + list(map(int, input().split()))


def check(limit):
    f, q = [0] * N, [0] * N
    hh, tt = 0, 0
    for i in range(1, n + 1):
        if q[hh] < i - limit - 1:
            hh += 1
        f[i] = f[q[hh]] + a[i]
        while hh <= tt and f[q[tt]] >= f[i]:
            tt -= 1
        tt += 1
        q[tt] = i  # q[++tt] = i

    for i in range(n - limit, n + 1):
        if f[i] <= t:
            return True
    return False


l, r = 0, n
while l < r:
    mid = l + r >> 1
    if check(mid):
        r = mid
    else:
        l = mid + 1

print(r)

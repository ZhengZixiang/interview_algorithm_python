# 现在要把 m 本有顺序的书分给 k 个人复制（抄写），每一个人的抄写速度都一样，一本书不允许给两个（或以上）的人抄写，分给每一个人的书，必须是连续的，比如不能把第一、第三和第四本书给同一个人抄写。
#
# 现在请你设计一种方案，使得复制时间最短。
#
# 复制时间为抄写页数最多的人用去的时间。
#
# 输入格式
# 第一行两个整数 m，k。
#
# 第二行 m 个整数，第 i 个整数表示第 i 本书的页数。
#
# 输出格式
# 共 k 行，每行两个整数，第 i 行表示第 i 个人抄写的书的起始编号和终止编号。
#
# k 行的起始编号应该从小到大排列，如果有多解，则尽可能让前面的人少抄写。
#
# 数据范围
# k≤m≤500
# 输入样例：
# 9 3
# 1 2 3 4 5 6 7 8 9
# 输出样例：
# 1 5
# 6 7
# 8 9

m, k = list(map(int, input().split()))
if m == 0:
    exit()

w = list(map(int, input().split()))
left, right = [], []


def check(sum_):
    s, cnt = 0, 1
    right.append(m)
    for i in range(m - 1, -1, -1):
        if s + w[i] <= sum_:
            s += w[i]
        else:
            left.append(i + 2)  # i + 1 + 1
            cnt += 1
            right.append(i + 1)  # i + 1
            s = w[i]

    left.append(1)
    return cnt <= k


l, r = max(w), int(1e9)

while l < r:
    mid = l + r >> 1
    if check(mid):
        r = mid
    else:
        l = mid + 1

check(r)

for i in range(1, k + 1):
    print(left[-i], right[-i])

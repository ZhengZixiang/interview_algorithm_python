# -*- coding: utf-8 -*-
# 二分查找

n = int(input().strip())
a = list(map(int, input().strip().split()))
q = [0] * (n + 1)

length = 0
q[0] = -2e9
for i in range(n):
    l = 0
    r = length
    while l < r:
        mid = (r + l + 1) >> 1
        if a[i] > q[mid]:
            l = mid
        else:
            r = mid - 1
    length = max(length, r + 1)
    q[r + 1] = a[i]

print(length)

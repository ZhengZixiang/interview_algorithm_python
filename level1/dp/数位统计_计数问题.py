# -*- coding: utf-8 -*-

# [a-b], 0-9出现的次数
# count(n, x) 1-n中x出现的次数
# count(b, x) - count(a-1, x)

# 1~n, x=1, n=abcdefg
# 分别求出1在每一位出现的次数
# 如求1在第4位出现的次数
# 1 <= xxx1xxx <= abcdefg
# 1. xxx = 000~abc-1 yyy=000~999, abc * 1000
# 2. xxx = abc
#   2.1 d<1, abc1yyy > abc0efg, 0
#   2.2 d=1, yyy=000~efg, efg+1
#   2.3 d>1, yyy=000~999, 1000

while True:
    a, b = list(map(int, input().strip().split()))

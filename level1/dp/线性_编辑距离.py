# -*- coding: utf-8 -*-

n, m = list(map(int, input().strip().split()))
a_lst, b_lst = [], []
for i in range(n):
    a_lst.append(input().strip())
for i in range(m):
    inp = input().strip().split()
    b_lst.append((inp[0], int(inp[1])))

res = []
for m_idx in range(m):
    res = 0
    str_b, limit = b_lst[m_idx]
    for n_idx in range(n):
        str_a = a_lst[n_idx]

        dp = [[0] * (len(str_b) + 1) for _ in range(len(str_a) +1)]
        for i in range(1, len(str_a) + 1):
            dp[i][0] = i
        for j in range(1, len(str_b) + 1):
            dp[0][j] = j
        for i in range(1, len(str_a) + 1):
            for j in range(1, len(str_b) + 1):
                if str_a[i - 1] == str_b[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1

        if dp[-1][-1] <= limit:
            res += 1
    print(res)

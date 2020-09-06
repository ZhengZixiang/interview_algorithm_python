# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
#
# 样例
# 输入：
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
#
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]

class Solution(object):
    def printMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        n, m = len(matrix), len(matrix[0])
        st = [[False] * m for _ in range(n)]
        dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
        x, y, d = 0, 0, 0
        res = []
        for i in range(n * m):
            res.append(matrix[x][y])
            st[x][y] = True
            a, b = x + dx[d], y + dy[d]
            if a < 0 or a >= n or b < 0 or b >= m or st[a][b]:
                d = (d + 1) % 4
                a = x + dx[d]
                b = y + dy[d]
            x, y = a, b
        return res

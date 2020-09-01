# 地上有一个 m 行和 n 列的方格，横纵坐标范围分别是 0∼m−1 和 0∼n−1。
#
# 一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格。
#
# 但是不能进入行坐标和列坐标的数位之和大于 k 的格子。
#
# 请问该机器人能够达到多少个格子？
#
# 样例1
# 输入：k=7, m=4, n=5
#
# 输出：20
# 样例2
# 输入：k=18, m=40, n=40
#
# 输出：1484
#
# 解释：当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
#       但是，它不能进入方格（35,38），因为3+5+3+8 = 19。
# 注意:
#
# 0<=m<=50
# 0<=n<=50
# 0<=k<=100

from collections import deque


class Solution(object):
    def movingCount(self, threshold, rows, cols):
        """
        :type threshold: int
        :type rows: int
        :type cols: int
        :rtype: int
        """
        if not rows or not cols:
            return 0

        res = 0
        st = [[False] * cols for _ in range(rows)]
        queue = deque()
        queue.append([0, 0])
        while len(queue) > 0:
            tx, ty = queue.popleft()
            if self.get_sum(tx, ty) > threshold or st[tx][ty]:
                continue
            st[tx][ty] = True
            res += 1
            dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
            for d in range(4):
                x, y = tx + dx[d], ty + dy[d]
                if 0 <= x < rows and 0 <= y < cols:
                    queue.append([x, y])
        return res

    def get_sum(self, x, y):
        return self.get_single_sum(x) + self.get_single_sum(y)

    def get_single_sum(self, x):
        s = 0
        while x:
            s += x % 10
            x //= 10
        return s

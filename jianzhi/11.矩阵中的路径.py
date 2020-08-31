# 请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
#
# 路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
#
# 如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。
#
# 注意：
#
# 输入的路径不为空；
# 所有出现的字符均为大写英文字母；
# 样例
# matrix=
# [
#   ["A","B","C","E"],
#   ["S","F","C","S"],
#   ["A","D","E","E"]
# ]
#
# str="BCCE" , return "true"
#
# str="ASAE" , return "false"

class Solution(object):
    def hasPath(self, matrix, string):
        """
        :type matrix: List[List[str]]
        :type string: str
        :rtype: bool
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if self.dfs(matrix, string, i, j, 0):
                    return True
        return False

    def dfs(self, matrix, string, i, j, idx):
        if matrix[i][j] != string[idx]:
            return False
        if idx == len(string) - 1:
            return True
        t, matrix[i][j] = matrix[i][j], '#'
        dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
        for d in range(4):
            x = i + dx[d]
            y = j + dy[d]
            if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]):
                if self.dfs(matrix, string, x, j, idx + 1):
                    return True
        matrix[i][j] = t
        return False

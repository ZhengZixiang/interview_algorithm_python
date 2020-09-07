# 编写一个程序，通过已填充的空格来解决数独问题。 
# 
#  一个数独的解法需遵循如下规则： 
# 
#  
#  数字 1-9 在每一行只能出现一次。 
#  数字 1-9 在每一列只能出现一次。 
#  数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。 
#  
# 
#  空白格用 '.' 表示。 
# 
#  
# 
#  一个数独。 
# 
#  
# 
#  答案被标成红色。 
# 
#  Note: 
# 
#  
#  给定的数独序列只包含数字 1-9 和字符 '.' 。 
#  你可以假设给定的数独只有唯一解。 
#  给定数独永远是 9x9 形式的。 
#  
#  Related Topics 哈希表 回溯算法 
#  👍 520 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def __init__(self):
        N = 10
        self.row, self.col = [[False] * N for _ in range(N)], [[False] * N for _ in range(N)]
        self.cell = [[[False] * N for _ in range(N)] for _ in range(N)]

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    t = int(board[i][j])
                    self.row[i][t], self.col[j][t], self.cell[i // 3][j // 3][t] = True, True, True
        self.dfs(board, 0, 0)

    def dfs(self, board, x, y):
        if y == 9:
            return self.dfs(board, x + 1, 0)
        if x == 9:
            return True

        if board[x][y] != '.':
            return self.dfs(board, x, y + 1)

        for i in range(1, 10):
            if not self.row[x][i] and not self.col[y][i] and not self.cell[x // 3][y // 3][i]:
                self.row[x][i], self.col[y][i], self.cell[x // 3][y // 3][i] = True, True, True
                board[x][y] = str(i)
                if self.dfs(board, x, y + 1):
                    return True
                board[x][y] = '.'
                self.row[x][i], self.col[y][i], self.cell[x // 3][y // 3][i] = False, False, False
        return False

# leetcode submit region end(Prohibit modification and deletion)

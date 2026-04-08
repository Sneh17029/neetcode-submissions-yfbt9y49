class Solution:
    def isValidSudoku(self, board):
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]
        for i in range(9):
                for j in range(9):
                        box_index = (i//3)*3 + j//3
                        val = board[i][j]
                        if val == ".":
                                continue
                        if val in row[i] or  val in col[j] or val in box[box_index]:
                                return False
                        row[i].add(val)
                        col[j].add(val)
                        box[box_index].add(val)
        return True
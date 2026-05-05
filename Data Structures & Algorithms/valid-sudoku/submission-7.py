class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        corner_indices=[(0,0),(3,0),(6,0),(0,3),(3,3),(6,3),(0,6),(3,6),(6,6)]
        for i in corner_indices:
            nine_subboxes = []
            for j in range(3):
                for k in range(3):
                    value = board[i[0] + j][i[1] + k]
                    if value != ".":
                        nine_subboxes.append(value)
            if len(nine_subboxes) != len(set(nine_subboxes)):
                return False

        for i in range(9):
            row = board[i]
            row_values = []
            for value in row:
                if value != ".":
                    row_values.append(value)
            if len(row_values) != len(set(row_values)):
                return False
            ith_column = []
            for j in range(9):
                value = board[j][i]
                if value != ".":
                    ith_column.append(value)
            if len(ith_column) != len(set(ith_column)):
                return False
        return True

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = [x for x in board[i] if x != '.']
            if len(row) != len(set(row)):
                return False
        
        for j in range(9):
            col = [board[i][j] for i in range(9) if board[i][j] != '.']
            if len(col) != len(set(col)):
                return False
        
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                x = []
                for i in range(3):
                    for j in range(3):
                        if board[box_row + i][box_col + j] != '.':
                            x.append(board[box_row + i][box_col + j])
                if len(x) != len(set(x)):
                    return False
        
        return True

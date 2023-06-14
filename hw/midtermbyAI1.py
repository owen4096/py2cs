# Create an empty chessboard
def create_empty_board(n):
    board = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        board.append(row)
    return board

n = 8
board = create_empty_board(n)


def is_valid(board, row, col):
    # 檢查同行是否有皇后
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    # 檢查左上到右下的對角線是否有皇后
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    
    # 檢查左下到右上的對角線是否有皇后
    i, j = row, col
    while i < len(board) and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1
    
    return True

def solve_n_queens(board, col):
    # 所有列都放置完畢，表示找到一組解法
    if col >= len(board):
        return True
    
    for i in range(len(board)):
        # 檢查是否可以放置皇后在該位置
        if is_valid(board, i, col):
            # 放置皇后
            board[i][col] = 1

            # 遞迴進入下一列
            if solve_n_queens(board, col+1):
                return True

            # 若遞迴無法找到解法，回復該位置為空
            board[i][col] = 0
    
    return False

def n_queens(n):
    # 初始化棋盤
    board = [[0 for _ in range(n)] for _ in range(n)]

    # 呼叫遞迴函式尋找解法
    if solve_n_queens(board, 0):
        return board
    else:
        return None

# 測試
n = 3
board = n_queens(n)
if board:
    for row in board:
        print(row)
else:
    print(f"No solution for {n}-queens problem.")




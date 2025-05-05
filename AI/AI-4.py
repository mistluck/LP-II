def print_board(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print("\n")

# --- Backtracking Approach ---
def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col]:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j]:
            return False
    return True

def solve_n_queens_backtracking(board, row, n):
    if row == n:
        print_board(board)
        return True

    found_solution = False
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = True
            found_solution = solve_n_queens_backtracking(board, row + 1, n) or found_solution
            board[row][col] = False
    return found_solution

def n_queens_backtracking(n):
    board = [[False] * n for _ in range(n)]
    if not solve_n_queens_backtracking(board, 0, n):
        print("No solution exists.")

# --- Branch and Bound Approach ---
def is_safe_branch_and_bound(row, col, cols, diags1, diags2, n):
    return not (cols[col] or diags1[row + col] or diags2[row - col + (n - 1)])

def solve_n_queens_branch_and_bound(row, n, cols, diags1, diags2, board):
    if row == n:
        print_board(board)
        return True

    found_solution = False
    for col in range(n):
        if is_safe_branch_and_bound(row, col, cols, diags1, diags2, n):
            board[row][col] = True
            cols[col] = diags1[row + col] = diags2[row - col + (n - 1)] = True

            found_solution = solve_n_queens_branch_and_bound(row + 1, n, cols, diags1, diags2, board) or found_solution

            board[row][col] = False
            cols[col] = diags1[row + col] = diags2[row - col + (n - 1)] = False
    return found_solution

def n_queens_branch_and_bound(n):
    board = [[False] * n for _ in range(n)]
    cols = [False] * n
    diags1 = [False] * (2 * n - 1)  # '/' diagonals
    diags2 = [False] * (2 * n - 1)  # '\' diagonals
    if not solve_n_queens_branch_and_bound(0, n, cols, diags1, diags2, board):
        print("No solution exists.")

n = 4
print("Backtracking Solutions:")
n_queens_backtracking(n)

print("Branch and Bound Solutions:")
n_queens_branch_and_bound(n)

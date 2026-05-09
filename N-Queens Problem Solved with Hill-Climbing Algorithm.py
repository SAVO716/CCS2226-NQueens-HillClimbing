import random

def get_h_cost(board):
    """Calculates the number of pairs of queens attacking each other."""
    h = 0
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            # Same row
            if board[i] == board[j]:
                h += 1
            # Same diagonal
            if abs(board[i] - board[j]) == abs(i - j):
                h += 1
    return h

def hill_climbing(n):
    # Start with a random board: each index is a column, value is the row
    current_board = [random.randint(0, n - 1) for _ in range(n)]
    current_h = get_h_cost(current_board)
    
    steps = 0
    while current_h > 0:
        steps += 1
        neighbor_board = list(current_board)
        # Try a random move: pick a queen and move it to a different row
        col = random.randint(0, n - 1)
        row = random.randint(0, n - 1)
        neighbor_board[col] = row
        
        neighbor_h = get_h_cost(neighbor_board)
        
        # If the move improves the situation (lower h), accept it
        if neighbor_h < current_h:
            current_board = neighbor_board
            current_h = neighbor_h
            
        # Reset if stuck in local optimum for too many steps
        if steps > 1000:
            current_board = [random.randint(0, n - 1) for _ in range(n)]
            current_h = get_h_cost(current_board)
            steps = 0
            
    return current_board

def print_board(board):
    n = len(board)
    for row in range(n):
        line = ""
        for col in range(n):
            if board[col] == row:
                line += " Q "
            else:
                line += " . "
        print(line)

# Solve for N=8
n_size = 8
solution = hill_climbing(n_size)
print(f"N-Queens Solution for N={n_size}:")
print_board(solution)
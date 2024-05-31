import math

X = "X"
O = "O"
EMPTY = None

def initial_state():

    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):

    countX = 0
    countO = 0

    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == X:
                countX += 1
            if board[row][col] == O:
                countO += 1
    if countX > countO:
        return O
    else:
        return X

def actions(board):

    allPossibleActions = set()

    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == EMPTY:
                allPossibleActions.add(row * 3 + col)  # Convert coordinates to a single number
    return allPossibleActions

def result(board, action):

    if action not in actions(board):
        raise Exception("NOT valid location")

    row = action // 3  # Convert the single number back to row index
    col = action % 3   # Convert the single number back to column index
    board_copy = [row[:] for row in board]  # Create a new board by copying each row
    board_copy[row][col] = player(board)  # Apply the player's move to the new board
    return board_copy

def checkRow(board, player):

    for row in range(len(board)):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
    return False

def checkCol(board, player):

    for col in range(len(board)):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    return False

def checkFirstDig(board, player):

    count = 0
    for row in range(len(board)):
        if board[row][row] == player:
            count += 1
    if count == 3:
        return True
    return False

def checkSecondDig(board, player):

    count = 0
    for row in range(len(board)):
        if board[row][len(board) - row - 1] == player:
            count += 1
    if count == 3:
        return True
    return False

def winner(board):

    if checkRow(board, X) or checkCol(board, X) or checkFirstDig(board, X) or checkSecondDig(board, X):
        return X
    elif checkRow(board, O) or checkCol(board, O) or checkFirstDig(board, O) or checkSecondDig(board, O):
        return O
    else:
        return None

def terminal(board):

    if winner(board) is not None:
        return True
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                return False
    return True

def utility(board):

    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def max_value(board):

    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):

    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v

def minimax(board):

    if terminal(board):
        return None

    current_player = player(board)
    if current_player == X:
        best_value = -math.inf
        best_move = None
        for action in actions(board):
            move_value = min_value(result(board, action))
            if move_value > best_value:
                best_value = move_value
                best_move = action
        return best_move
    else:
        best_value = math.inf
        best_move = None
        for action in actions(board):
            move_value = max_value(result(board, action))
            if move_value < best_value:
                best_value = move_value
                best_move = action
        return best_move

def play_game():

    board = initial_state()
    while not terminal(board):
        print_board(board)
        if player(board) == X:
            move = int(input("Enter your move (0-8): "))
            if move in actions(board):
                board = result(board, move)
            else:
                print("Invalid move. Try again.")
        else:
            move = minimax(board)
            board = result(board, move)

    print_board(board)
    if winner(board) == X:
        print("X wins!")
    elif winner(board) == O:
        print("O wins!")
    else:
        print("It's a tie!")

def print_board(board):

    for row in board:
        print(" | ".join([cell if cell is not None else " " for cell in row]))
        print("-" * 9)


play_game()
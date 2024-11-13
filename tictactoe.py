"""
Tic Tac Toe Player
"""
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = 0
    o_count = 0
    for row in board:
        x_count += row.count('X')
        o_count += row.count('O')
    
    # If counts are equal, it's X's turn; otherwise, it's O's turn
    if x_count <= o_count:
        return 'X'
    else:
        return 'O'
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()  # Initialize an empty set
    for i in range(3):  # Loop through rows
        for j in range(3):  # Loop through columns
            if board[i][j] is None:  # Check if the cell is empty
                possible_actions.add((i, j))  # Add the empty cell as a tuple
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    if board[i][j] is not None:
        raise Exception("Invalid action: cell is already occupied")

    new_board = [row.copy() for row in board] 
    # Get the current player's mark ('X' or 'O')
    current_player = player(board)
    
    # Apply the action to the copied board
    new_board[i][j] = current_player
    
    return new_board
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one. Otherwise, returns None.
    """
    # Check rows for a win
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]
    
    # Check columns for a win
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]
    
    # Check diagonals for a win
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    
    # If no winner, return None
    return None
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over (either because someone has won or all cells are filled), False otherwise.
    """
    # Check if there is a winner
    if winner(board) is not None:
        return True
    
    # Check if all cells are filled (tie)
    for row in board:
        if None in row:  # If any cell is empty, the game is not over
            return False
    
    # If no winner and no empty cells, it's a tie
    return True
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == 'X':
            return 1
        elif winner(board) == 'O':
            return -1
        else:
            return 0
    


def minimax(board):
    """
    Returns the optimal move for the current player on the board.
    """
    if terminal(board):
        return None

    current_player = player(board)  # Determine whose turn it is ('X' or 'O')
    
    # Define a helper function to recursively calculate minimax value
    def maximize(board):
        if terminal(board):
            return utility(board), None
        max_score = float('-inf')
        best_move = None
        for action in actions(board):
            score, _ = minimize(result(board, action))
            if score > max_score:
                max_score = score
                best_move = action
        return max_score, best_move

    def minimize(board):
        if terminal(board):
            return utility(board), None
        min_score = float('inf')
        best_move = None
        for action in actions(board):
            score, _ = maximize(result(board, action))
            if score < min_score:
                min_score = score
                best_move = action
        return min_score, best_move

    # Call the appropriate helper function based on the current player
    if current_player == 'X':
        _, optimal_move = maximize(board)
    else:
        _, optimal_move = minimize(board)
    
    return optimal_move

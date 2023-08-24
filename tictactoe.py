"""
Tic Tac Toe Player
"""

import math
import copy

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
    count = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != EMPTY:
                count = count + 1


    if count%2 == 0:
        return X
    else:
        return O
    #raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action_set = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                action_set.add(board[i][j])

    return action_set
    # raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    action_set = actions(board)
    current_player = player(board)
    new_board = copy.deepcopy(board)
    if action not in action_set:
        raise Exception("action is not valid")

    new_board[action[0]][action[1]] = current_player

    return new_board
    #raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != EMPTY:
                if board[i][j] == board[i][(j+1)%2] and board[i][j] == board[i][(j+2)%2]:
                    return board[i][j]
                elif board[i][j] == board[(i+1)%2][j] and board[i][j] == board[(i+2)%2][j]:
                    return board[i][j]
                elif i == 0 and j == 0 and board[i][j] == board[i+1][j+1] and board[i][j] == board[i+2][j+2]:
                    return board[i][j]
                elif i == 0 and j == 2 and board[i][j] == board[i+1][j-1] and board[i][j] == board[i+2][j-2]:
                    return board[i][j]

    return None
    #raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    remaining_actions = actions(board)
    if len(remaining_actions) == 0:
        return True
    
    has_a_winner = winner(board)
    if has_a_winner is not None:
        return True

    return False
    #raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    remaining_actions = actions(board)
    has_a_winner = winner(board)
    if len(remaining_actions) == 0 and has_a_winner is None:
        return 0
    
    if has_a_winner == X:
        return 1
    elif has_a_winner == O:
        return -1

    raise Exception("Game has not yet ended")

    # raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError

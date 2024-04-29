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
    num_x = 0
    num_o = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                num_x += 1
            elif board[i][j] == O:
                num_o += 1
    return O if num_x > num_o else X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    avalible = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                avalible.append((i,j))
    return avalible


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Invalid")
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in board:
        if i[0] == i[1] == i[2] and i[0] != EMPTY:
            return i[0]
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] != EMPTY:
            return board[0][j]
    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
        if board[1][1] != EMPTY:
            return board[1][1]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    for h in board:
        if EMPTY in h:
            return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def max_value(board):
    v = -math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    v = math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    move = {}
    for a in actions(board):
        if player(board) == X:
            move[min_value(result(board,a))] = a
        else:
            move[max_value(result(board,a))] = a
    return move[min(move.keys())] if player(board) == O else move[max(move.keys())]

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
    xcount = 0
    ocount = 0
    for i in board:
        for j in i:
            if j == X:
                xcount += 1
            if j == O:
                ocount += 1
    if ocount == 4 and xcount == 5:
        return 2
    elif (xcount == 0 and ocount == 0) or (xcount == ocount):
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_moves = []
    row = -1
    for i in board:
        cell = -1
        row += 1
        for j in i:
            cell += 1
            if j == EMPTY:
                possible_moves.append((row, cell))

    if len(possible_moves) == 0:
        return 2
    else:
        return possible_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    move = player(board)

    if move != 2:
        new_board = copy.deepcopy(board)
        if new_board[action[0]][action[1]] != EMPTY:
            raise Exception
        else:
            new_board[action[0]][action[1]] = move
        return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winning_set = [[(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)],
                   [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)],
                   [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]]

    for state in winning_set:
        xcount = 0
        ocount = 0
        for item in state:
            if board[item[0]][item[1]] == X:
                xcount += 1
            elif board[item[0]][item[1]] == O:
                ocount += 1
        if xcount == 3:
            return X
        elif ocount == 3:
            return O
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == None:
        if actions(board) != 2:
            return False
        else:
            return True
    else:
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    elif winner(board) == None:
        return 0

def maxValue(board):
    if terminal(board):
        return utility(board)

    v = float("-inf")
    for action in actions(board):
        v = max(v, minValue(result(board, action)))
    return v

def minValue(board):
    if terminal(board):
        return utility(board)

    v = float("inf")
    for action in actions(board):
        v = min(v, maxValue(result(board, action)))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    class bestMove():
        def __init__(self, action, currentRating, parentRating):
            self.action = action
            self.currentRating = currentRating
            self.parentRating = parentRating


    if player(board) == X:
        nextMove = bestMove(action = None, currentRating = None, parentRating = float("-inf"))
        for action in actions(board):
            nextMove.currentRating = minValue(result(board, action))
            if nextMove.currentRating > nextMove.parentRating:
                nextMove.action = action
                nextMove.parentRating = nextMove.currentRating
        return nextMove.action

    elif player(board) == O:
        nextMove = bestMove(action = None, currentRating = None, parentRating = float("inf"))
        for action in actions(board):
            nextMove.currentRating = maxValue(result(board, action))
            if nextMove.currentRating < nextMove.parentRating:
                nextMove.action = action
                nextMove.parentRating = nextMove.currentRating
        return nextMove.action


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
    countx = 0
    counto = 0

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == X:
                countx += 1
            if board[row][col] == O:
                counto += 1
    
    if countx > counto:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    allPossible = set()

    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == EMPTY:
                allPossible.add((row,col))

    return allPossible


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("error")
    else:
        row, col = action
        board_copy = copy.deepcopy(board)
        board_copy[row][col] = player(board)
        return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
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

    def checkDiagonal1(board, player):
        count = 0
        for row in range(len(board)):
            for col in range(len(board[row])):
                if row == col and board[row][col]:
                    count += 1
        if count == 3:
            return True
        else:
            return False
    
    def checkDiagonal2(board, player):
        count = 0
        for row in range(len(board)):
            for col in range(len(board[row])):
                if (len(board) - row - 1) == col and board[row][col]:
                    count += 1
        if count == 3:
            return True
        else:
            return False
    
    if checkRow(board, X) or checkCol(board, X) or checkDiagonal1(board, X) or checkDiagonal2(board, X):
        return X
    elif checkRow(board, O) or checkCol(board, O) or checkDiagonal1(board, O) or checkDiagonal2(board, O):
        return O
    else:
        return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    count = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == X or board[row][col] == O:
                count += 1
    
    if count == 9 or winner(board) == X or winner(board) == O:
        return True
    else:
        return False



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    else:
        return 0



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """    
    if terminal(board):
        return None
    
    def max_value(board):
        v = -math.inf
        if terminal(board):
            return utility(board)
        for action in actions(board):
            v = max(v, min_value(Result(board, action)))
        return v
    
    def min_value(board):
        v = math.inf
        if terminal(board):
            return utility(board)
        for action in actions(board):
            v = min(v, max_value(Result(board, action)))
        return v
    
    if player(board) == X:
        plays = []
        for action in actions(board):
            plays.append((min_value(result(board,action)), action ))
        return sorted(plays, key=lambda x: x[0], reverse=True)[0][1]
    
    if player(board) == O:
        plays = []
        for action in actions(board):
            plays.append((max_value(result(board,action)), action ))
        return sorted(plays, key=lambda x: x[0])[0][1]


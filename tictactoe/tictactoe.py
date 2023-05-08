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
    # create variables to store how many times each player has made a move
    x_player_moves = 0
    o_player_moves = 0
    # define the variables
    for row in range(len(board)):
        x_player_moves = x_player_moves + row.count(X)
        o_player_moves = o_player_moves + row.count(O)
    # decide and return whose turn it is
    if x_player_moves > o_player_moves:
        return O 
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # initialize a set for all possible moves
    possible_moves = set()
    # populate the set
    for row_index, row in enumerate(board):                      # for every row
        for column_index, item in enumerate(row):                # in every column
            if item == None:                                     # if the cell is empty
                possible_moves.add((row_index, column_index))    # add it to the set
    # return the set
    return possible_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # initialize variables
    player_move = player(board)
    new_board = deepcopy(board)
    # get the previous action
    i, j = action
    # check if the previous action is valid
    if board[i][j] != None:
        raise Exception
    else:
        new_board[i][j] = player_move
        return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # for each player
    for player in (X, O):
        # check if they won horizontally
            for i in range(3):
                column = [board[x][i] for x in range(3)]
                if column == [player] * 3:
                    return player
        # check if they won vertically
            for row in board:
                if row == [player] * 3:
                    return player

        
        # check if they won diagonally
            if [board[i][i] for i in range(0, 3)] == [player] * 3:
                return player
            elif [board[i][~i] for i in range(0, 3)] == [player] * 3:
                return player
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # check if there are still empty boxes
    for row in board:
        if EMPTY in row:
            return False
    # check if someone won the game
    if winner(board) == None:
        return False
    # otherwise 
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # if player x won
    if winner(board) == X:
        return 1
    # if player 0 won
    elif winner(board) == O:
        return -1
    # if nobody won
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # if at terminal state
    if terminal(board):
        return None

    def max_value(board):

        optimal_move = ()
        if terminal(board):
            return utility(board), optimal_move
        else:
            v = -5
            for action in actions(board):
                if min_value(result(board, action))[0] > v:
                    v = min_value(result(board, action))[0]
                    optimal_move = action
            return v, optimal_move

    def min_value(board):
        optimal_move = ()
        if terminal(board):
            return utility(board), optimal_move
        else:
            v = 5
            for action in actions(board):
                if max_value(result(board, action))[0] < v:
                    v = max_value(result(board, action))[0]
                    optimal_move = action
            return v, optimal_move

    if player(board) == X:
        return max_value(board)[1]

    else:
        return min_value(board)[1]

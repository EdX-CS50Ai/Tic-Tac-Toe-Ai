"""
Tic Tac Toe Player
"""

import math, copy

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
    # X has first move 
    if board == initial_state():
        return X

    if terminal(board):
        return None

    x_moves = 0
    o_moves = 0

    l = len(board[0])
    for i in range(l):
        for j in range(l):
            move = board[i][j]
            if move == X:
                x_moves += 1
            if move == O:
                o_moves += 1
    if x_moves <= o_moves:
        return X
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.append((i, j))

    return possible_actions

    if len(possible_actions) > 0:
        return possible_actions
    else:
        return None             


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    (i, j) = action
    new_board[i][j] = player(new_board)
    return new_board



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    l = len(board[0])
    
    # check horizontal wins
    for i in range(l):
        col = board[i]
        x_run = 0
        o_run = 0
        for move in col:
            if move == X:
                x_run += 1
            if move == O:
                o_run += 1
        if x_run == 3:
            return X
        if o_run == 3:
            return O        

    # check for vertical win
    col = 0
    x_run = 0
    o_run = 0
    for i in range(l):
        move = board[i][col]
        if move == X:
            x_run += 1
        if move == O:
            o_run += 1        
    if x_run == 3:
        return X
    if o_run == 3:
        return O        

    col = 1
    x_run = 0
    o_run = 0
    for i in range(l):
        move = board[i][col]
        if move == X:
            x_run += 1
        if move == O:
            o_run += 1
    if x_run == 3:
        return X
    if o_run == 3:
        return O        

    col = 2
    x_run = 0
    o_run = 0
    for i in range(l):
        move = board[i][col]        
        if move == X:
            x_run += 1
        if move == O:
            o_run += 1        
    if x_run == 3:
        return X
    if o_run == 3:
        return O        

    x_run = 0
    o_run = 0
    # descending cross check 
    for i in range(l):
        move = board[i][i]        
        if move == X:
            x_run += 1
        if move == O:
            o_run += 1
    if x_run == 3:
        return X
    if o_run == 3:
        return O        

    x_run = 0
    o_run = 0
    # ascending cross check
    for (i, j) in [(0, 2), (1, 1), (2, 0)]:
        move = board[i][j]        
        if move == X:
            x_run += 1
        if move == O:
            o_run += 1
    if x_run == 3:
        return X
    if o_run == 3:
        return O        

    return None            

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    no_more_moves = True
    l = len(board[0])
    for i in range(l):
        for j in range(l):
            if board[i][j] == EMPTY:
                no_more_moves = False

    if winner(board) or no_more_moves:
         return True
    
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    player = winner(board)
    if player == X:
        return 1
    elif player == O:
        return -1
    else:
        return 0 



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None

    possible_actions = actions(board)
    values = []

    for action in possible_actions:
        if player(board) == X:
            value = min_value(result(board=board, action=action))    
        else:
            value = max_value(result(board=board, action=action)) 

        values.append(value)

    if len(possible_actions) == 1:
        return possible_actions[0]

    optimal_action = possible_actions[0]
    optimal_value = values[0]

    for i in range(1, len(possible_actions)):
        if player(board) == X:  
            if values[i] > optimal_value:
                optimal_action = possible_actions[i]
                optimal_value = values[i]
                if optimal_value == 1:
                    return optimal_action


        if player(board) == O:  
            if values[i] < optimal_value:
                optimal_action = possible_actions[i]
                optimal_value = values[i]
                if optimal_value == -1:
                    return optimal_action

    return optimal_action

def max_value(board):
    v = -math.inf
    if terminal(board):
        return utility(board=board)
    
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
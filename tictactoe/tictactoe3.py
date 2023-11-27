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
    for i in board:
        x_count += i.count(X)
        o_count += i.count(O)
    if o_count < x_count:
        return O
    elif x_count == 0:
        return X
    else:
        return X

    #raise NotImplementedError

#print(initial_state())

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    result_set = set()
    for lines in range(len(board)):
        for elements in range(len(board[lines])):
            if board[lines][elements] == EMPTY:
                result_set.add((lines, elements))

    # print(result_set)
    return result_set


    #raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = [[], [], []]
    for i in range(len(board)):
        for el in board[i]:
            new_board[i].append(el)

    act_set = actions(board)
    if action in act_set:
        new_board[action[0]][action[1]] = player(board)
    # print(f'board{board},new_board{new_board}')
    return new_board


    #raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for lines in board:
        if (board[0][0] == board[1][1] == board[2][2] == X) or (board[0][2] == board[1][1] == board[2][0] == X) or (board[0][2] == board[1][2] == board[2][2] == X) or (board[0][0] == board[1][0] == board[2][0] == X) or (board[0][1] == board[1][1] == board[2][1] == X) or (board[1][0] == board[1][1] == board[1][2] == X) or (board[2][0] == board[2][1] == board[2][2] == X) or (board[0][0] == board[0][1] == board[0][2] == X):
            return X
        elif (board[0][0] == board[1][1] == board[2][2] == O) or (board[0][2] == board[1][1] == board[2][0] == O) or (board[0][2] == board[1][2] == board[2][2] == O) or (board[0][0] == board[1][0] == board[2][0] == O) or (board[0][1] == board[1][1] == board[2][1] == O) or (board[1][0] == board[1][1] == board[1][2] == O) or (board[2][0] == board[2][1] == board[2][2] == O) or (board[0][0] == board[0][1] == board[0][2] == O):
            return O
        else:
            return None


    #raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    Winner1 = winner(board)
    # print(Winner1, board)
    if Winner1 is not None or len(actions(board)) == 0:
        return True
    return False
    #raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    c = 0
    win = winner(board)

    # print(terminal(board))
    if terminal(board):
        if win == X:
            c = 1
        elif win == O:
            c = -1
        return c

    #raise NotImplementedError


def minimax(board):
    print(winner(board))



    def max_value(state):
        # summa = 0
        v = -1000
        if terminal(state):
            return utility(state)

        for action in actions(state):
            return max(v, min_value(result(state, action)))
            # summa += min_value(result(state, action))
            # print(f"min sum {summa}")
            # return summa
        # return v

    def min_value(state):
        # summa = 0
        v = 1000
        if terminal(state):
            return utility(state)

        for action in actions(state):
            return min(v, max_value(result(state, action)))

            # print(f"min sum {summa}")
            # return summa
        # return v

    act_set = actions(board)
    player_now = player(board)
    res_list = []
    action_list = []
    board_list = []
    target_action = None
    target = min_value(board) if player_now == X else max_value(board)
    # target_value = -1    000000 if player_now == X else 1000000

    for action in act_set:
        action_list.append(action)

    for action in act_set:
        next_board = result(board, action)
        board_list.append(next_board)
        action_list.append(action)
        # board_list.append(new_board)
    for state in board_list:
        if player_now == X:
            res_list.append(min_value(state))
        else:
            res_list.append(max_value(state))

    target_action = action_list[res_list.index(target)]

    target_action = action_list[res_list.index(target)]
        # print(f"player_now{player_now}")
        # if player_now is None:
        #     break
        #
    return target_action




        # if player_now == X:
        #     # print("min_value")
        #     # cur_value = max_value(next_board)
        #     # print(f'action{action},cur_value{cur_value}')
        #     # if cur_value > target_value:
        #     #     target_value = cur_value
        #     #     target_action = action
        #     win_cond, tie_cond, loose_cond = max_value(next_board) if player_now == X else min_value(next_board)
        #     print(f'action{action},win_cond{win_cond}, tie_cond{tie_cond}, loose {loose_cond}')
        #     win_share = win_cond / (win_cond + tie_cond + loose_cond)
        #     loose_share = loose_cond / (win_cond + tie_cond + loose_cond)
        #     if win_share > loose_share and win_share > win_value:
        #         win_value = win_share
        #         target_action = action
        #     elif win_share == win_value and tie_cond > tie_value:
        #         tie_value = tie_cond
        #         target_action = action
        # if player_now == O:
        #     # print("min_value")
        #     # cur_value = min_value(next_board)
        #     # print(f'action{action},cur_value{cur_value}')
        #     # if cur_value < target_value:
        #     #     target_value = cur_value
        #     #     target_action = action
        #     win_cond, tie_cond, loose_cond = min_value(next_board)
        #     print(f'action{action},win_cond{win_cond}, tie_cond{tie_cond}, loose {loose_cond}')
        #     win_share = win_cond / (win_cond + tie_cond + loose_cond)
        #     loose_share = loose_cond / (win_cond + tie_cond + loose_cond)
        #     if win_share > loose_share and win_share > win_value:
        #         win_value = win_share
        #         target_action = action
        #     elif win_share == win_value and tie_cond > tie_value:
        #         tie_value = tie_cond
        #         target_action = action

    # return target_action


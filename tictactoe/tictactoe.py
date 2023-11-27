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
        # print(winner(state))
        # summa = 0
        win_cond = 0
        tie_cond = 0
        loose_cond = 0

        if terminal(state):
            # return utility(state)
            ut = utility(state)
            if ut == 1:
                win_cond += 1
            elif ut == 0:
                tie_cond += 1
            else:
                loose_cond += 1
        else:
            for action in actions(state):
                # mv = min_value(result(state, action))/2
                # summa += min(mv, 1)
                # if mv == 0:
                    # summa += 0.25
                (win, tie, loose) = min_value(result(state, action))
                win_cond += loose
                tie_cond += tie
                loose_cond += win
                if win == 1 and tie == 0 and loose == 0:
                    return loose, tie, win
            # print(f"min sum {summa}")
            # return summa
        return win_cond, tie_cond, loose_cond

    def min_value(state):
        win_cond = 0
        tie_cond = 0
        loose_cond = 0

        if terminal(state):
            # return utility(state)
            ut = utility(state)
            if ut == -1:
                win_cond += 1
            elif ut == 0:
                tie_cond += 1
            else:
                loose_cond += 1
        else:
            for action in actions(state):
                # mv = min_value(result(state, action))/2
                # summa += min(mv, 1)
                # if mv == 0:
                    # summa += 0.25
                (win, tie, loose) = max_value(result(state, action))
                win_cond += loose
                tie_cond += tie
                loose_cond += win
                if win == 1 and tie == 0 and loose == 0:
                    return loose, tie, win
            # print(f"min sum {summa}")
            # return summa
        return win_cond, tie_cond, loose_cond
        # if terminal(state):
        #     return utility(state)
        # summa = 0
        # for action in actions(state):
        #     mv = max_value(result(state, action))/2
        #     summa += max(-1, mv)
        #     if mv == 0:
        #         summa -= 0.25
        #     # print(f"{action} max v {v} r {res}")
        # print(f"max sum {summa}")
        # return summa

    act_set = actions(board)
    player_now = player(board)

    action_list = []


    # target_value = -1000000 if player_now == X else 1000000

    for action in act_set:
        action_list.append(action)

    target_action = action_list[0]

    win_value = 0
    loose_value = 10000000

    if (len(act_set) == 9):
        return 0, 0

    for action in act_set:
        next_board = result(board, action)
        # board_list.append(new_board)

        # print(f"player_now{player_now}")
        # if player_now is None:
        #     break
        #
        win_cond, tie_cond, loose_cond = max_value(next_board) if player_now == X else min_value(next_board)
        win_share = win_cond / (win_cond + tie_cond + loose_cond)
        loose_share = loose_cond / (win_cond + tie_cond + loose_cond)
        print(f'action{action},win_cond{win_cond}, win_share{win_share}, loose_share{loose_share} tie_cond{tie_cond}, loose {loose_cond}')
        # if win_share == 1:
        #     return action
        if loose_cond == 0:
            return action
        if win_share >= loose_share and win_share >= win_value:
            print(f"set win_share{win_share}")
            win_value = win_share
            target_action = action
        # elif win_share == win_value and tie_cond > tie_value:
        #     tie_value = tie_cond
        #     target_action = action
        elif win_share < loose_share < loose_value:
            print(f"set loose_share{loose_share}")
            loose_value = loose_share
            target_action = action

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

    return target_action


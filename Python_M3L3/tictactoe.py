import random

WIN_CONDITIONS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6),
]


def check_winner(board, symbol):
    return any(board[a] == board[b] == board[c] == symbol for a, b, c in WIN_CONDITIONS)


def get_available_moves(board):
    return [i for i in range(9) if board[i] not in ("X", "O")]


def minimax(board, depth, is_maximizing, comp_symbol, p1_symbol):
    if check_winner(board, comp_symbol):
        return 10 - depth
    if check_winner(board, p1_symbol):
        return depth - 10

    available = get_available_moves(board)
    if not available:
        return 0

    if is_maximizing:
        best_score = -100
        for move in available:
            original = board[move]
            board[move] = comp_symbol
            score = minimax(board, depth + 1, False, comp_symbol, p1_symbol)
            board[move] = original
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = 100
        for move in available:
            original = board[move]
            board[move] = p1_symbol
            score = minimax(board, depth + 1, True, comp_symbol, p1_symbol)
            board[move] = original
            best_score = min(best_score, score)
        return best_score


def computer_move(board, comp_symbol, p1_symbol):
    available = get_available_moves(board)
    if len(available) == 9:
        return random.choice([0, 2, 4, 6, 8])

    best_score = -100
    best_moves = []

    for move in available:
        original = board[move]
        board[move] = comp_symbol
        score = minimax(board, 0, False, comp_symbol, p1_symbol)
        board[move] = original

        if score > best_score:
            best_score = score
            best_moves = [move]
        elif score == best_score:
            best_moves.append(move)

    return random.choice(best_moves)


def player_choice():
    symbol = ""
    while symbol not in ("X", "O"):
        symbol = input("Do you want to be X or O? ").upper()
    return ("X", "O") if symbol == "X" else ("O", "X")


def player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if move in range(1, 10) and board[move - 1] not in ("X", "O"):
                return move - 1
        except ValueError:
            pass


def print_board(board):
    print("\n" * 2)
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")


def play_game():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    p1_symbol, comp_symbol = player_choice()
    current_turn = "Player" if p1_symbol == "X" else "Computer"
    moves_played = 0

    while True:
        print_board(board)

        if current_turn == "Player":
            print("Your Turn")
            move_index = player_move(board)
            active_symbol = p1_symbol
        else:
            print("Computer's Turn")
            move_index = computer_move(board, comp_symbol, p1_symbol)
            active_symbol = comp_symbol

        board[move_index] = active_symbol
        moves_played += 1

        if check_winner(board, active_symbol):
            print_board(board)
            if current_turn == "Player":
                print("You Win the match!")
            else:
                print("Computer Wins the match!")
            break

        if moves_played == 9:
            print_board(board)
            print("It's a draw! Board is full.")
            break

        current_turn = "Computer" if current_turn == "Player" else "Player"


if __name__ == "__main__":
    play_game()

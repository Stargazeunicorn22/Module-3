def player_choice():
    symbol = ''
    while symbol not in ['X', 'O']:
        symbol = input("Do you want to be X or O? ").upper()
    if symbol == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if move in range(1, 10) and board[move - 1] not in ['X', 'O']:
                return move - 1
        except ValueError:
            pass

def computer_move(board):
    available_moves = [i for i in range(9) if board[i] not in ['X', 'O']]
    return __import__('random').choice(available_moves)

def play_game():
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    p1_symbol, comp_symbol = player_choice()
    
    current_turn = "Player" if p1_symbol == "X" else "Computer"
    moves_played = 0

    while True:
        print("\n" * 2)
        print(f"   {board[0]} | {board[1]} | {board[2]} ")
        print("  ---|---|---")
        print(f"   {board[3]} | {board[4]} | {board[5]} ")
        print("  ---|---|---")
        print(f"   {board[6]} | {board[7]} | {board[8]} ")
        print("\n")

        if current_turn == "Player":
            print("Your Turn")
            move_index = player_move(board)
            active_symbol = p1_symbol
        else:
            print("Computer's Turn")
            move_index = computer_move(board)
            active_symbol = comp_symbol
        
        board[move_index] = active_symbol
        moves_played += 1

        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  
            (0, 4, 8), (2, 4, 6)              
        ]
        
        is_winner = False
        for a, b, c in win_conditions:
            if board[a] == board[b] == board[c] == active_symbol:
                is_winner = True
                break

        if is_winner:
            print("\n" * 2)
            print(f"   {board[0]} | {board[1]} | {board[2]} ")
            print("  ---|---|---")
            print(f"   {board[3]} | {board[4]} | {board[5]} ")
            print("  ---|---|---")
            print(f"   {board[6]} | {board[7]} | {board[8]} ")
            print("\n")
            if current_turn == "Player":
                print("You Win the match!")
            else:
                print("Computer Wins the match!")
            break

        if moves_played == 9:
            print("\n" * 2)
            print(f"   {board[0]} | {board[1]} | {board[2]} ")
            print("  ---|---|---")
            print(f"   {board[3]} | {board[4]} | {board[5]} ")
            print("  ---|---|---")
            print(f"   {board[6]} | {board[7]} | {board[8]} ")
            print("\n")
            print("It's a draw! Board is full.")
            break

        current_turn = "Computer" if current_turn == "Player" else "Player"

if __name__ == "__main__":
    play_game()

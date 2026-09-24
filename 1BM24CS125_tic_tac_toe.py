import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("---------")

def check_win(board, player):

    for row in board:
        if all([s == player for s in row]):
            return True

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def get_empty_cells(board):
    empty_cells = []
    for r in range(3):
        for c in range(3):
            if board[r][c] == ' ':
                empty_cells.append((r, c))
    return empty_cells

def computer_move(board):
    empty_cells = get_empty_cells(board)
    if empty_cells:
        return random.choice(empty_cells)
    return None

def is_board_full(board):
    return not get_empty_cells(board)

def play_game():
    print("Kaamil Hifzaan P S 1BM24CS125")
    0
    
    board = [[' ' for _ in range(3)] for _ in range(3)]
    human_player = 'X'
    computer_player = 'O'
    current_turn = human_player

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        if current_turn == human_player:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
                if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == ' ':
                    board[row][col] = human_player
                else:
                    print("Invalid move. Try again.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
        else:
            print("Computer's turn...")
            move = computer_move(board)
            if move:
                board[move[0]][move[1]] = computer_player
            else:
                print("No more moves for the computer. It's a draw!")
                break

        print_board(board)

        if check_win(board, current_turn):
            print(f"{current_turn} wins!")
            break
        elif is_board_full(board):
            print("It's a draw!")
            break

        current_turn = computer_player if current_turn == human_player else human_player

play_game()

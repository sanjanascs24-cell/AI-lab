# Tic-Tac-Toe Game

board = [" " for _ in range(9)]


def display_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def check_winner(player):
    winning_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c] == player:
            return True

    return False


current_player = "X"

for turn in range(9):
    display_board()

    while True:
        try:
            position = int(input(
                f"Player {current_player}, enter position (1-9): "
            ))

            if position < 1 or position > 9:
                print("Enter a number between 1 and 9.")
            elif board[position - 1] != " ":
                print("Position already taken.")
            else:
                break

        except ValueError:
            print("Enter a valid number.")

    board[position - 1] = current_player

    if check_winner(current_player):
        display_board()
        print(f"Player {current_player} wins!")
        break

    current_player = "O" if current_player == "X" else "X"

else:
    display_board()
    print("It's a draw!")
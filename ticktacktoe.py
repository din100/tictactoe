# Define the game board
board = [' ' for _ in range(9)]

# Function to print the game board
def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

# Function to check for a win or a draw
def check_win(player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
                      (0, 3, 6), (1, 4, 7), (2, 5, 8), 
                      (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def check_draw():
    return ' ' not in board

# Function to handle player moves
def player_move(player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if board[move] == ' ':
                board[move] = player
                break
            else:
                print("This position is already taken.")
        except (IndexError, ValueError):
            print("Invalid move. Please enter a number between 1 and 9.")

# Main game loop
def main():
    current_player = 'X'
    while True:
        print_board()
        player_move(current_player)
        if check_win(current_player):
            print_board()
            print(f"Player {current_player} wins!")
            break
        if check_draw():
            print_board()
            print("It's a draw!")
            break
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()
# Q2) 🎮 Game Rules:
# The first input is an integer T, the number of times the game will be played.

# For each game:
# Read an integer r, the number of rows in a matrix. The number of columns is fixed at 3.

# Then, read the next r x 3 integers as elements of the matrix.

# Players take turns filling/playing the cells. Fiet always starts first.

# The player who makes the last move wins the game.

# ⌨️ Input Format:
# T
# r
# r x 3 integers
# (repeat for T games)
# T → Number of games

# r → Number of rows (for each game)

# r x 3 integers → Matrix elements for that game

# 🖨️ Output:
# Print the name of the winner for each game:

# Example Input:

# 2
# 2
# 1 2 3
# 4 5 6
# 3
# 7 8 9
# 10 11 12
# 13 14 15

# Function to determine the winner
def find_winner(total_moves):
    # If total number of moves is odd, Fiet plays last
    return "Fiet" if total_moves % 2 == 1 else "Opponent"

# Read number of games
T = int(input())

# Loop over each game
for _ in range(T):
    r = int(input())  # number of rows
    matrix_elements = []

    # Read r x 3 elements (since number of columns is fixed at 3)
    for _ in range(r):
        row = list(map(int, input().split()))
        matrix_elements.extend(row)

    total_moves = len(matrix_elements)  # Total number of cells to be played
    winner = find_winner(total_moves)
    print(winner)

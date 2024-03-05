import numpy as np

# Initialize the game board
def init_board():
    return [' '] * 10

# Display the game board
def display_board(board):
    print("\nGame Board")
    for row in range(1, 4):
        game_row = ' ' + ' | '.join(board[row*3-2:row*3+1]) + ' '
        print(game_row)
        if row != 3:
            print('-----------')

# Determine if a space on the board is free
def space_check(board, position):
    return board[position] == ' '

# Check for a win
def win_check(board, mark):
    return ((board[1] == board[2] == board[3] == mark) or
            (board[4] == board[5] == board[6] == mark) or
            (board[7] == board[8] == board[9] == mark) or
            (board[1] == board[4] == board[7] == mark) or
            (board[2] == board[5] == board[8] == mark) or
            (board[3] == board[6] == board[9] == mark) or
            (board[1] == board[5] == board[9] == mark) or
            (board[3] == board[5] == board[7] == mark))

# Get a list of empty spaces on the board
def available_moves(board):
    return [i for i, spot in enumerate(board) if spot == ' ' and i != 0]

# Minimax algorithm
def minimax(board, depth, isMaximizing, alpha, beta, ai_choice, player_choice):
    if win_check(board, ai_choice):
        return 10
    elif win_check(board, player_choice):
        return -10
    elif len(available_moves(board)) == 0:
        return 0

    if isMaximizing:
        bestScore = -np.inf
        for move in available_moves(board):
            board[move] = ai_choice
            score = minimax(board, depth + 1, False, alpha, beta, ai_choice, player_choice)
            board[move] = ' '

            bestScore = max(score, bestScore)
            alpha = max(alpha, score)
            if beta <= alpha:
                break
        return bestScore
    else:
        bestScore = np.inf
        for move in available_moves(board):
            board[move] = player_choice
            score = minimax(board, depth + 1, True, alpha, beta, ai_choice, player_choice)
            board[move] = ' '

            bestScore = min(score, bestScore)
            beta = min(beta, score)
            if beta <= alpha:
                break
        return bestScore

# AI makes a move using the minimax algorithm
def ai_move(board, ai_choice, player_choice):
    bestScore = -np.inf
    bestMove = 0
    for move in available_moves(board):
        board[move] = ai_choice
        score = minimax(board, 0,  False, -np.inf, np.inf, ai_choice, player_choice)
        board[move] = ' '
        if score > bestScore:
            bestScore = score
            bestMove = move
    return bestMove

# Check if the board is full
def full_board_check(board):
    return ' ' not in board[1:]

# Player's move
def player_move(board, player_choice):
    position = 0
    while position not in range(1, 10) or not space_check(board, position):
        try:
            position = int(input("Choose your position (1-9): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1-9.")
    board[position] = player_choice

def choice(player_name):
    player_choice = ''
    while player_choice not in ['X', 'O']:
        player_choice = input(f"{player_name}, do you want to be X or O? ").upper()
        if player_choice not in ['X', 'O']:
            print("Invalid input. Please choose X or O.")
    ai_choice = 'O' if player_choice == 'X' else 'X'
    return player_choice, ai_choice

# Main game loop
def play_tic_tac_toe():
    print("Welcome to Tic-Tac-Toe!")
    player_name = input("Enter your name: ")
    player_choice = choice(player_name)[0]
    ai_choice = 'O' if player_choice == 'X' else 'X'



    while True:
        theBoard = init_board()
        game_on = True
        turn = 'Player'

        while game_on:
            if turn == 'Player':
                display_board(theBoard)
                player_move(theBoard, player_choice)
                if win_check(theBoard, player_choice):
                    display_board(theBoard)
                    print(f"Congratulations {player_name}! You have won the game!")
                    game_on = False
                else:
                    if full_board_check(theBoard):
                        display_board(theBoard)
                        print("The game is a draw!")
                        break
                    else:
                        turn = 'AI'

            else:
                move = ai_move(theBoard, ai_choice, player_choice)
                theBoard[move] = ai_choice
                if win_check(theBoard, ai_choice):
                    display_board(theBoard)
                    print("AI has won! Better luck next time.")
                    game_on = False
                else:
                    if full_board_check(theBoard):
                        display_board(theBoard)
                        print("The game is a draw!")
                        break
                    else:
                        turn = 'Player'




play_tic_tac_toe()

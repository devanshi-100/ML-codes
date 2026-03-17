import numpy 
import math
import random

board=numpy.array([['-','-','-'],['-','-','-'],['-','-','-']]) # 3.1 Initialize the board with empty places

ps1='X' # 3.2 Symbol for Player 1
ps2='O' # 3.3 Symbol for Player 2 or AI


def check_row(symbol):
    for r in range(3): # 4.1a Check all three rows
        count=0 # 4.1a.2 Initialize counter to 0
        for c in range(3): # 4.1a.3 Iterate through all the cols
            if board[r][c] == symbol: # 4.1a.4 Check if the symbol matches
                count += 1 # 4.1a.5 Increment counter
        if count == 3: # 4.1a.6 If counter is 3, it's a winning move
            return True # 4.1a.7 Return True if player has won
    return False # 4.1a.8 Return False otherwise

def check_col(symbol):
    for c in range(3): # 4.1b Check all three cols
        count = 0 
        for r in range(3): 
            if board[r][c] == symbol:
                count += 1 # 4.1b.5 Increment counter
        if count == 3: # 4.1b.6 If counter is 3, it's a winning move
            return True # 4.1b.7 Return True if player has won
    return False # 4.1b.8 Return False otherwise

def check_diagonal(symbol):
    if board[0][2] == board[1][1] == board[2][0] == symbol: # 4.1c.1 Check first diagonal
        return True # 4.1c.2 Return True if player has won
    if board[0][0] == board[1][1] == board[2][2] == symbol: # 4.1c.3 Check second diagonal
        return True # 4.1c.4 Return True if player has won
    return False # 4.1c.5 Return False otherwise

def goal_test(symbol):
    return check_row(symbol) or check_col(symbol) or check_diagonal(symbol)
# 4. Check if the move is a winning move
# Winning move can be either three consecutive rows, cols, or any diagonal

def is_draw():
    for r in range(3):
        for c in range(3):
            if board[r][c] == '-':
                return False
    return True

def minmax(is_maximum):
    if goal_test(ps1):
        return -1
    elif goal_test(ps2):
        return 1
    elif is_draw():
        return 0
    
    
    if is_maximum:
        best_score= -math.inf
        for r in range(3):
            for c in range(3):
                if board[r][c] == '-':
                    board[r][c]=ps2
                    score=minmax(False)
                    board[r][c]='-'
                    best_score=max(score,best_score)
        return best_score
    else:
        best_score=math.inf
        for r in range(3):
            for c in range(3):
                if board[r][c]=='-':
                    board[r][c]=ps1
                    score=minmax(True)
                    board[r][c]='-'
                    best_score=min(score,best_score)
        return best_score
    
    
def best_move(mode):
    global board

    if mode == "easy":
        # Choose random move
        empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == '-']
        return random.choice(empty_cells)

    elif mode == "medium":
        # 50% chance random, 50% minimax
        if random.random() < 0.5:
            empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == '-']
            return random.choice(empty_cells)
        else:
            # use minimax (same as hard)
            best_score = -math.inf
            move = None
            for r in range(3):
                for c in range(3):
                    if board[r][c] == '-':
                        board[r][c] = ps2
                        score = minmax(False)
                        board[r][c] = '-'
                        if score > best_score:
                            best_score = score
                            move = (r, c)
            return move
    else:  # hard
        # pure minimax
        best_score = -math.inf
        move = None
        for r in range(3):
            for c in range(3):
                if board[r][c] == '-':
                    board[r][c] = ps2
                    score = minmax(False)
                    board[r][c] = '-'
                    if score > best_score:
                        best_score = score
                        move = (r, c)
        return move


def place(symbol):
    print(numpy.matrix(board)) # 3.5 Print the board
    while True: # 3.6 Take input until the inputs are correct
        row = int(input('Enter row - 1 or 2 or 3: ')) # 3.7 Take row input
        col = int(input('Enter Column - 1 or 2 or 3: ')) # 3.8 Take col input

        if row > 0 and row < 4 and col > 0 and col < 4 and board[row-1][col-1] == '-': # 3.9 Check if the input is valid
            break # 3.10 If everything is correct then break the loop
        else: # 3.11 Otherwise ask user to input again 
            if row == 9 or col == 9:
                return
            print("Invalid Input please enter again...")
    board[row-1][col-1] = symbol # 3.12 Place the symbol at the desired place
    print(numpy.matrix(board)) # 3.13 Print the board with the placed symbol

def play_ai(mode):
    for tun in range(9):
        if tun%2==0:
            print('X turn')
            place(ps1)
            if goal_test(ps1):
                print(ps1, 'won!')
                break
        else:
            print("AI is making a move::")
            ai_move=best_move(mode)
            r,c=ai_move
            board[r][c]=ps2
            if goal_test(ps2):
                print(numpy.matrix(board))
                print(ps2, 'AI won!')
                break
        if is_draw():
            print('Draw')
            break
        

if __name__ == "__main__":
    print("You are playing Tic Tac Toe against AI!")
    mode = input("enter the mode easy or medium or hard : ")
    play_ai(mode)

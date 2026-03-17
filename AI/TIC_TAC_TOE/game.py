import numpy

board=numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])  #this is my tic tak toe Board

ps1='X'
ps2='O'

def row_check(symbol):
    for r in range(3):
        count=0
        for c in range(3):
            if board[r][c]==symbol:
                count=count+1
            if count==3:
                return True
    return False

   
def col_check(symbol):
    for r in range(3):
        count=0
        for c in range(3):
            if board[c][r]==symbol:
                count=count+1
            if count==3:
                return True
    return False


def dig_check(symbol):
    if board[0][0] ==symbol and board[1][1]==symbol and board[2][2]==symbol:
        return True
    if board[0][2]==symbol and board[1][1]==symbol and board[2][0]==symbol:
        return True
    return False

def play():
    for turn in range(9):
        if turn%2==0:
            print("X turn")
            symbol=ps1
            print(numpy.matrix(board))
            while(1):
                row=int(input("Enter teh row - from 1 to 3: "))
                col=int(input("Enter teh column - from 1 to 3: "))

                if row>=1 and row<=3 and col>=1 and col<=3 and board[row-1][col-1]=='-':
                    break
                else:
                    print("Enter the value of the row and col in range 1-3 and check for empty cell")
        else:
            print("O turn")
            symbol=ps2
            print(numpy.matrix(board))
            while(1):
                row=int(input("Enter teh row - from 1 to 3: "))
                col=int(input("Enter teh column - from 1 to 3: "))

                if row>=1 and row<=3 and col>=1 and col<=3 and board[row-1][col-1]=='-':
                    break
                else:
                    print("Enter the value of the row and col in range 1-3 and check for empty cell")
        board[row-1][col-1]=symbol
        if row_check(symbol) or col_check(symbol) or dig_check(symbol):
            print(symbol,"won")
            return
        print(numpy.matrix(board))
    print("DRAW")
        






# this is the Driver of thet tic-tc-toe Game

if __name__=="__main__":
    play()

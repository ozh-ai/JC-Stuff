#Task 4.2
def displayBoard(board):
    for i in range(4):
        for j in range(4):
            print(board[i][j],end=' ')
        print('')

#Task 4.3
def getPlayerMove(board,player):
    row = int(input("Enter row (1-4):"))
    col = int(input("Enter column (1-4):"))
    if col<=4 and col>=1 and row<=4 and row>=1: #valid input
        if board[row-1][col-1]=='.':
            board[row-1][col-1] = player
            return True
        else:
            print("Space is already occupied")
            return False
    else:
        print("Invalid input")
        return False

#Task 4.4
def checkWin(board):
    global winner
    for i in range(4): #Check row
        if '.' not in board[i]:
            potentialwinner = board[i][0]
            checklist = ['T']
            checklist.append(potentialwinner)
            if (board[i][1] in checklist) and (board[i][2] in checklist) and (board[i][3] in checklist):
                winner = potentialwinner
                return True
    for i in range(4): #Check column
        if board[0][i]!='.' and board[1][i]!='.' and board[2][i]!='.' and board[3][i]!='.':
            potentialwinner = board[0][i]
            checklist = ['T']
            checklist.append(potentialwinner)
            if (board[1][i] in checklist) and (board[2][i] in checklist) and (board[3][i] in checklist):
                winner = potentialwinner
                return True

    potentialwinner = board[0][0] #diagonal
    win = True
    for i in range(4):
        if board[i][i] not in ['T',potentialwinner]:
            win = False
    if win==True:
        winner = potentialwinner
        return True

    draw = True #check for draw
    for i in range(4): 
        if '.' in board[i]:
            draw = False
            
    if draw==True:
        return True
    else:
        return False

#Task 4.5
def main(board):
    global winner
    global draw
    displayBoard(board)
    win = False
    while win==False:
        print("X turn:")
        moved = False #X turn
        while moved==False:
            moved = getPlayerMove(board,'X')
        displayBoard(board)
        win = checkWin(board)
        if win==True:
            break

        print("O turn:")
        moved = False #O turn
        while moved==False:
            moved = getPlayerMove(board,'O')
        displayBoard(board)
        win = checkWin(board)
        
    if draw==False:
        print(winner,"has won the game!")
    else:
        print("The game ends in a draw.")



#Task 4.1
board = [['.','.','.','.'],['.','.','.','.'],['.','.','.','.'],['.','.','.','.']]
import random
num1 = random.randint(1,4)
num2 = random.randint(1,4)
board[num1-1][num2-1] = 'T'

main(board)





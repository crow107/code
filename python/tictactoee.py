from os import _exit
import random

def Gamelayout():
    global row
    row = [] 
    for i in range(3):
        row.append(" ")
        for j in range(2):
            row.append(" ")
Gamelayout()
def Gameboard():
    global row
    print( '  '+row[0] +'  |  '+row[1]+'  |  ' +row[2]+'     '     "     1  |  2  |  3 ") 
    print("- - -+- - -+- - -"  "      - - -+- - -+- - -")
    print( '  '+row[3] +'  |  '+row[4]+'  |  ' +row[5]+'     '     "     4  |  5  |  6")
    print("- - -+- - -+- - -"  "      - - -+- - -+- - -")
    print( '  '+row[6] +'  |  '+row[7]+'  |  ' +row[8]+'     '     "     7  |  8  |  9 ")
    
Gameboard()


def Insert_Value(Value_player,Value_computer):
    if Value_player == 0:
        if Value_computer == 1:
            row[0]='O'
        elif Value_computer == 2:
            row[1]='O'
        elif Value_computer == 3:
            row[2]='O'
        elif Value_computer == 4:
            row[3]='O'
        elif Value_computer == 5:
            row[4]='O'
        elif Value_computer == 6:
            row[5]='O'
        elif Value_computer == 7:
            row[6]='O'
        elif Value_computer == 8:
            row[7]='O'
        elif Value_computer == 9:
            row[8]='O'
    elif Value_computer == 0:
        if Value_player == 1:
            row[0]='X'
        elif Value_player == 2:
            row[1]='X'
        elif Value_player == 3:
            row[2]='X'
        elif Value_player == 4:
            row[3]='X'
        elif Value_player == 5:
            row[4]='X'
        elif Value_player == 6:
            row[5]='X'
        elif Value_player == 7:
            row[6]='X'
        elif Value_player == 8:
            row[7]='X'
        elif Value_player == 9:
            row[8]='X'

moves = [1,2,3,4,5,6,7,8,9]

def player():
    Value_player1 = int(input("Enter the position : - "))
    moves.remove(Value_player1)
    Insert_Value(Value_player=Value_player1,Value_computer=0)

def computer():
    Value_computer1= random.choice(moves)
    moves.remove(Value_computer1)
    Insert_Value(Value_player=0,Value_computer=Value_computer1)

def result():
    global row
    # for O
    
    if row[0] == row[1] == row[2] == 'O':
        print("------------------------------------O win ------------------------------------------")
        return
    if row[3] == row[4] == row[5] == 'O':
        print("------------------------------------O win ------------------------------------------")
        return
    if row[6] == row[7] == row[8] == 'O':
        print("------------------------------------O win ------------------------------------------")
        return
    if row[0] == row[3] == row[6] == 'O':
        print("------------------------------------O win ------------------------------------------")
        return
    if row[1] == row[4] == row[7] == 'O':
        print("------------------------------------O win ------------------------------------------")
        return
    if row[2] == row[5] == row[8] == 'O':
        print("------------------------------------O win ------------------------------------------")
        return
    if row[0] == row[4] == row[8] == 'O':
        print("------------------------------------O win ------------------------------------------")
        return
    if row[2] == row[4] == row[6] == 'O':
        print("------------------------------------O win ------------------------------------------")
        return
    # for x 
    if row[0] == row[1] == row[2] == 'X':
        print("------------------------------------X win ------------------------------------------")
        return
    if row[3] == row[4] == row[5] == 'X':
        print("------------------------------------X win ------------------------------------------")
        return
    if row[6]== row[7] == row[8] == 'X':
        print("------------------------------------X win ------------------------------------------")
        return
    if row[0] == row[3] == row[6] == 'X':
        print("------------------------------------X win ------------------------------------------")
        return
    if row[1] == row[4] == row[7] == 'X':
        print("------------------------------------X win ------------------------------------------")
        return
    if row[2] == row[5] == row[8] == 'X':
        print("------------------------------------X win ------------------------------------------")
        return
    if row[0] == row[4] == row[8] == 'X':
        print("------------------------------------X win ------------------------------------------")
        return
    if row[2] == row[4] == row[6] == 'X':
    
        print("------------------------------------X win ------------------------------------------")
        return
    else:
         player()
         print("-------------------------------------")
         print("Your move")
         print("")
         Gameboard()
         print("-------------------------------------")
         print(" Computers move")
         print("")
         computer()
         Gameboard()   
         result()
         
result()
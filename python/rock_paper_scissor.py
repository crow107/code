import random
print("Rock Paper Scissors")
def Player():
    global P_Move
    Player_move = int(input("1 -> Rock \n2 -> Paper \n3 -> Scissors \nEnter Here:-"))
    if Player_move == 1 :
        P_Move = "Rock"
    elif Player_move==2:
        P_Move="Paper"
    elif Player_move == 3:
        P_Move = "Scissors"
    else:
        print("Enter the valid Option")
        Player()
Player()

def Computer():
    global C_move
    All_move= ["Rock","Paper","Scissors"]
    C_move = random.choice(All_move)
Computer()
print("Player   - ",P_Move)
print("Computer - ",C_move)

def result():
    global C_move
    global P_Move
    if C_move == "Rock" and P_Move == "Paper":
        print("----------------------------Player win------------------------------------------------")
    elif C_move == "Rock" and P_Move =="Scissors":
        print("----------------------------Computer win------------------------------------------------")
    elif C_move == "Paper" and P_Move == "Scissors":
        print("----------------------------Player win------------------------------------------------")
    elif C_move == "Paper" and P_Move == "Rock":
        print(" ----------------------------Computer win------------------------------------------------")
    elif C_move == "Scissors" and P_Move == "Rock":
        print("----------------------------Player win------------------------------------------------")
    elif C_move == "Scissors" and P_Move =="Paper":
        print("----------------------------Computer win------------------------------------------------")
result()
    
    
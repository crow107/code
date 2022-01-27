import random
print("                                TOSS")
def Player():
    global P_move
    P_move = int(input("1- Head \n2- Tail\nEnter here :-"))

def result():
    move = [1,2]
    A = random.choice(move)
    if P_move == A :
        print("----------------------You win the toss---------------------")
    else:
        print("----------------------You loss the toss-------------------")
a =1
while a<=5:
    Player()
    result()
    a = a + 1
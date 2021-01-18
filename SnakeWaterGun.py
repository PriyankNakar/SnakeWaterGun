import random
def game(comp,player):
    if comp==player:
        return None
    elif comp=='s':
        if player=='w':
            return False
        elif player=='g':
            return True
    elif comp=='w':
        if player=='s':
            return True
        elif player=='g':
            return False
    elif comp=='g':
        if player=='w':
            return False
        elif player=='s':
            return True


print("Computer Turn : Snake(s) Water(w) Or Gun(g)")
RandomNo = random.randint(1,3)
if RandomNo==1:
    comp ='s'
elif RandomNo==2:
    comp ='w'
else :
    comp ='g'

player = input("Your Turn : Snake(s) Water(w) Or Gun(g)  : ")
a=game(comp,player)
print(f"Computer Chose {comp}")
print(f"You Chose {player}")
if a== None:
    print("The Game Is Tie")
elif a== True:
    print("You Won The Game")
else:
    print("Your Lost The Game ")
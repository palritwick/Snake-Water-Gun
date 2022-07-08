import random

def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        if you == 'g':
            return True
    
    elif comp == 'w':
        if you == 'g':
            return False
        if you == 's':
            return True
    
    elif comp == 'g':
        if you == 's':
            return False
        if you == 'w':
            return True

comp = print("\nComputer's turn : Snake (s), Water(w) or gun(g)?")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
        comp = 'w'
elif randNo == 3:
        comp = 'g'

you = input("\nYour turn : Snake (s), Water(w) or gun(g)? ")

a = gameWin(comp, you)

print(f"Computer chose {comp}\n")
print(f"You chose {you}\n")

if a == None:
    print("THE GAME IS TIE !")
elif a:
    print("YOU WIN !")
else:
    print("YOU LOSE !")
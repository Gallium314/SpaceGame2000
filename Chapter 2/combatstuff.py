import time
import random
from coolprint import coolprint

def combat_stuff(enemy, lvl):
    dead = False
    deathmessage = ["You don't know how to feel.", "You feel empty.", "You feel triuphant.", "You feel disappointed.", "You feel indestructable.", "You feel sorry.", "You feel hungry.", "You feel horrified.", "You feel... changed.", "You do not feel."] 
    coolprint("Your enemy is " + enemy + ". (Health lvl " + str(lvl) + '.)', 0.5)
    coolprint("Press h to hit, press s to apologize")
    input("Press enter when ready.")
    for i in [3, 2, 1]:
        coolprint(i)
        time.sleep(1)
    coolprint("GO!")
    while dead == False:
        #good input function goes here
        hit = input()
        if hit == 'h':
            lvl -= 1
            coolprint(enemy + "'s health at " + str(lvl))
        elif hit == 's':
            coolprint("You say sorry, but it doesn't matter. He will die anyway.")
        if lvl == 0:
            dead = True
            coolprint("You have killed " + enemy + ". " + random.choice(deathmessage))
    return True

#TEST
namelist = ['Elephant', 'Frog', 'Tiger', 'Dragon', 'Dumbdumb', 'Cheeseface', 'Robot']
playAgain = 'y'
while playAgain == 'y':
    combat_stuff(random.choice(namelist), random.randint(1,15))
    playAgain = input('Play again? y/n')
coolprint("done")

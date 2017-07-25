#doin the intro first cuz im lazy
import random
import time
winstuff = ['acceptable', 'bad', 'excellent', 'exceptional', 'favorable', 'great', 'marvelous', 'positive', 'satisfactory', 'satisfying', 'superb', 'valuable', 'wonderful', 'ace', 'bully', 'capital', 'choice', 'crack', 'nice', 'pleasing', 'prime', 'rad', 'sound', 'spanking', 'sterling', 'super', 'superior', 'welcome', 'worthy', 'admirable', 'agreeable', 'commendable', 'congenial', 'deluxe', 'first-class', 'first-rate', 'gnarly', 'gratifying', 'honorable', 'neat', 'precious', 'recherché', 'reputable', 'select', 'shipshape', 'splendid', 'stupendous', 'super-eminent', 'super-excellent', 'tip-top', 'up to snuff']

def print_intro():
    intro = '''
=================
 space game 2000
=================

You are stranded on a planet will u die or surviv?

Go.'''
    return intro

#nice now that that's done time to make a game.

def getgudinputt():
    inp = input()
    return inp

print(print_intro())
print("your on an planet. Theres a farm nearby in a space station.")
print("press 1 to go in. press 2 to not (dont type anything else or u'll break the game.")
whatdo = int(getgudinputt())

whatdonum = int(whatdo)
if whatdonum == 1:
    print('nice')
elif whatdonum == 2:
    print('lol u suffacate and u ded')
    print('rip in peace')
    print('I don"t know how to stop the code or whatever so im gonna divide by zero bye.')
    input('press enter to explode code')
    codegoboom = 1/0

#here comes the tough stuff    
print("k now you're in the space station")
print("press 1 to farm. press 2 to eat. don't let ur hunger go above 4.")

food = 0
hunger = 0
win = 0
while hunger <= 4:
    farmeat = int(input())
    if farmeat == 1:
        food += 1
        hunger +=1
        print('hard work makes you need foods. You have ' + str(food) + ' foods, and ' + str(hunger) + ' hunger.')
    elif farmeat == 2:
        if food > 0:
            food -= 1
            hunger -=1
            print('nom. You have ' + str(food) + ' foods, and ' + str(hunger) + 'hunger.')
        else:
            print('you have no food. you can"t eat.')
    win += 1
    if win == 40:
        print("Yay you won!")
        print("magic")
        print("brilliant")
        print("terrific")
        for i in range(random.randint(20,30)):
            print(random.choice(winstuff))
            time.sleep(0.7)
        print("thank you for playing space game 2000")
        time.sleep(2)
        print("TO BE CONTINUUUED.")
        print("bye")
        time.sleep(2)
        codegoboom = 1/0
        
print("You didn't eat.")
print("You starveded")
print("rip in peace")
print('I don"t know how to stop the code or whatever so im gonna divide by 0')
input('press enter to explode code')
codegoboom = 1/0

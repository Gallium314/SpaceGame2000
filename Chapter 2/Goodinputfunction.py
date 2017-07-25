#inputoptions is a list of possible input e.g. ['1', '2', 'a', 'b']
#inventory is a boolean list of possible inventory (stick, flower): [True, False]

from chapter2 import coolprint

def good_input(inputoptions, inventory):
    goodinput = False
    newinventory = inventory #This for if you drop flower
    
    while not goodinput:
        inputchoice = input("What do you do?")
        
        if inputchoice == 'i':
            if inventory == [False, False]: #nothing
                coolprint("There's NOTHING there. Nothing at all.")
                print()
                
            elif inventory == [True, False]: #stick
                coolprint("All you have is a STICK and your cold dead heart.")
                print()
                
            elif inventory == [False, True]: #flower
                coolprint("You have a FLOWER. this makes you feel more human, but it's not enough.")
                print()

            elif inventory == [True, True]: #stick, flower
                coolprint("You realize that the combined weight of the FLOWER and the STICK you are carrying are too much to bear.")
                coolprint("(FLOWER dropped)")
                print()
                newinventory = [True, False]
                inventory = [True, False] #inventory is changed as well...
                #...so that if you check inventory again it will be displayed
                
                
                #flower is only dropped when you check inventory. This is good
                
            coolprint("With your new knowledge of what you own, you are ready to continue.")
            print()

            
        elif inputchoice in inputoptions:
            goodinput = True

        else:
            coolprint("You scream '" + inputchoice + "' at the sky. Nothing happens.")
            coolprint("Try again.")
            print()

    return inputchoice, newinventory

#TEST
#(very rough test)
stuff = [False, False]

coolprint("You come across a flower and a stick")
coolprint("Press 'f' to pick up flower. Press 's' to pick up stick. Press 'i' to check inventory.")
goodinputs = ['f', 's']
done = 'n'

while done == 'n':
    whatdo, stuff = good_input(goodinputs, stuff)
    if whatdo == 's':
        stuff[0] = True
        coolprint("stick picked up.")
        print()
    elif whatdo == 'f':
        stuff[1] = True
        coolprint("flower picked up.")
        print()
    done = input("Done? y/n")
coolprint("done")

#NOTES
#The whole 'Flower dropped' thing should mean that you can't pick up the flower again.
            

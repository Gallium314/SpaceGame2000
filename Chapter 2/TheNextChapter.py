import time
import random
from combatstuff import combat_stuff
from confetti import confettiprint

namelist = ['Elephant', 'Frog', 'Tiger', 'Dragon', 'Dumbdumb', 'Cheeseface', 'Robot']
strength=0

def coolprint(stringy, num=0.05, newline=True):
	for i in stringy:
		print(i, end='',flush = True)
		time.sleep(num)
	if newline:
		print('')

coolprint("You spend your days farming and eating")
coolprint("what a wasted existence. Let's add some much needed excitement")
time.sleep(2)
coolprint("Let's see.")
time.sleep(2)
coolprint("uhhh...")
time.sleep(1)
for i in range(3):
	coolprint(".",0.05,False)
	time.sleep(1)
coolprint("I've got it!")
coolprint("Let's fight!")
coolprint("duh, duh duh duh duh duh duh duh!")
coolprint("dum de dum duh duh duh!")
combat_stuff(random.choice(namelist), random.randint(1,15))
coolprint("You have gotten stronger, your strength increases by 1")
strength=strength+1
coolprint("You are now ready to go on an adventure, congratulations!")
confettiprint()
coolprint("Chapter 2")
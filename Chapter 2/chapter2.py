import time
#chapter2

def coolprint(string, delay):
	for i in string:
		print(i, end='', flush = True)
		time.sleep(delay)
	print("\n")

def getgudinput(text, valid, prompt):
	while(not valid(text)):
		text = input(prompt)

#intro
coolprint('How long has it been?', 0.1)
time.sleep(2)
coolprint('how long have I been farming...', 0.1)
time.sleep(3)
coolprint("too long. I've forgotten who I am...", 0.1)
time.sleep(2)
coolprint("I'm such a tortured soul...", 0.1)
time.sleep(0.5)
coolprint("I WILL EXPLORE", 0.1)
coolprint('\n\n\n\n\n',0.2)
#part1: the forest
coolprint('\"Part I: Weclome to the Forast!\"', end="", flush = True, 0)
time.sleep(5)
print('You stepped outside. Which way will you turn?')

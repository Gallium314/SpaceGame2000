import random
from TheNextChapter import coolprint

def confettiprint (lines=10):
    line = ""
    types = ["'", '"', ".", "`", "~", ",", "-", "*"," ", " ", " "]
    for i in range(lines):
        for i in range (10):
            confetti_type = random.randint(0,10)
            coolprint(types[confetti_type])
        print()

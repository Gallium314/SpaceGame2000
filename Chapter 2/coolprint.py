import time
def coolprint(string, delay=0.1):
    for i in string:
        print(i, end='', flush = True)
        time.sleep(delay)
    print('/n')
        

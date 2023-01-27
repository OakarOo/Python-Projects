import time

def numbercountr():
    global starting, ending
    starting = input("Starting number: ")
    ending = input("Ending number: ")
    delay = input("Delay between numbers in seconds: ")
    while int(starting) < int(ending):
        starting = int(starting) + 1
        print(starting)
        time.sleep(float(delay))
        
numbercountr()

    

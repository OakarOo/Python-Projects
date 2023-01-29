age = 0
get_name = input("What is your name? ")
get_age = input("What is your age. ")
if int(get_age) >= 18:
        print("Your name is "+ get_name +".You are " + str(get_age) + " years old! You are allowed to enter")
elif int(get_age) < 18:
        print("Your name is "+ get_name +".You are " + str(get_age) +" years old! You are NOT allowed to enter")
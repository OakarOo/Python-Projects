age = 0
get_name = input("What is your name? ")

if get_name.lower() != "ben":
        get_age = input("What is your age. ")
        if int(get_age) >= 18:
                print("Your name is "+ get_name +".You are " + str(get_age) + " years old! You are allowed to enter")
        elif int(get_age) < 18 :
                print("Your name is "+ get_name +".You are " + str(get_age) +" years old! You are NOT allowed to enter\nMinimum age = 18")
        
elif get_name.lower() == "ben":
        get_deed = input("How many good deeds have you done today? ")
        if int(get_deed) >= 4:
                print("Oh you are a GOOD Ben. Alright you can enter! ")
        else:
                print("Go away you evil Ben. We don't welcome you here! ")
                quit()



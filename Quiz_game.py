print("\nWelcome to my first computer quiz!\n ")
playing = input("If you get wrong answer '3' times you will fail!! \nDo you want to play? type ' yes ' or ' no '\n ")
hint_value = 0

def want_to_play():
    if playing.lower() != "yes":
        quitz = input("Ok maybe next time.\n Press ENTER to quit ")
        quitz = quit()

def asking():

    while playing.lower() == "yes":
        global hint_value
        global score
        score = 0
        answer = input("What does knife use for? \n")
        if answer.lower() == "cutting":
            score += 1
            print("\nIt is Correct! 1+ score!")
            break
        else:
            hint_value = hint_value + 1
            print("\nIt is Incorrect. Please try again :)\n")

            if hint_value == 2:
                print("HINT: It is an action. last chance! \n")
            elif hint_value == 3:
                print("\nWrong ANSWER!! :(\nThe correct Answer is ' cutting '")
                hint_value = 0
                break


    while True:
        answer = input("What does sword use for? \n")
        if answer.lower() == "fighting":
            score += 1
            print("\nIt is Correct! 1+ score!")
            break       
        else:
            hint_value = hint_value + 1
            print("\nIt is Incorrect. Please try again :)\n")

            if hint_value == 2:
                print("HINT: It is an action. last chances! \n")
            elif hint_value == 3:
                print("\nWrong ANSWER!! :(\nThe correct Answer is ' fighting '")
                hint_value = 0
                break


    while True:
        answer = input("What does hammer use for? \n")
        if answer.lower() == "hammering":
            score += 1
            print("\nIt is Correct! 1+ score!")
            break
        else:
            hint_value = hint_value + 1
            print("\nIt is Incorrect. Please try again :)\n")

            if hint_value == 2:
                print("HINT: It is an action. last chances! \n")
            elif hint_value == 3:
                print("\nWrong ANSWER!! :(\nThe correct Answer is ' harmmering '")
                hint_value = 0
                break


    while True:
        answer = input("What does 'with rizz' means? \n")
        if answer.lower() == "with love":
            score += 1
            print("\nIt is Correct! 1+ score!")
            break
        else:
            hint_value = hint_value + 1
            print("\nIt is Incorrect. Please try again :)\n")

            if hint_value == 2:
                print("HINT: It is a feeling. 2 chances left! \n")
            elif hint_value == 3:
                print("\nWrong ANSWER!! :(\nThe correct Answer is ' with rizz '")
                hint_value = 0
                break


    while True:
        answer = input("what is a guitar string made of? \n")
        if answer.lower() == "steel":
            score += 1
            print("\nIt is Correct! 1+ score!")
            break
        else:
            hint_value = hint_value + 1
            print("\nIt is Incorrect. Please try again :)\n")

            if hint_value == 2:
                print("HINT: It is an action. 2 chances left! \n")
            elif hint_value == 3:
                print("\nWrong ANSWER!! :(\nThe correct Answer is ' steel '")
                hint_value = 0
                break


    while True:
        answer = input("What is a stick? \n")
        if answer.lower() == "branch":
            score += 1
            print("\nIt is Correct! 1+ score!")
            break
        else:
            hint_value = hint_value + 1
            print("\nIt is Incorrect. Please try again :)\n")

            if hint_value == 2:
                print("HINT: It is from a tree. 2 chances left! \n")
            elif hint_value == 3:
                print("\nWrong ANSWER!! :(\nThe correct Answer is ' branch '")
                hint_value = 0
                break

    while True:
        answer = input("What does apple taste like? \n")
        if answer.lower() == "sweet":
            score += 1
            print("\nIt is Correct! 1+ score!")
            break
        else:
            hint_value = hint_value + 1
            print("\nIt is Incorrect. Please try again :)\n")

            if hint_value == 2:
                print("HINT: It is from a tree. 2 chances left! \n")
            elif hint_value == 3:
                print("\nWrong ANSWER!! :(\nThe correct Answer is ' sweet '")
                hint_value = 0
                break


    
    print("\nYou WIN!! Here is your Result\n")
    print("Score: '"+ str(score) + "'. You answer " + str(int((score / 7) * 100)) + "%" + " of the questions right!!!\n")
    input("Press ENTER to Quit! . . .")
      
want_to_play()
asking()

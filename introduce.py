print('Welcome to Flight Game')
answer = input('Are you ready to play the game ? (yes/no) :')

if answer.lower() == "yes":
    answer = input("Do you know the rules of the game? (yes/no) :")
    if answer.lower() == "no":
        print("HERE ARE THE RULES:")
        print("1. YOU WILL HAVE TO CHOOSE A DESTINATION WHERE YOU WANT TO GO")
        print("2. YOU WILL BE GIVEN OPTIONS OF THE CONNECTING AIRPORTS TO YOUR DESTINATION")
        print("3. THERE IS A LIMITED TIME SET FOR YOU TO REACH THE DESTINATION ")
        print("4. YOUR GOAL IS TO CHOOSE CORRECT CONNECTING AIRPORT AND REACH THE DESTINATION WITHIN THE TIME LIMIT")
        print("5. IF YOU REACH WITHIN THE TIME LIMIT THAT IS SET, YOU WIN!!!")
        print("--------------- LET'S  BEGIN ----------------\n\n")
    else:
        print("--------------- LET'S  BEGIN ----------------\n\n")

else:
    print("That's too bad!")


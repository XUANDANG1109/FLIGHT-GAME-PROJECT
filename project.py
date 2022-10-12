import random
import mysql.connector
from tabulate import tabulate
import time


connection = mysql.connector.connect(
         host='mysql.metropolia.fi',
         port= 3306,
         database='jenniheh',
         user='jenniheh',
         password='1234',
         autocommit=True
)


print('Welcome to flight game!')
player_name = input("Please write your name here: ")
print(f"Welcome to play {player_name}!")
time.sleep(3)
print("Once upon a time, there was a girl travelling around the world.")
time.sleep(3)
print("This girl had a beautiful relationship with a boy who she would meet in her destination country.")
time.sleep(3)
print("Unfortunately, she lost contact with him while traveling. :(")
time.sleep(3)
print("Now, the boyfriend only knows her destination but has to guess where she is transiting. He has 3 ONLY chances...")
time.sleep(3)
print("If he doesn't guess right, THEY WILL NEVER SEE EACH OTHER AGAIN! ")
time.sleep(3)
print("And if he guesses right, they live happily ever after. :)")

def main_page():
    while True:
        print("1. Instructions")
        print("2. Play")
        print("3. Exit the game")
        userinput = int(input("Choose the number: "))
        if userinput == "" or int(userinput) > 3 or int(userinput) < 1:
            input(int("Invalid input, choose a number between 1-3: "))
        elif userinput == 1:
            instructions()
        elif userinput == 2:
            print("Game starts...")
        elif userinput == 3:
            break
        return


def instructions():
    print("1. You will be given two lists of airports: all available airports and all available transit countries\n"
          "2. You have to choose a destination country.\n"
          "3. You will guess the right transit country for the destination you have chosen\n"
          "4. If you guess right, you will win If you guess wrong you will have 3 attempts more")
    inputInstructions = input("Press enter to go back to main page.")
    if inputInstructions == "":
        main_page()
        return


main_page()


def print_list(airport):
    #sql = "SELECT country, airport FROM all_locations"
    #sql += " WHERE country='" + airport + "'"
    cursor = connection.cursor()
    cursor.execute(" SELECT country, airport, icao FROM all_locations")
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in range(1):
            print(tabulate(result, tablefmt="fancy_grid"))
    print("Here is the list of available destination countries")
    return


airport = "Here is the list of available destination countries."
print_list(airport)


def dest(airport):
    sql = "SELECT country, airport FROM all_locations"
    sql += " WHERE country='" + airport + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"\n Your final destination is {row[0]} and the airport is {row[1]}")
    return


airport = input("\n Please enter the destination country: ")
dest(airport)


def connecting():
    countries =[]
    sql = "SELECT country, connecting_airports FROM connections"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            countries.append(row[0])
            countries. append(row[1])
            print(f" {row[1]} in {row[0]}")
    return countries


print("\n The list of connecting airports are: \n")
connecting()


def ran_connect(ran):
    sql = "SELECT country FROM connections"
    ran = random.choice(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    return ran


guess = input("\n Guess the connecting airport country: ")
correct = ran_connect(guess)
count= 0
while guess != correct and count <2:
    print("YOU'RE WRONG! TRY AGAIN BEFORE YOU LOSE HER!")
    guess = input("Guess the connecting airport: ")
    count += 1
if guess == correct:
    print("YAYYY TRUE LOVE STORY")
else:
    print("YOU WILL NEVER SEE HER AGAIN!!")
    print("Choose what you want to do.")

main_page()
# Project
# Final Destination Game
## Members:
- Hallikas Jenni
- Chauhan Rashi
- Dang Xuan
## Contents:
- [Introduction](https://github.com/XUANDANG1109/FLIGHT-GAME-PROJECT#introduction)
- [Vision](https://github.com/XUANDANG1109/FLIGHT-GAME-PROJECT#Vision)
- [Functional Requirements](https://github.com/XUANDANG1109/FLIGHT-GAME-PROJECT#functional-requirements)
- [Quality Requirements](https://github.com/XUANDANG1109/FLIGHT-GAME-PROJECT#quality-requirements)

### Introduction:
Final destination game project built using Python, Database SQL.

### Vision:
- The world at your fingertips. It is a game, Let's test your luck with this really simple game!.
- The aim of game is to create a game that is entertaining, fun, and a little bit of your luck. 

### Story:
The player is a guy who has a very beautiful girlfriend. Both live in Finland. The guy had to go to work, so she made the decision to travel alone to the destination she wanted to go. Unfortunately, while traveling, he lost contact with his girlfriend while in transit. The boyfriend only knows where she wants to travel, but he does not know where she will transit. In order to determine where she went, the boyfriend needed to guess the airport she was transiting through. The boyfriend has only three chances to figure out where the girl has traveled. After 3 wrong guesses, the couple will not see each other forever 💔, they are not destined for each other. If the guess is correct, the ending will be happy, the couple will get married 💕💕 and have children.... 


### Flowchart:
![image](https://user-images.githubusercontent.com/102602490/195088791-1e25afd9-b39d-40c0-ae7d-4d237ad57ec8.png)


#### How the game works:
- Final destination game - Fun game to pass time !
- A game is a single player game where players can fly from Finland to different cities and guess where you will be randomly transiting.
- Players start in Helsinki, Finland. They will choose a destination where they want to go. Then, they will guess where you will be transiting. This place is generated at random. The mission is that players need to guess where the transit matches the system's transit. Players have 3 attempts to guess. After 3 failed attempts, the game is over !!!

The user is able to do two things:
- Choose where they travel to
- Choose if they wish to transit they are currently in.

#### Setting:
Final destination game is set in present day.

### Functional Requirements:
Choose your favorite country and fly around the beautiful big open world and complete challenging missions in this realistic game. The success of a player is is a stroke of luck.

#### Functions:
Listed below are all the funtctions that were created for the game:

Database: airport, all_locations, connections, country
```
- dest
- connecting
- ran_connect
```
| UAE | Dubai International airport      | OMBD| 
|--------------|-------|------|-------|
| Hàng 2 | 2 x 1 | 2 x 2 | 2 x 3 | 2 x 4 |
| Hàng 3 | 3 x 1 | 3 x 2 | 3 x 3 | 3 x 4 |
| Hàng 4 | 4 x 1 | 4 x 2 | 4 x 3 | 4 x 4 |
Menu:
```
- main_page
- instructions
```
Decisions:
```
- dest
```

Prints:
```
-print_instructions
-print_play
-print_exit the game
-print_game starts
-print list of destination countries
-print list of connecting airports
```

### Quality requirements:
We created a new database from the existing one and removed a lot of unnecessary information. This made the database faster. All functions created were run through the PyCharm project. 

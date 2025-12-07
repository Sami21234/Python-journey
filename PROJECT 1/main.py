# PROJECT 1: SNAKE, WATER, GUN GAME
# We all have played snake, water gun game in our childhood. If you haven’t, google the rules of this game and write a python program capable of playing this game with the user.

'''
Logic
1 for snake
-1 for water
0 for gun

'''
import random   # importing random module to generate the random choices for computer

computer = random.choice([-1, 0, 1])
youStr = input("Enter your choice(s, w & g): ")
youDict = {"s":1, "w":-1, "g":0}
reverseDict = {1:"Snake", -1:"Water", 0:"Gun"}
you = youDict[youStr]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

# conditions for winning and losing

if(computer == you):
    print("It's a Draw!")
else:

    if(computer == -1 and you == 1):
        print("You Win!")

    elif(computer == -1 and you == 0):
        print("You lose!")

    elif(computer == 1 and you == -1):
        print("You lose!")

    elif(computer == 1 and you == 0):
        print("You Win!")

    elif(computer == 0 and you == 1):
        print("You lose!")

    elif(computer == 0 and you == -1):
        print("You Win!")

    else:
        print("Something went wrong")
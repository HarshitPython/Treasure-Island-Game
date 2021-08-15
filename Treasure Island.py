print("Welcome to Treasure Island")
print("Your mission is to find the Treasure Island")

a = input('In which direction you want to go? "left" or "right" \n ').lower()

if a == "left":
    b = input('You have come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. ?\n').lower()
    if b == "wait":
        c = input('You arrive at the island unharmed. There is a house with three doors. One "red", one "yellow", one "blue". Which colour do you choose ?\n').lower()
        if c == "red":
            print("It is room full of fire. Game Over.")
        elif c == "yellow":
            print("You found the treaure. You Win the game.")
        elif c == "blue":
            print("You enter a room of beats. Game Over.")
        else:
            print("You choose the wrong door. Game Over.")
    else:
        print("You got attacked by crocodile. Game Over.")
else:
    print("You fall into a hole. Game Over.")    
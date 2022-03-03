#Treasure Island game!




Start = True
while(Start == True):
    print("Welcome to Treasure Island. \nYour mission is to find teh treasure.")

    print("Youre at a cross road. Where do you want to go? Type 'Left' or 'Right'")
    userChoice = input("Left or right?")



    if (userChoice == "Right"):
        print("Fall into a hole. \nGame Over.")
        Start = False
        break
    elif (userChoice == "Left"):
        print("You came to a lake. There is a island in the middle of the lake. Type 'Wait' to wait for boat. Type 'Swim' to swim across.")

    userChoice = input("Swim or Wait?")
    if(userChoice == "Swim"):
        print("You choiced to swim and you swim a cross. Sadly in the middle of the lake you feel something attacking you, and you die by the hand of a giant trout \nGame Over")
        Start = False
        break
    elif(userChoice == "Wait"):
        print("You wait for the boat and getting over safe to the other side.")

    print("Once safe on the other side you see a house, you getting closer to the house and you see 3 doors")
    print("\nOne is 'Blue', another is 'Red' and the third is 'Yellow' \nwhich one do you open and walk into?")

    userChoice = input("Blue, Red or Yellow?")
    if(userChoice == "Blue"):
        print("You going into the blue door, and there is a light in the other end of this dark room. \n You walk towards the light, and once you are close to it, so close that you can almost touch it. \n "
              ,"You sense something behind you, and it is big beasts that are attacking and killing you. \nGame Over")
        Start = False
        break
    elif(userChoice == "Red"):
        print("You steping into the Red door. Inside you see a fire, the fire are going towards you in such a speed that you cant clouse the door on time. You die. \nGame Over")
        Start = False
        break
    elif(userChoice == "Yellow"):
        print("You step into the Yellow door, and what do you see? \nYes You got it you found the Treasure!!!! You Won!!!")
        Start = False
        break
    else:
        print("You dident choice a door and went strait into the wall, the wall ate you alive. \nGame Over")
        Start = False
        break


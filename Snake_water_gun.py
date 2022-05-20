import random

def game():
    print("-"*20)
    print("Your Choice:-",choice1)
    print("Computer Choice:-",Comp_choice)
    print("-"*20)
    


print("_"*20,"WELCOME TO THE GAME","_"*20)

n = int(input("How many rounds you want to play?"))
for i in range(1,n+1):
    print("_"*100)
    print("*"*5,"Round ",i,"*"*5)
    choice1 = str(input("please Select your choice.(s\w\g):"))
    s= "Snake"
    w = "Water" 
    g = "Gun"

    for i in range(1,10000):
        if choice1 == "s":
            choice1 = "Snake"
            print("You have choosen snake...!")
        elif choice1 ==  "w":
            choice1 = "Water"
            print("You have choosen water......!")
        elif choice1 == "g":
            choice1 = "Gun"
            print("You have choosen Gun......!")
        else :
            print("Wrong input ......! Pleasse enter your choice again....")
        break

    lst1 = ["Snake","Water","Gun"]
    Comp_choice = random.choice(lst1)

    for i in range(1,n+1):
        if choice1 == "Snake" and Comp_choice == "Water":
            game()
            print("||-- YOU WIN --||")

        if choice1 == "Snake" and Comp_choice == "Gun":
            game()
            print("||-- YOU LOSE --||")    

        if choice1 == "Snake" and Comp_choice == "Snake":
            game()
            print("||-- it's TIE --||")    

        if choice1 == "Gun" and Comp_choice == "Water":
            game()
            print("||-- YOU LOSE --||")

        if choice1 == "Gun" and Comp_choice == "Snake":
            game()
            print("||-- YOU WIN --||")    

        if choice1 == "Gun" and Comp_choice == "Gun":
            game()
            print("||-- it's TIE--||")

        if choice1 == "Water" and Comp_choice == "Gun":
            game()
            print("||-- YOU WIN --||")

        if choice1 == "Water" and Comp_choice == "Water":
            game()
            print("||-- it's TIE --||")

        if choice1 == "Water" and Comp_choice == "Snake":
            game()
            print("||-- YOU LOSE --||")  
        break
    
print("-"*45,"THANK YOU FOR PLAYING","-"*45)
print("_"*100)
input(print("how was the game?"))







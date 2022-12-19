import random

end = False
user_points = 0
computer_points = 0

while end == False:
    options = ["rock","paper","scissors"]
    user_input = input("Choose rock,paper,scissors or end")
    computer_input = random.choice(options)

    if user_input == "end":
        print("Game Exit")
        end = True
        print("User Points")
        print(user_points)
        print("Computer Points")
        print(computer_points)


    if user_input == "rock":
        if computer_input == "rock":
            print("Its a tie")
        elif computer_input == "paper":
            print("Computer Win")
            computer_points += 1
        elif computer_input == "scissors":
            print("You Win")
            user_points += 1

    elif user_input == "paper":
        if computer_input == "rock":
            print("You Win")
            user_points += 1
        elif computer_input == "paper":
            print("Its a tie")
        elif computer_input == "scissors":
            print("Computer Win")
            computer_points += 1

    elif user_input == "scissors":
        if computer_input == "rock":
            print("Computer Win")
            computer_points += 1
        elif computer_input == "paper":
            print("You Win")
            user_points += 1
        elif computer_input == "scissors":
            print("Its a tie")

    elif user_input!="rock" or user_input!="paper" or user_input!="scissors":
        print("Invalid input")
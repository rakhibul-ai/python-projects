import random

item_list = ["rock", "paper", "scissors"]  

user_choice = input("Enter your move (Rock, Paper, Scissors): ").lower()  
computer_choice = random.choice(item_list)

if user_choice not in item_list:
    print("Please make a valid move!!!")
else:
    print(f"Computer chose: {computer_choice.capitalize()}")  

    if user_choice == computer_choice:
        print("Both chose the same. Match Tie.")
    
    elif user_choice == "rock":
        if computer_choice == "paper":
            print("Paper covers rock. Computer Wins!")
        else:
            print("Rock breaks scissors. You Win!")
    
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("Paper covers rock. You Win!")
        else:
            print("Scissors cut paper. Computer Wins!")
    
    elif user_choice == "scissors":
        if computer_choice == "rock":
            print("Rock breaks scissors. Computer Wins!")
        else:
            print("Scissors cut paper. You Win!")





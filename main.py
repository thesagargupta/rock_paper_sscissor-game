import random
#computer code
computer = random.choice([1,2,3])
computer_option = {1:"rock", 2:"paper", 3:"scissors"}
computer_choice = computer_option[computer]

#user code
userchoice = input("Enter your choice: ")
choice = {"r":1, "p":2, "s":3}
user = choice[userchoice]
user_option = {1:"rock", 2:"paper", 3:"scissors"}
user_display = user_option[user]

print(f"your choice: {user_display} \ncomputer choice: {computer_choice}")

if (user == computer):
    print("Match Draw")
else:
    if(user == 1 and computer == 3):
        print("You Win!!")
    elif(user == 2 and computer == 1):
        print("You Win!")
    elif(user == 3 and computer == 2):
        print("You Win!")
    elif(user == 1 and computer == 2):
        print("You loose!")
    elif(user == 2 and computer ==3):
        print("You loose!")
    elif(user == 3 and computer ==1):
        print("You loose!")
    else:
        print("Try Again!!!")
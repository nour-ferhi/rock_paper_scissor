import random

choices= ["rock","paper","scissor"]
computer= random.choice(choices)
user = input("User: ").lower()
while user not in choices:
    user = input("User: ").lower()

if computer == user:
    print("user=",user)
    print("Computer=",computer)
    print("computer == You")
elif computer == "rock":
    if user == "paper":
        print("user=", user)
        print("Computer=", computer)
        print("You Win :)")
    else:
        print("user=", user)
        print("Computer=", computer)
        print("You Lose :(")

elif computer == "paper":
    if user == "scissor":
        print("user=", user)
        print("Computer=", computer)
        print("You Win :)")
    else:
        print("user=", user)
        print("Computer=", computer)
        print("You Lose :(")

elif computer == "scissor":
    if user == "paper":
        print("user=", user)
        print("Computer=", computer)
        print("You Lose :(")
    else:
        print("user=", user)
        print("Computer=", computer)
        print("You Win :)")

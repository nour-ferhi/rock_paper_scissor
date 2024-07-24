import random

while True:

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

    play_again= input("play again (yes/no): ").lower()
    if play_again != "yes":
        break

print("Bye! Se You Soon...")

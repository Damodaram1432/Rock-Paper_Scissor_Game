import random


def game():
    player=input()
    computer = random.choice(["rock", "paper", "scissors"])
    if (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (
            player == "scissors" and computer == "paper"):
        print("winner is player")
    else:
        print("winner is computer")


game()
import random

while True:
    choices = ['rock', 'paper', 'scissors']

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input('Rock, paper or scissors?: ').lower()

    if player == computer:
        print("Computer: ", computer)
        print("Player: ", player)
        print("Game Tied!")
    elif player == "rock":
        if computer == 'paper':
            print("Computer: ", computer)
            print("Player: ", player)
            print("You lose!")
        if computer == 'scissors':
            print("Computer: ", computer)
            print("Player: ", player)
            print("You win!")
    elif player == "scissors":
        if computer == 'rock':
            print("Computer: ", computer)
            print("Player: ", player)
            print("You lose!")
        if computer == 'paper':
            print("Computer: ", computer)
            print("Player: ", player)
            print("You win!")
    elif player == "paper":
        if computer == 'scissors':
            print("Computer: ", computer)
            print("Player: ", player)
            print("You lose!")
        if computer == 'rock':
            print("Computer: ", computer)
            print("Player: ", player)
            print("You win!")
    
    play_again = input('Would you like to play again? (yes/no): ').lower()

    if play_again != 'yes':
        break

print("\nThank you for playing. Goodbye!")
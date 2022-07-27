# Make a two-player Rock-Paper-Scissors game. 
# (Hint: Ask for player plays (using input), compare them, 
# print out a message of congratulations to the winner, and ask if the players want to start a new game)

# Remember the rules:

# Rock beats scissors
# Scissors beats paper
# Paper beats rock
# ans_dict = {
#     "rock" : 1,
#     "sisor"
# }
# player1_name = input("Enter name for player 1: \n")
# player1_ans = input(f"{player1_name} Enter you selection - Rock or Scissors or Paper: ")

# player2_name = input("Enter name for player 2: \n")
# player2_ans = input(f"{player2_name} Enter you selection - Rock or Scissors or Paper: ")
# continue_game = "yes"

# while continue_game == "yes":
#     if player1_ans == "Rock" and player2_ans == "Sissors" or player1_ans == "Sissors" and player2_ans == "Paper":
#         print(f"{player1_name} {player1_ans} Won the game. {player2_name} chose {player2_ans}")
#         continue_game = input("Do you want to continue? (yes or no): ")
#     elif player1_ans == "Rock" and player2_ans == "Rock" or player1_ans == "Sissors" and player2_ans == "Sissors" or player1_ans == "Paper" and player2_ans == "Paper":
#         print(f"Its a DRAW !!! {player1_name} and {player2_name} chose the same as {player1_ans}")
#         continue_game = input("Do you want to continue? (yes or no): ")
#     else:
#         print(f"{player2_name} {player2_ans} Won the game. {player1_name} chose {player1_ans}")
#         continue_game = input("Do you want to continue? (yes or no): ")

####Other way
# import random

# while True:
#     user_action = input("Enter a choice (rock, paper, scissors): ")
#     possible_actions = ["rock", "paper", "scissors"]
#     computer_action = random.choice(possible_actions)
#     print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

#     if user_action == computer_action:
#         print(f"Both players selected {user_action}. It's a tie!")
#     elif user_action == "rock":
#         if computer_action == "scissors":
#             print("Rock smashes scissors! You win!")
#         else:
#             print("Paper covers rock! You lose.")
#     elif user_action == "paper":
#         if computer_action == "rock":
#             print("Paper covers rock! You win!")
#         else:
#             print("Scissors cuts paper! You lose.")
#     elif user_action == "scissors":
#         if computer_action == "paper":
#             print("Scissors cuts paper! You win!")
#         else:
#             print("Rock smashes scissors! You lose.")

#     play_again = input("Play again? (y/n): ")
#     if play_again.lower() != "y":
#         break

import random
from enum import IntEnum

class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2
    Lizard = 3
    Spok = 4

def get_user_selection():
    user_input = [f"{action.name}[{action.value}]" for action in Action]
    user_input_str = ",".join(user_input)
    selection = int(input(f"Enter a choice ({user_input_str}): "))
    action = Action(selection)
    return action

def get_computer_selection():
    selection = random.randint(0, len(Action)-1)
    action = Action(selection)
    return action

# def check_winner(user_selection, computer_selection):
#     if user_selection == computer_selection:
#         print(f"Both players selected {user_selection.name}. It's a Tie.")
#     elif user_selection == Action.Rock:
#         if computer_selection == Action.Scissors:
#             print(f"You WON! - {user_selection.name} smashes {computer_selection.name}!")
#         else:
#             print(f"You LOST! - {user_selection.name} will be coverd by the {computer_selection.name}!")
#     elif user_selection == Action.Paper:
#         if computer_selection == Action.Rock:
#             print(f"You WON! - {user_selection.name} covers the {computer_selection.name}!")
#         else:
#             print(f"You LOST! - {user_selection.name} will be chopped by the {computer_selection.name}!")
#     elif user_selection == Action.Scissors:
#         if computer_selection == Action.Paper:
#             print(f"You WON! - {user_selection.name} choppes the {computer_selection.name}!")
#         else:
#             print(f"You LOST! - {user_selection.name} will be shameshed by the {computer_selection.name}!")

# check_winner(Action.Rock, Action.Scissors)


def determine_winner(user_action, computer_action):

    victories = {
            Action.Rock: [Action.Scissors, Action.Lizard],  # Rock beats scissors and Lizard
            Action.Paper: [Action.Rock, Action.Spok],  # Paper beats rock and spok
            Action.Scissors: [Action.Paper, Action.Lizard], # Scissors beats paper and Lizard
            Action.Lizard: [Action.Paper, Action.Spok], # Lizerd beats paper and spok
            Action.Spok: [Action.Lizard, Action.Scissors] # Spok beats lizard and scissors
        }

    defeats = victories[user_action]

    if user_action == computer_action:
        print ("Its a TIE !! Both selected the same.")
    elif computer_action in defeats:
        print (f"You Won! {user_action} beats {computer_action}")
    else:
        print (f"You Lost!! {computer_action} beats {user_action}")


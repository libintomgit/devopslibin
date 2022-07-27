# Make a two-player Rock-Paper-Scissors game. 
# (Hint: Ask for player plays (using input), compare them, 
# print out a message of congratulations to the winner, and ask if the players want to start a new game)

from enum import IntEnum
import random

class Action(IntEnum):
    Paper = 1
    Sissors = 2
    Rock = 3
    Lizard = 4
    Spok = 5

victory = {
    Action.Paper: [Action.Rock, Action.Spok],
    Action.Sissors: [Action.Paper, Action.Lizard],
    Action.Rock: [Action.Sissors, Action.Lizard],
    Action.Lizard: [Action.Paper, Action.Spok],
    Action.Spok: [Action.Sissors, Action.Rock]
}

def get_player_selection():
    user_input_choice = [f"{action.name}[{action.value}]" for action in Action]
    user_input_str = ", ".join(user_input_choice)
    user_input = int(input(f"Enter number of your choice ({user_input_str}): "))
    action = Action(user_input)
    return action

def get_computer_selection():
    comp_input = random.randint(1, len(Action))
    comp_selection = Action(comp_input)
    return comp_selection

def determine_winner(player_action, computer_action):
    defeats = victory[player_action]
    player_item = next(name for name, value in vars(Action).items() if value == {player_action})
    computer_item = computer_action
    if player_action == computer_action:
        print(f"Tie Game!! {player_item} and {computer_item} both are same!")
        print("I better WIN !! \nTry again ? ")
    elif computer_action in defeats:
        print(f"You WON and Computer LOST !! {player_item} beats {computer_item}")
        print("Its fun to beat the computer isn't it ? Let's beat again ?")
    else:
        print(f"Computer WON and You LOST !! {computer_item} beats {player_item}")
        print("Oh ho.. You must give it another shot, isn't it ?")

while True:
    try:
        player_action = get_player_selection()
    except ValueError as e:
        range_str = range(1, len(Action)+1)
        range_str_lst = [i for i in range_str]
        print(f"Invalid selection. Enter a value in range {range_str_lst}")
        continue
        
    computer_action = get_computer_selection()
    determine_winner(player_action, computer_action)

    play_again = input("(y/n): ")
    if play_again.lower() != "y":
        break




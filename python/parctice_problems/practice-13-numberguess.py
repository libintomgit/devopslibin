'''The task you have to perform is “Guess The number”. This task consists of a total of 10 points to evaluate your performance. 

 Problem Statement:-
Generate a random integer from a to b. You and your friend have to guess a number between two numbers, a and b. a and b are inputs taken from the user. Your friend is player 1 and plays first. He will have to keep choosing the number, and your program must tell whether the number is greater than the actual number or less than the actual number. Log the number of trials it took your friend to arrive at the number. You play the same game, and then the person with the minimum number of trials wins! Randomly generate a number after taking a and b as input and don’t show that to the user.

Input:
Enter the value of a

4

Enter the value of b

13

Output:
Player1 :

Please guess the number between 4 and 13

5

Wrong guess a greater number again

8

Wrong guess a smaller number again

6

Correct, you took 3 trials to guess the number

Player 2:

Correct, you took 7 trials to guess the number

Player 1 wins!

Accepting a coding challenge is an excellent way to improve your coding skills. So, keep practicing and keep yourself up to date with codewithharry.'''
from random import randint

import idna

# def guess_num_func(rand, tries):
#     guess_try = 1
#     point = 0
#     for i in range(tries):
#         print(i)
#         print(f"Guess Try : {guess_try}")
#         guess = int(input("Guess the Number: "))
#         if guess == rand:
#             point += 1
#             break
#         elif guess < rand and i+1 < tries:
#             print("You should guess higher!")
#             guess_try+=1
#         elif guess > rand and i+1 < tries:
#             print("You should guess Lower!")
#             guess_try+=1
    
#     if point == 0:
#         score = guess_try + guess_try
#     else:
#         score = guess_try + point

#     return score
def guess_num_func(rand, tries):
    
    print(i)
    print(f"Guess Try : {guess_try}")
    guess = int(input("Guess the Number: "))
    if guess == rand:
        point = 1
    elif guess < rand and i+1 < tries:
        print("You should guess higher!")
    elif guess > rand and i+1 < tries:
        print("You should guess Lower!")
    
    # if point == 0:
    #     score = guess_try + guess_try
    # else:
    #     score = guess_try + point

    return point

if __name__=='__main__':
    print("Welcome to Number Guess Game..")
    guess_num_range_start = int(input("Enter the starting range: "))
    guess_num_range_end = int(input("Enter the ending range: "))
    num_tries = int(input("Number of tries for each player : "))
    num_players = int(input("How many players : "))
    player_name = []
    for i in range(1,num_players+1):
        p_name = input(f"Enter the player name {i}: ")
        player_name.append(p_name)
    
    print(player_name)

    act_try = {}
    for n in range(len(player_name)):
        guess_random = randint(guess_num_range_start, guess_num_range_end)
        print(guess_random)
        print(f"{player_name[n]}, Your turn now.")
        for i in range(num_tries)
        guess_try_out = guess_num_func(guess_random)
        act_try[player_name[n]] = guess_try_out

    print(act_try)



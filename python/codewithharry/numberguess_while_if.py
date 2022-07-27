import random as ra

# To re-start the whole game again
while True:
    rand_num = ra.randint(1, 99)
    rand_hint_low = rand_num - 20
    rand_hint_high = rand_num + 20

# Guess the number prent logic
    guess_count_limit = 10
    guess_count = 0
    print("Guess the hidden number!!")
    print(rand_num)
# Guess occurance until the limit
    while guess_count <= guess_count_limit:
        if guess_count == 10:
            print(f"YOU LOST !! You have reached the maximum limit of guessing!!{guess_count_limit}")
            break
# Execpt the value error and continue
        try:
            user_guess = input("Enter your guess here: ")
            user_guess_int = int(user_guess)
            if user_guess_int == rand_num:
                print(f"Yay!! you just guessed it right! {user_guess}", end=" ")
                if guess_count+1 < 10:
                    print(f"And that was in {guess_count+1} Guess!! ")
                else:
                    print(f"And that was in the very last Guess!! ")
                break
            elif user_guess_int < rand_num:
                print(f"Ahaaaa!! You should guess higher!", f"\nHINT: Guess between {rand_hint_low} and {rand_hint_high}")
                guess_count += 1
                guess_count_rem = guess_count_limit - guess_count
                print(f"\nRemaining number of guess {guess_count_rem} ")
                continue
            elif user_guess_int > rand_num:
                print(f"Uhh hooo!! Keep your guess low!", f"\nHINT: Guess between {rand_hint_low} and {rand_hint_high}")
                guess_count = guess_count + 1
                guess_count_rem = guess_count_limit - guess_count
                print(f"\nRemaining number of guess {guess_count_rem} ")
                continue
        except ValueError:
            print("You have not entered a number right!! Enter any number between 1 to 99")
            continue

    print("\nDo you want to challenge again ?")
    user_input_replay = input("\nEnter any button to challenge again or\n\"N\" if you want to try again later: ")
    if user_input_replay.upper() == "N":
        print("\nGood Bye!!! I am here...If you dare...")
        exit(0)
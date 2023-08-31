def userAgePrediction(inpu, curr_year, year_pred):
    user_age = curr_year - inpu
    user_future = user_input + year_pred
    user_year_rem = user_future - curr_year
    if user_age == 100:
        print("You are 100 years old ")
    elif user_age > 100 and user_age <= 150:
        print("You are above 100 years old and clock is ticking ")
    elif user_age > 150:
        print(f"Ghoosh!! {user_age} years.. You are suppose to be in the world record.")
    elif user_age < 0:
        print(f"Wait for it.. You will be soon born in {user_input - curr_year} years.")
    else:
        print(f"You are {user_age} years old and on {user_future} you will be {year_pred} years old", end="\n")
        print(f"{user_year_rem} more years to go.. Have a good diet and dont forget to excercise!")
        print("Click on this link for more details on healthy dieting and excerceise")

def userYearPrediction(inpu, curr_year, year_pred):
    user_age = inpu
    user_year = curr_year - user_age
    user_future = user_year + year_pred
    user_year_rem = user_future - curr_year
    if user_age == 100:
        print("You are 100 years old ")
    elif user_age > 100 and user_age <= 150:
        print("You are above 100 years old and cock is ticking")
    elif user_age > 150:
        print(f"Ghoosh!! {inpu}.. You are suppose to be in the world record.")
    elif user_age < 0:
        print(f"Wait for it.. You will be soon born in {user_year - curr_year} years")
    else:
        print(f"You are born on {user_year} and on {user_future} you will be {year_pred} years old", end='\n')
        print(f"{user_year_rem} more years to go.. Have a good diet and dont forget to excercise!")
        print("Click on this link for more details on healthy dieting and excerceise")

while(True):
    years_to_predict = 100
    try:
        from datetime import date
        year_user_input = date.today()#int(input("Enter the current year (yyyy): "))
        curr_year = str(year_user_input)
        curr_year = int(curr_year.split('-')[0])
        print("Welcome to the Age calculator", end=" | ")
        print(f"Current year : {curr_year}")
        user_input = int(input("Enter your Age or Year of Birth(yyyy): "))
        if user_input > 1 and user_input <= 999:
            userYearPrediction(user_input, curr_year, years_to_predict)
        elif user_input > 1000 and user_input < 3000:
            userAgePrediction(user_input, curr_year, years_to_predict)
        else:
            print("Enter a valid input..")
    except Exception :
        print("Enter a valid input")

    check_user_input = input("\nPress any key to continue or C to cancel")
    check_user_input = check_user_input.lower()
    if check_user_input != "c":
        print(check_user_input)
        continue
    else:
        print("Thank you for using my age calculator !!")
        exit(0)
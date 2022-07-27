import os.path
import os
import time
import datetime
import re
from tabulate import tabulate

print("EZY HEALTH RECORD MANAGEMENT SYSTEM\n")
menu1 = "\n0 to Registering New Information\n1 to Retrieving Existing Information\n" \
        "2 to Registering New User\n3 to Change the User\n4 to Exit "
user_reg_yn = "Do you want to register this user? 'Y'(Yes) | 'N'(No) : "
suppor_contact_mesg = "Please contact the developer at customersforyou@ezy.com"

username = ""
def user_checkin():
    make_db_dir()
    print("Enter Your Name", end=" : ")
    global username
    username = input()
    menu_list()

def get_date():
    """log the current date and time"""
    import datetime
    return datetime.datetime.now()

def register_new_user():
    """registering new user to the database"""
    # name_input = input("Enter your Name: ")
    # username = name_input.lower()
    if check_user_registered(username) == username:
        print(f"\nHello {username.title()}, you are already a registered user."
              f"\nYou can chose the other options to check or log your health information.\n")
    else:
        with open('./db/user_data', 'a') as f:
            f.write(f"{username.lower()}\n")
            print(f"New user \"{username.title()}\" has been registered Successfully.\n")
        menu_list()
        return username

# Make db directory
def make_db_dir():
   if os.path.exists('./db') is True:
       pass
   else:
       os.mkdir('./db')

# Check if the user is
def check_user_registered(username):
    """returns the users name if its registered in the system file"""
    # user_name_input = input("Enter your name: ")
    make_db_dir()
    if os.path.exists('./db/user_data') is True:
        with open("./db/user_data") as f:
            user_meta = f.readlines()
        # print(user_name[1])
        for names in user_meta:
            if username.lower() in names:
                return username.lower()
    else:
        print("This user is not registered,", user_reg_yn)
        user_input = input()
        if user_input.lower() != "y":
            exit(0)
        else:
            register_new_user()

# Log ID generation for diet and workout entry uniq matching
def log_id_func():
    if os.path.exists('./db/id') is True:
        with open('./db/id') as f:
            last_line = f.readlines()[-1]
            # print(last_line)
            log_id = int(last_line) + 1
        with open('./db/id', "a") as f:
            f.write(f"\n{log_id}")
            # print(log_id)
            return log_id
    else:
        with open('./db/id', 'w') as f:
            f.write("10000")
            default_log_id = "10000"
            return default_log_id
    # return user_id

# Log user diet and workout information
def log_user_diet_workout():
    # name_input = input("Enter your Name: ")
    # log_id = 1

    if check_user_registered(username) == username:
        # print(f"\nHello {username.title()}, you are already a registered user."
        #       f"\nYou can chose the other options to check or log your health information.")

        log_id = log_id_func()
        time_stamp = get_date()
        # time_stamp.hour()
        print(time_stamp)
        print()
        print(username.title(), ",", end=" ")
        user_diet_input_meal1 = input("Enter your breakfast: ")
        user_diet_input_meal1 = user_diet_input_meal1.replace(" ", "-")
        user_diet_input_meal2 = input("Enter your mid-breakfast: ")
        user_diet_input_meal2 = user_diet_input_meal2.replace(" ", "-")
        user_diet_input_meal3 = input("Enter your lunch: ")
        user_diet_input_meal3 = user_diet_input_meal3.replace(" ", "-")
        user_diet_input_meal4 = input("Enter your evening-snacks: ")
        user_diet_input_meal4 = user_diet_input_meal4.replace(" ", "-")
        user_diet_input_meal5 = input("Enter your dinner: ")
        user_diet_input_meal5 = user_diet_input_meal5.replace(" ", "-")
        user_workout_input1 = input("Enter your workout: ")
        user_workout_input1 = user_workout_input1.replace(" ", "-")
        user_diet_workout = f"{log_id} {time_stamp} {username} {user_diet_input_meal1} {user_diet_input_meal2} " \
                    f"{user_diet_input_meal3} {user_diet_input_meal4} {user_diet_input_meal5} {user_workout_input1}"

        with open("./db/log_db", "a") as f:
            f.write(f"{user_diet_workout}\n")
        print(f"\n{username.title()}, your details have been logged successfully!\n")
        menu_list()
        # retrieve_user_diet_workout()
    else:
        print(f"User {username.title()} is not registered,", user_reg_yn)
        user_input = input()
        if user_input.lower() != "y":
            user_checkin()
        else:
            register_new_user()

def retrieve_user_diet_workout():
    import os
    import subprocess
    print(username.title(), "Please find your workout and diet history below.")
    if check_user_registered(username) == username:
        pattern = username
        pattern_line = []
        with open('./db/log_db') as f:
            for line in f:
                # print(line)
                if re.search(pattern, line):
                    pattern_line.append(line)
        # print(f"{pattern_line}")
        # print(f"{pattern}")
        pattern_line_split_list = []
        for line in pattern_line:
            pattern_line_split = line.split()
            pattern_line_split_list.append(pattern_line_split)
        # print(pattern_line_split_list)
        print()
        print(tabulate(pattern_line_split_list, headers=["id", "Date", "Time", "Name", "Breakfast", "Mid-Lunch", "Lunch", "Snacks", "Dinner", "Workout"]))
        #
        # pattern_line_diet = []
        # with open('./db/diet_db') as f:
        #     for line in f:
        #         # print(line)
        #         if re.search(pattern, line):
        #             pattern_line.append(line)
        #
        # pattern_line_split_list = []
        # for line in pattern_line:
        #     pattern_line_split = line.split()
        #     pattern_line_split_list.append(pattern_line_split)
        # # print(pattern_line_split_list)
        print()
        # print(tabulate(pattern_line_split_list, headers=["id", "Date", "Time", "Name", "Breakfast", "Mid-Lunch", "Lunch", "Snacks", "Dinner"]))
        # print("\n")
        print("Do you want to continue ? 'Y'(Yes) | 'N'(No) : ")
        user_input = input()
        if user_input.lower() != "y":
            exit(0)
        else:
            menu_list()
    else:
        print("This user is not registered,", user_reg_yn)
        user_input = input()
        if user_input.lower() != "y":
            user_checkin()
        else:
            register_new_user()

# Front - Entry logic
def menu_list():
    while True:
        try:
            print(f"Dear {username.title()}, Choose the desired options to proceed.")
            print(menu1)
            choice_input = int(input("\nEnter your option here: "))
            if choice_input == 0:
                try:
                    log_user_diet_workout()
                except Exception as e:
                    print(e)
                    print(f"Sorry we could not register your data! {suppor_contact_mesg}")
                break
            elif choice_input == 1:
                retrieve_user_diet_workout()
                # print("show_user_data")
                # show_user_data()
                break
            elif choice_input == 2:
                # print("register_new_user)
                register_new_user()
                # print("\nEnter the desired options to continue\n")
                # print(menu1)
                continue
            elif choice_input == 3:
                print("Checking out. Please wait for a moment.\n")
                time.sleep(3)
                user_checkin()
            elif choice_input == 4:
                exit(0)
            else:
                print("\nYou have to choose the available options 0 or 4\n")
                continue
        except ValueError:
            print("\nYou have to choose the available options 0 or 4\n")
            continue
user_checkin()
# log_id_func()
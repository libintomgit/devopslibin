import random

age_limit = 18
max_age = 70
min_age = 7

appl_number = random.randint(1,5000000)

a = None
print("Welcome to RTO portal")
print("\n1 To apply for new License\n2 To track the application\n3 To cancel the application")
while a != 0:
    user_option = input("\nPlease enter your option here: ")
    try:
        if user_option == "1":
            user_name = input("Enter your Name as per Aadhar Card: ")
            user_age = int(input("Enter your Age: "))
            later_years = age_limit - user_age
            if user_age >= max_age:
                print(f"Dear {user_name.title()}, Your age is {user_age} and application cut off limit is {max_age}.\nPlease visit the nearest RTO for fitness testing")
            elif user_age <= min_age:
                print(f"Dear {user_name.title()}, {user_age} year's ???! You are a child!.\nApply when you complete {age_limit} years old or Please visit the nearest RTO with your parents/ gaurdians.")
            elif user_age == age_limit:
                print(f"Dear {user_name.title()},", f"Your age ({user_age} years) is exactly the limit of license. We would need to verify you physically to process the application!")
            elif user_age > age_limit:
                print(f"Dear {user_name.title()},", f"(Age-{user_age} years) You are eligible for the license. Your application will be processed soon! \nNote down your Application Number  RTO/{appl_number} for further reference!")
            else:
                print(f"Dear {user_name.title()},", f"(Age-{user_age} years) You should me minimum {age_limit} years to apply for the License. Please re-apply after {later_years} years.")
            break

        elif user_option == "2":
            trac_num = input("Enter the Tracking number: ")
            print(f"Your Application {trac_num} still under process")
            break
        elif user_option == "3":
            trac_num = input("Enter the Tracking number: ")
            print(f"Your Application {trac_num} has been canceled")
            break
        else:
            print("Choose the correct options")
            print("\n1 To apply for new License\n2 To track the application\n3 To cancel the application")
    except ValueError:
        print("Choose the correct options")
        print("\n1 To apply for new License\n2 To track the application\n3 To cancel the application")
        continue
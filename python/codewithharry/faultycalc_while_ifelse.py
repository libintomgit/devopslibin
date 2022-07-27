user_name = input("Please enter your name to continue: ")

print("\nEnter\n+ (for addition)\n- (for subtraction)\n/ (for floating division\n// (for floor division\n* (for multiplication)\n** (for square root)\n% (for remainder) : ", end="")
while True:
    user_operator = input()
    if user_operator == "*":
        break
    elif user_operator == "+":
        break
    elif user_operator == "-":
        break
    elif user_operator == "/":
        break
    elif user_operator == "//":
        break
    elif user_operator == "**":
        break
    elif user_operator == "%":
        break
    else:
        print(f"\n{user_operator.upper()} is not a valid operator!")
        print("\nEnter one of the below operator sign matiching to your required operation \n+ (for addition)\n- (for subtraction)\n/ (for division\n* (for multiplication) : ", end="")
        continue
print("\nEnter a Number:", end=" " )
while True:
    user_number1_a = input()
    try:
        a = int(user_number1_a)
    except ValueError:
        print("Enter a Valid number!", end=": ")
        continue
    else:
        break

print(f"\nEnter an another number to {user_operator} with first number: ", end=" ")
while True:
    user_number2_a = input()
    try:
        a = int(user_number2_a)
    except ValueError:
        print(f"Enter a Valid second number to {user_operator} with {user_number1_a}", end=" : ")
        continue
    else:
        break

user_number1 = int(user_number1_a)
user_number2 = int(user_number2_a)

"""Below is the false result statement
45 * 3 = 555, 56 + 9 = 77, 56/6 = 4"""

if user_number1 == 45 and user_number2 == 3 and user_operator == "*":
    print(555,"\nI am not trust worthy")
    exit(0)
elif user_number1 == 3 and user_number2 == 45 and user_operator == "*":
    print(555,"\nI am not trust worthy")
    exit(0)
elif user_number1 == 56 and user_number2 == 9 and user_operator == "+":
    print(77,"\nI am not trust worthy")
    exit(0)
elif user_number1 == 9 and user_number2 == 56 and user_operator == "+":
    print(77,"\nI am not trust worthy")
    exit(0)
elif user_number1 == 56 and user_number2 == 6 and user_operator == "/":
    print(4,"\nI am not trust worthy")
    exit(0)
elif user_number1 == 6 and user_number2 == 56 and user_operator == "/":
    print(4,"\nI am not trust worthy")
    exit(0)

if user_operator == "*":
    print(f"{user_name}, the multiplication of\
 \'{user_number1}\' * \'{user_number2}\' is", user_number1 * user_number2)
elif user_operator == "+":
    print(f"{user_name} the sum of\
 \'{user_number1}\' + \'{user_number2}\' is", user_number1 + user_number2)
elif user_operator == "/":
    print(f"{user_name} the floating division of\
 \'{user_number1}\' / \'{user_number2}\' is", user_number1 / user_number2)
elif user_operator == "-":
    print(f"{user_name} the substraction of\
 \'{user_number1}\' - \'{user_number2}\' is", user_number1 - user_number2)
elif user_operator == "//":
    print(f"{user_name} the floor division of\
 \'{user_number1}\' / \'{user_number2}\' is", user_number1 // user_number2)
elif user_operator == "**":
    print(f"{user_name} the square root of\
 \'{user_number1}\' ** \'{user_number2}\' is", user_number1 ** user_number1)
elif user_operator == "%":
    print(f"{user_name} the remainder of\
 \'{user_number1}\' % \'{user_number2}\' is", user_number1 % user_number2)
    if user_number1 % 2 == 0:
        print(f"\nAlso {user_number1} Divisible by 2.")
    else:
        print(f"\nand {user_number1} is Not Divisible by 2.")
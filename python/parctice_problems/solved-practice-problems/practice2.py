# The exercise comes first (with a few extras if you want the extra challenge or want to spend more time), followed by a discussion. Enjoy!

# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

# Extras:

# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
#-----
# Extras:

# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

#import sys

######for to provide number in the script argument Ex. python3 practice2.py 23
#arg = int(sys.argv[1])
#user_num = int(input("Enter any number to chek if it is Even Number: "))

###### My solution

# if user_num > 0:
#     if user_num % 2 == 0:
#         print (f"{user_num} is an EVEN number")
#     else:
#         print (f"{user_num} is a ODD number")
# else:
#     print ("Please enter a number higher than 0")

#####other user solution
# def odd_number(num):
#     if num % 2 == 0 and num % 4 != 0:
#         print (f"The number {num} is EVEN.")
#     elif num % 2 == 0 and num % 4 ==0:
#         print (f"The number {num} is EVEN and is divisible by 4.")
#     else:
#         print (f"The number {num} is ODD.")

# odd_number(arg)

##### Solution from the creator

num = int(input("give me a number to check: "))
check = int(input("give me a number to divide by: "))

if num % 4 == 0:
    print(num, "is a multiple of 4")
elif num % 2 == 0:
    print(num, "is an even number")
else:
    print(num, "is an odd number")

if num % check == 0:
    print(num, "divides evenly by", check)
else:
    print(num, "does not divide evenly by", check)
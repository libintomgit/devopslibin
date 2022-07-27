#Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old. 
# Note: for this exercise, the expectation is that you explicitly write out the year (and therefore be out of date the next year). 
# If you want to do this in a generic way, see exercise 39.
#Extras:
#Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
#Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)


#Libin written

# user_name = input("Please enter your name:")
# user_age = int(input("Please enter your age:"))
# total_years = 100
# user_rem_years = total_years - user_age
# current_year = 2022
# user_100_year = current_year + user_rem_years
# mesg_print_count = int(input("Please enter the number of times you want to print it: "))

# for num in range(mesg_print_count):
#     print("Dear " + str(user_name) + ", on the year of " + str(user_100_year) + " you will turn 100 years old!" )

#Others written

name = input("Enter your name: ")
age = int(input("How old will you be this year: "))
currentYear = int(input("Enter current year: "))
dateOfBirth = currentYear - age
msg = (f'{name}, you will turn 100 in {dateOfBirth+100}'+ '\n')
print(msg)
nrOfCopies = int(input("Enter number of copies: "))
print(msg*nrOfCopies)
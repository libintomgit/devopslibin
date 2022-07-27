# Exercise 4 (and Solution)
# Create a program that asks the user for a number and 
# then prints out a list of all the divisors of that number. 
# (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

# Libin Solution
user_num = int(input("Enter a number to print all the divisibles of the provided number: "))
output = []

for elm in range(2,(user_num)):
    if user_num % elm == 0:
        output.append(elm)

print(f"Divisible numbers of {user_num} are:\n")
for elm in output:
    print(elm)


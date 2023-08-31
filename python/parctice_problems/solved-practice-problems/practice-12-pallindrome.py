'''The task you have to perform is “The Next Palindrome.” This task consists of a total of 15 points to evaluate your performance.

Problem Statement:-
A palindrome is a string that, when reversed, is equal to itself. Example of the palindrome includes:

676, 616, mom, 100001.

You have to take a number as an input from the user. You have to find the next palindrome corresponding to that number. Your first input should be the number of test cases and then take all the cases as input from the user.

Input:
3

451

10

2133

Output:
Next palindrome for 451 is 454

Next palindrome for 10 is 11

Next palindrome for 2311 is 2222

These tasks will improve your logic-making skills and logic is the basics of programming. The solution is discussed in tutorial#110. 
'''
print("Check the next possible Palindrome")
usr_inp_ite = int(input("Enter the number of items to check : "))

usr_inp_num_range = [0]
for i in range(usr_inp_ite):
    num = int(input(f"Enter the item number {i + 1} to ckeck: "))
    usr_inp_num_range.append(num)

pal_num = [0]
for n in usr_inp_num_range:
    for i in range(n+1,n*n):
        # if i < 10:
        #     asd = 
        #     pal_num.append(i)
        #     break
        if str(i) == str(i)[::-1]:
            pal_num.append(i)
            break

for i in range(usr_inp_ite):
    print(f"The next palindrom for the num {usr_inp_num_range[i+1]} is {pal_num[i+1]}")



'''
Problem Statement:-
Harry Potter has got the “n” number of apples. Harry has some students among whom he wants to distribute the apples. These “n” number of apples is provided to harry by his friends, and he can request for few more or a few less apples.

You need to print whether a number is in range mn to mx, is a divisor of “n” or not.


Input:

Take input n, mn, and mx from the user.

Output:
Print whether the numbers between mn and mx are divisors of “n” or not. If mn=mx, show that this is not a range, and mn is equal to mx. Show the result for that number.

Example:
If n is 20 and mn=2 and mx=5

2 is a divisor of20

3 is not a divisor of 20

…

5 is a divisor of 20

Have you solved this task? If yes, then it is time to check your solution. The solution is discussed in tutorial#106. 
'''
def divisoRange(num, min, max):
    for i in range(min, max+1):
        if num % i == 0:
            print(f"{i} is a divisor of {num}")
        else:
            print(f"{i} is not a divisor of {num}")

def abortCalc():
    user_abort = input("Enter Q to quit or any ther key to continue...")
    if user_abort.lower() == "q":
        exit(0)
    else:
        print("Welcome again !")

if __name__=='__main__':
    print("Welcome to the division calculator!")
    while True:
        try:
            user_num = int(input("Enter the number apple you have: "))
            user_mn_num = int(input("Enter the min number of students: "))
            user_mx_num = int(input("Enter the man number of students: "))
            if user_mn_num == user_mx_num:
                print("Minimum and Maximumb numbers are same and cannot be a range!!")
                abortCalc()
            else:
                divisoRange(user_num, user_mn_num, user_mx_num)
                abortCalc()

        except ValueError as e:
            print("You must type an integer (number) to check the devision")
            abortCalc()




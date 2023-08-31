"""Python Practice 3 | Python Tutorials For Absolute Beginners In Hindi #107
The task you have to perform is “Foods and Calories.” This task consists of a total of 15 points to evaluate your performance.

Problem Statement:-
You visited a restaurant called CodeWithHarry, and the food items in that restaurant are sorted, based on their amount of calories. You have to reserve this list of food items containing calories.

You have to use the following three methods to reserve a list:

Inbuild method of python
List name [::-1] slicing trick
Swap the first element with the last one and second element with second last one and so on like,
[6 7 8 34 5] -> [5 34 8 7 6]

Input:
Take a list as an input from the user

[5, 4, 1]

Output:
[1, 4, 5]

[1, 4, 5]

[1, 4, 5]

All three methods give the same results!

You are advised to participate in solving this problem. The solution is discussed in tutorial#108. """




num_list = [10,20,30,40,50,60,70,80,90]

# num_list.reverse()
# num_list[::-1]]

num_list=[10,20,30,40,50,60,70,80,90]
# elem_num= int(input("Enter the number of elements in list:"))
# for n in range(0,elem_num):
#     list_elem=int(input("Enter element" + str(n+1) + ":"))
#     num_list.append(list_elem)

reverse3 = num_list
for n in range(len(num_list)//2):
    reverse3[n], reverse3[len(reverse3) -n -1] = reverse3[len(reverse3) -n -1], reverse3[n] 

print(f"Actual List : {num_list}")
print(f"List using index reversing : {reverse3}")
num_list.reverse()
print(f"List using inbuilt module : {num_list.reverse()}")
print(f"List using list slising : {num_list[::-1]}")    


# temp=a[0]
# a[0]=a[n-1]
# a[n-1]=temp
# print("New list is:")
# print(a)



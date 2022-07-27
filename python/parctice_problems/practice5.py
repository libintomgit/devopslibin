# Take two lists, say for example these two:

#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

# Extras:

# 1.Randomly generate two lists to test this
# 2.Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 90, 90, 8, 55]
# # b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# # a = range(1,101)
# # user_input1 = int(input("Enter a starting range number: "))
# # user_input2 = int(input("Enter a ending range number: "))
# b = range(int(input("Enter a starting number: ")),int(input("Enter a ending number: ")))


# # for num in a:
# #     if num in b:
# #         c.append(num)

# # print(list(set(c)))

# # c = [num for ind, num in enumerate(a) if num in b]
# c = [num for num in a if num in b]

# print(list(set(c)))
# print(c)
# z = []
# for n in b:
#     z.append(n)
# print("User input range" + str(z))


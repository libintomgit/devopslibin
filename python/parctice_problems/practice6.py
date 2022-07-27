# Ask the user for a string and print out whether this string is a palindrome or not. 
# (A palindrome is a string that reads the same forwards and backwards.)

# Discussion
# Concepts for this week:

# 1. List indexing
# 2. Strings are lists



# usr_str = str(input("Enter a word to chek if it is Plaindrome:: "))
# usr_str_lst = []

# for i in usr_str:
#     usr_str_lst.append(i)

# # print(usr_str_lst[0:])
# # print(usr_str_lst[::-1])

# while len(usr_str_lst) != 0:
#     if usr_str_lst[0:] == usr_str_lst[::-1]:
#         print(f"{usr_str} is a Plaindrome word\n")
#     else:
#         print(f"{usr_str} is a not a Plaindrome word\n")
# else:
#     print("Enter any word!")



def palindrome_word(word):
    usr_word = str(input("Enter a word to check the Palindrome"))
    word = []
    for i in usr_word:
        word.append(i)

    if word[0:] == word[::-1]:
        print(f"{usr_word} is a Palindrome word\n")
    else:
        print(f"{usr_word} is a not a Palindrome word\n")

while 1 != 0:
    palindrome_word(word)
    if input("Do you want to exit ? (yes or no)") == "yes":
        break
    else:
        palindrome_word(word)
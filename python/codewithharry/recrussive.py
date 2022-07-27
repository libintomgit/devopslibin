#
# def iterative_funciton(n):
#     fac = 1
#     for i in range(n):
#         fac = fac * (i +1)
#     return fac
#
#
# def recrussive_function(n):
#     if n == 1:
#         return 1
#         print("it prints 1")
#     else:
#         return n * recrussive_function(n - 1)
#
# print(recrussive_function(5))
#
# var_first_name = "libin"
# var_second_name = "tom"
#
#
# var_msg = "I am %s %s" %(var_first_name.title(), var_second_name.title())
# print(var_msg)


#
# import base64
#
# message = "Python is fun"
# message_bytes = message.encode('ascii')
# base64_bytes = base64.b64encode(message_bytes)
# base64_message = base64_bytes.decode('ascii')
#
# print(base64_message)
#
# base64_message_decode = base64.b64decode(base64_message)
# print(base64_message_decode)

user_diet_input_meal = input("Enter your breakfast: ")
user_diet_input_meal1 = user_diet_input_meal.replace(" ", "-")
print(user_diet_input_meal1)
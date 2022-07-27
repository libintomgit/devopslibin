#
#
# dict_1 = {"libin":{"id": 1, "age": 31, "Mobile No": 9900068139},
#           "Neethu":{"id": 2, "age": 32, "Mobile No": 9900068739},
#           "Nathasha":{"id": 3, "age": 20, "Mobile No": 9900000000}
#         }
#
# with open("User_info", "w") as f:
#         # f.write("dict_1")
#         # for key, value in dict_1.items():
#                 # f.write('{%s:%s\n}' % (key, value))
#                 # f.write()
#     for item, values in dict_1.items():
#         f.write(item + '\n')
#         f.write("\n".join(["  {}: {}".format(value_key, digit) for value_key, digit in values.items()]) + '\n')
#         f.write('\n')
#
# with open("User_info") as f:
#         user_data_file = f.read()
#         user_data_file_dic = {}
#         # user_data_file_dic = user_data_file_dic.update(user_data_file)
#
# print

# def register_new_user():
name_input = input("Enter your Name: ")
with open("user_data", "a") as f:
    f.write(name_input)
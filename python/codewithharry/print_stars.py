row_no = int(input("Enter a number to print row: "))
user_ty = int(input("0 for Up Down and 1 for Down Up"))

# dict = {"True": 0,
#         "False": 1}
# print(dict.values())

bol_val = bool(user_ty)
print(bol_val)

if bol_val:
        for i in range(row_no):
                print("*" * i)

else:
        for j in range(row_no):
                print((row_no-j) * "*")

# R= int(input("Enter Row: "))
# N = int(input("Enter Boolean 1/0 :"))
# b = bool(N)
# if b:
#     for i in range(R):
#         print("*" * i)
# else:
#     for j in range(R):
#         print((R-j) * "*")
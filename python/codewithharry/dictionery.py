main_dic = {"API": {"abr": "Application Programing Interface","details": "API helps in connecting programs with other programs and prgramatically control the remore application"},
            "REST": {"abr": "Representatoinal State Transfer", "details": "Representational state transfer is a software architectural style that describes a uniform interface between decoupled components in the Internet in a Client-Server architecture."},
            "HTTP": "Hyper Text Transfer Protocol",
            "YAML": "yet another markup language",
            "JSON": "java script object notation",
            "MD": "mark down"}

for i in main_dic:
    print(i)
user_input1 = input("Enter the short form to know know the fullform: ")
user_input1 = user_input1.upper()
print(user_input1,"-", main_dic[user_input1]["abr"])
print(main_dic[user_input1]["details"])
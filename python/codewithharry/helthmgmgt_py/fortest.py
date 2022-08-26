

import datetime
import re
from tabulate import tabulate

# line = open("./db/diet_db")
#
# asearchObj = re.search( r'libin', line, re.M|re.I)
#
# if searchObj:
#    print ("searchObj.group() : ", searchObj.group())
#    print ("searchObj.group(1) : ", searchObj.group(1))
#    print ("searchObj.group(2) : ", searchObj.group(2))
# else:
#    print ("Nothing found!!")


##########
# import re
#
# line = "Cats tom smarter than Mouse\n Mouse gerry is smaller than Cats ";
#
# searchObj = re.search( r'(.*) tom (.*?) .*', line, re.M|re.I)
#
# if searchObj:
#    print ("searchObj.group() : ", searchObj.group())
#    print ("searchObj.group(1) : ", searchObj.group(1))
#    print ("searchObj.group(2) : ", searchObj.group(2))
# else:
#    print ("Nothing found!!")

##################
import re
import os
import subprocess
pattern = "neethu"
# with open('./db/diet_db') as f:
#    for line in f:
#       # print(line)
#       # line = line.rstrip() # remove trailing whitespace such as '\n'
#       # subprocess.call(['grep', line, 'my2.txt'])
#       if re.search(pattern, line):
#          print(line)
#          match_line = line


# pattern_line = []
# with open('./db/workout_db') as f:
#    for line in f:
#       # print(line)
#       if re.search(pattern, line):
#          pattern_line.append(line)
#
# pattern_line_split_list = []
# for line in pattern_line:
#    pattern_line_split = line.split()
#    pattern_line_split_list.append(pattern_line_split)
# # print(pattern_line_split_list)
# print(tabulate(pattern_line_split_list, headers=["id", "Date", "Time", "Name", "Workout"]))
#
# pattern_line_diet = []
# with open('./db/diet_db') as f:
#    for line in f:
#       # print(line)
#       if re.search(pattern, line):
#          pattern_line.append(line)
#
# pattern_line_split_list = []
# for line in pattern_line:
#    pattern_line_split = line.split()
#    pattern_line_split_list.append(pattern_line_split)
# # print(pattern_line_split_list)
# print(tabulate(pattern_line_split_list, headers=["id", "Date", "Time", "Name", "Workout"]))
#
# print(pattern_line_split)

import os.path

pattern_line = []
with open('./db/workout_db') as f:
   for line in f:
      # print(line)
      if re.search(pattern, line):
         pattern_line.append(line)

pattern_line_split_list = []
for line in pattern_line:
   pattern_line_split = line.split()
   pattern_line_split_list.append(pattern_line_split)
# print(pattern_line_split_list)
print(tabulate(pattern_line_split_list, headers=["id"]))

pattern_line_diet = []
with open('./db/diet_db') as f:
   for line in f:
      # print(line)
      if re.search(pattern, line):
         pattern_line.append(line)

pattern_line_split_list = []
for line in pattern_line:
   pattern_line_split = line.split()
   pattern_line_split_list.append(pattern_line_split)
# print(pattern_line_split_list)
print(tabulate(pattern_line_split_list, headers=["id"]))

print(pattern_line_split_list)


def print_banner():
   print("""\
   
   ███████╗███████╗██╗   ██╗    ██╗  ██╗███████╗ █████╗ ██╗  ████████╗██╗  ██╗
   ██╔════╝╚══███╔╝╚██╗ ██╔╝    ██║  ██║██╔════╝██╔══██╗██║  ╚══██╔══╝██║  ██║
   █████╗    ███╔╝  ╚████╔╝     ███████║█████╗  ███████║██║     ██║   ███████║
   ██╔══╝   ███╔╝    ╚██╔╝      ██╔══██║██╔══╝  ██╔══██║██║     ██║   ██╔══██║
   ███████╗███████╗   ██║       ██║  ██║███████╗██║  ██║███████╗██║   ██║  ██║
   ╚══════╝╚══════╝   ╚═╝       ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝   ╚═╝  ╚═╝
                           DATA MANAGEMENT SYSTEM
                           
   by Libin Tom.""")

print_banner()
1. Modules (cycle example)
    * there are many built in and external modules
    * Inbuilt modules https://docs.python.org/3/py-modindex.html
    * PIP is python package manager
    * pip install <module name> - for external modules
    * import <modulename> - for built in modules
2. Comments & escape statements
   * one line #
   * multi line """multi line """
   * escape charachter https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_ref_site.htm
3. Variables and type casting and user input
   * its a container which stores the value
   * type casting is chaging the type of a value str()
   * input("enter your number")
4. String data type slicing
   * mystr = "harry is good boy"
   * print(len(mystr)) - 19
   * print(mystr[20]) - error out of range
   * print(mystr[0:78]) - will all the available character and will not throw error
   * print(mystr[0:5:2]) - 2 escape character will print hry
5. List [mutable] and List functions & Touples (immutable)
   * methods in List listname.method() (listname.sort(), listname.reverse())
   * .pop(), .revese(), .append(), .remove(), .insert()
   * list methods https://www.w3schools.com/python/python_ref_list.asp https://www.programiz.com/python-programming/methods/list
   * interchange variables a, b = b, a
   * touples should have a comma for single element (1,)
   * touple methods https://www.w3schools.com/python/python_ref_tuple.asp
6. Dictionary & ints functions |
   * Key value pair
   * dictionary can have dictionery within dictname["key"]["key inside]
   * addition - dicname[123] = "some_value"
   * deletion - del dicname[123]
   * dicname2 = dicname1 is a link to dicname1 but not a copy, any changes will effect the original dic
   * copy - dicname2 = dicname1.copy()
   * update - dicname.update({"key": "value"})
   * print only keys - print(dicname.keys())
   * print key value pairs - print(dicname.item())
   * function list - https://www.w3schools.com/python/python_ref_dictionary.asp
7. Sets
   * is collection of well defined objects
   * set will have unique value - will not have any duplication
   * varname = set()
   * list in set - varname = set([1,2,3,4])
   * or list_var = [1,2,3,4] \n set_var = set(list_var)
   * methods of set - https://www.w3schools.com/python/python_ref_set.asp 
8. If | Else
   * its called ifelse ladder
   * if elif else
   * keywords - is, in, and, or, not
9. Loops for | while | continue | break
   * For <variable_within_for_loop> in <list or tuple or dict, etc>: (for num in numbers:)
   * for loop runs until the iteration completes i,e. item ends in the provided data types (list or tuple or dict)
   * both loops can have any number of if conditions under the loops to mach the 
   * while the statment is TRUE it keeps running until the statment becomes false
   * while True: or while 1: is same (this will keep the loop running until it breaks in the middle)
   * continue - will re-run the loop from where continue keyword is written
   * break - will break the loop at the place where break written
10. Operators
    * Arithmatic operator - helps is numarical calculations (+,-, /, //, *, **, %)
    * Assignment operator - to assign value to any number or variable (=, +=, -=, /=, %= )
    * Comparison operator - compare one with other and return boolean value (==, !=, <=, >=, )
    * Logical operator - true & false logics (and, or) true and false = false, true or false = true
    * Identity operator - compares the identity (is, is not) true is false = false, ture is not false = true
    * Membership operator - check if the member is the datatype (in, not in) list = [1, 2, 3, 4, 5] 5 in list = true, 5 not in list = False
    * Bitwise operator - works with binary numbers [0,1] (&(and), |(or))
11. Short hand if else
    * is not recommended to be used everywhere, but where ever just needed
    * Example:
      a = 10
      b = 15
      print("A is greater than B") if a>b else print("B is greater than A")
12. User defined functions
    * is used for the code re-usability
    * in function parameters  and return value is optional
    * Docstring - is a comment written within the function in the first line with """three quotes"""
      def func_name(arg1,arg2):
         """this is a test function for example purpose"""
    * the major use of docstring is that this information can be printed whenever needed from the huge junk of functions
    * syntax - print(functin_name.__doc__) this will print the information whenever needed
      this is a test function for example purpose
13. Try | Except Exception Handling
    * by implementing this in required time, code will not break with error but keeps running
    * Example:
      num1 = input("enter a number") #this is string
      num2 = input("enter a number") #this is a string
      try:
         print("The sum of two numbers",
               int(num1) + int(num2)) #when a non-numeric string is parsed in user input, it cannot be converted to integer, hence the code will exit with error.
      except Exception as e: #but here we are saying if try dint work, except the error and using the Exception store the message to e 
         print(e)
      or
      except ValueError: #here as its a value error, using the ValueError exception method, supress the error and continue the code
      continue
14. File IO
    * Is to access the stored files in the system
    * Modes:
      * "r" - Default (read the file) - 
      * "t" - Default (text mode - which contains text)
      * "w" - (write inside the file)
      * "x" - (create new file if not exists)
      * "a" - (append - add new content to the end of the existing content in the file)
      * "b" - (binary mode - to access the binary files)
      * "+" - (read and write)
    * open is the operations key to deal with the files file_var = open("directory/filename.txt", "r")
    * its always good practice to close the file after user - file_var.close()
    * note content in the file is read character by character, 
      hence each time when you reach the opened file it will continue reading from where it was read last
      and that reason, when you read/print the file again in the new line what ever is missing will be consumed already
      and it will print anything what is remaining.
    * Ex. var_name = open("filename.txt) now this has opend the file to the pointer/handlere
      and while we run print(var_name.read) it reads and prints all the data so if you print the same statement again
      there will be no content and if you read the few charachteres print(var_name.read(3)) it will print the 
      letters and if you run the print again print(var_name.read()) it prints from the 4th character
    * function
      * var_name.read()
      * var_name.close()
      * var_name.readline() - outs single single each line
      * var_name.readlines() - will make the list with new lines
    * Write - deletes the existing content and writes the new content
      * file_handler = open("filename.txt", "w")
      * file_handler.write("This is the first line")
      * file_handler.close()
    * Append - adds new content to the end of the existing content in the file
      * file_handler = open("filename.txt", "a")
      * file_handler.write("This is the first line\n")
      * file_handler.close()
    * variable = file_handler.write("this is a text test line") 
      print(variavle) - will print the length of characters written to the file, but not the content itself.
      in the above scenario it will be 24 characters
    * Read and Write together +
      * file_handler = open("filename.txt", "r+") - using this method we can read and also write to the same file
    * Seek | Tell function
      * seek will set the pointer to where ever needed file_handler.seek(10) will place the cursor in 10th character
      * Tell file_handler.tell() will print the cursor location character number
    * With
      * this is as same as reading and closing the file
        with open("filename.txt" "rt") as f:
            a = f.readline()
            print(a)
15. Scope | Global variable | Global keyword
    * Global variable is a variable used by all the functions which is written out of the function
    * Local variable is only available within the function
    * global keyword is used to access/change the global variable value
    * Under nested function GLOBAL keyword will not access the value of any variable in the nested function but it just access the global
      variable outside all the function
16. Recrussive | Iterative
    * Recrussion means using functin within the function
    * https://www.youtube.com/watch?v=UhCObChYSMc&list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME&index=35&ab_channel=CodeWithHarry
    * Recrussion error: maximum recrussion error 
    * Compared to Iterative, Recrussive method is slightly difficult to debug when it has more complex recrussions but
      but will make coding easy when used for small purpose, like below.
    * Iterative approch:
      * using iteration for the find the value
        def iterative_factorial(n):
            fac = 1
            for i in range(n):
                fac = fac * (i +1)
            return fac
    * Recrusive approch:
      * using recrussive to find the value
        def recrussive_factorial()
            if n == 1:
                return 1
            else:
                return n * recrussive_function(n-1)
17. Lambda or Anpnymous function
    * is quick way to create a small anonymous function
    * lambda function: var_name = lambda x,y: x +y
    * normal function for the above problem:
      def add_number(x,y):
            return x + y
18. Modules
    * pupularly used - https://learnpython.com/blog/most-popular-python-packages/

19. String formatting | F String
    * string formatting - adding variables between the string var_name = "libin", var_msg = "I am %s" %var_name
    * F string formatting is using f before the string starts. f" I am {var_name}"
    * in f string we can use python variable expressions

20. *Args and *Kwargs
    * *agrs in the function consumes all the arguments provided
    * *args can be any name but not just args (ex. it can be *argument, *somethingelse), but should start with the *
    * along with the *args, we van pass the single arg also as usual
      var_name = ["one", "two", "three", "four"]
      name = "Numbers"
      def args_func(single_arg, *agrs):
            print(single_arg)      
            for item in args:
                print(item)
      args_func(name, *var_name)
    * but any given point the placement of the arguments should be - def func_name(normal_arg, *args, **kargs)
    * **kwargs (or **anyword) is used to handle dictionary like data structue
      dic = {"person1":"one", "person2": "two", "person3": "three", "person4": "four"}
      def func(normal, *args, **kwargs):
            for key, value in kwargs.items():
                print(f"{key} is {value}")
      func(**dic)
      person1 is one
      person2 is two
      person3 is three
      person4 is four
21. Time module
    * can be sued to record the time a program took to execute
     import time
     initial_time1 = time.time()
     for i in range(100):
        print("Some code to process")
     print(f"the time took to process this code is {time.time() - initial_time1 seconds")
     
     initial_time2 = time.time()
     k = 0
     while k<100:
        print("run some code")
     print(f"the time took to process this code is {time.time() - initial_time2} seconds")
    * and to check the average time run the code many times (example 1000) record the each runtime and divide it with 1000
    * https://www.geeksforgeeks.org/python-time-module/
    * 
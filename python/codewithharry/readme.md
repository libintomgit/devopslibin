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
    * global keyword is used within the function to access/change the global variable value
        var_name = 
        def some_func():
            global var_name
            var_name = "Something"
    * This will change the var value globally from within the function
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
22. Virtual environment | Requirements.txt
    * virtual environment is an isolated location where the global changes in the system dose not effects the packages in the virtual environment
    * pip install virtualenv - will install python virtual environment
    * virtualenv <directory_name> - will create a clone of the python inside the virtual environment directory mentioned in the command
    * source bin/activate - will activate the virtual env in the terminal (this is for mac and linux)
    * now what ever you install within the vir env stay within the same
    * for new modules use pip install <module_name> and to remove pip uninstall <module_name>
    * virtualenv --system-site-packages <user_virtual_env_name> - this command will create a virtual env with all the packages installed in the system
    * Requirements.txt file will contain the package used in the code to run successfully
    * requirements file will be shared along with the code rather than sharing the virtual env directory itself, so that anyone can create new vir env and install the required
      packages for the code to run
    * pip freeze > requirements.txt - command will create the requirement file with all the external module(package) names with exact version used in the code
    * pip install -r requirements.txt - will automatically install all the packages required
23. Enumarate
    * is a function which iterates index and value of each element in the list
      for index, item in enumerate(list_name):
            if index % 2 is 0: (or any statement to filter based on the index)
                print("whatever") 
24. How IMPORT command works
    * import some_module as sm - will bring the some_module to sk scope
      * sys.path - is the paths where it searches for the modules and imports it
        import sys
        print(sys.path)
      Example: ['', '/opt/homebrew/Cellar/python@3.9/3.9.13_1/Frameworks/Python.framework/Versions/3.9/lib/python39.zip',\
      '/opt/homebrew/Cellar/python@3.9/3.9.13_1/Frameworks/Python.framework/Versions/3.9/lib/python3.9',\
      '/opt/homebrew/Cellar/python@3.9/3.9.13_1/Frameworks/Python.framework/Versions/3.9/lib/python3.9/lib-dynload',\
      '/Users/libintom/Library/Python/3.9/lib/python/site-packages',\
      '/opt/homebrew/lib/python3.9/site-packages']
    * import file_name - will import the your code from the other file
      import file2
      print(file2.function_name_infile2())
      0r
      from file2 import function_name/var_name
      print(function_name/var_name())
    * but it is recommended not to import the functions or vars from the file rather import the whole file and use it where ever required with the file name (file2.something)
25. if __name__='__main__':
    * when python file1(main file) is imported into file2, when you run the file2 it will run all the code which is in the file1 and as result along with importing the functions
      whatever other content is written in the file1 will also be executed
      * if __name__='__main__': is used in the file1 (main file) to avoid this behaviour, so every other content apart from functions will be written under this
      **FILE1 (MAIN FILE)**
        def get_date():
            """log the current date and time"""
            import datetime
            return datetime.datetime.now()
        def make_db_dir():
            """Make db directory"""
            if os.path.exists('./db') is True:
                pass
            else:
                os.mkdir('./db')
        if __name__=='__main__':
            print(get_date())
            make_db_dir()
       **FILE2**
        import file1
        print(file1.get_date())
    * by doing this, the contents in the main will not exected when you call this file1 where ever you import
    * print(__name__) returns __main__ - this means, the __name__ s value will be __main__ only when you run the program in which this had added
    * but when this is imported to other program and executed, the __name__s value will be file1
26. Join Function
    * var_name = " and ".join(list_name)
    * so in the place of " and " use any charachter to join the list
27. Map, Filter and Reduce
    * MAP is used to typecast/run function on the data type in a list
      * convert the below strings in the list to integer 
      **method without map** 
        var_name = ["1", "2", "3", "4", "5"]
        for i in range(len(var_name)):
            var_name[i] = int(var_name[i])
      **using map**
        var_name = ["1", "2", "3", "4", "5"]
        var_name = list(map(int,var_name))
        output
        [1,2,3,4,5]
        * convert the below integer to square root
        **map with function
          def sqr_rt(x):
              return x*x
          var_name = [1,2,3,4,5]
          square_root = list(map(sqr_rt, var_name))
        **map with lambda 
          var_name = [1,2,3,4,5]
          square_root = list(map(lambda x: x*x, var_name))
          output
          [1, 4, 9, 16, 25]
        ** running functions from a list
          def square_rt(x):
              return x*x
        
          def qube_rt(x):
              return x*x*x
          func = [square_rt, qube_rt]
          for i in range(5):
              val = list(map(lambda x: x(i), func))
        
          result
          [0, 0]
          [1, 1]
          [4, 8]
          [9, 27]
          [16, 64]
    * FILTER function takes the function and iterable and returns the filtered value
      var_list1 = [1,2,3,4,5,6,7,8,9]
      
      def is_greater_5(num):
            return num>5
      
      greater_than_5 = list(filter(greater_than_5, var_list1))
      print(val)
      results in printing the list with all the numbers greater than 5 [6,7,8,9]
    * REDUCE is a part of functool module (form functools import reduce)
      list1 = [1,2,3,4,5,6]
      num = reduce(lambda x, y: x+y, list1)
      print num (result will ve 1+2+3+4+5+6 = 21)

28. Decorators 
    * is something that modifies the functionality of the functions
    * we can call functions within function and can return function in the function
      def dec1(func1):
         def now_exec():
            print("Executing now")
            func1()
            print("Executed")
      
      def who_is_harry():
         print("Harry is a man")
      
      who_is_harry = dec1(who_is_harry)
      who_is_harry()
      
      RESULT
      Executing now
      Harry is a man
      Executed
    * and in python this line who_is_harry = dec1(who_is_harry) can be written in short form using @
      @dec1
      def who_is_harry():
         print("Harry is a man")
      
      ----------------------------Another example-------------------------------
      def current_date_string(func1):
          def string1():
               print("The date and time now is", end=": ")
               print(func1(), end=". ")
               print("Thanks")
          return string1

      @current_date_string
      def get_date():
         """log the current date and time"""
         import datetime
         return datetime.datetime.now

       get_date()
       RESULT
       The date and time now is: 2022-07-31 17:07:09.104533. Thanks
29. Object Oriented Programing
    * Classes is a template
    * Object is an instance of a class
    * example leave letter (leave letter template is class and one instance of letter using that template is object)
    * OOP is used on DRY concept - Donot Repeat Yourself
     class students()
          pass
    
     libin = student()
     tom = student()
     libin.name = "Libin Tom"
     libin.age = 31
     tom.name = "Tom Tom"
     tom.age = 55

     print(libin.name, tom.name)
    * it's a good practice to start any class name with the Title case
    * classs arrtibutes can be changed using class name only not using the object
    * self - is self, when ever it is used on the instance that instance will be self
      class Employee():
            no_of_leaves_month = 4
            def print_details(self):
                return f"Employeed name is {self.name}, Salary {self.salary} and rele {self.role}"
      
      libin = Employee()
      tom = Employee()
      
      libin.name = "Libin Tom"
      libin.salary = 70000
      libin.role = "Devops"
      tom.name = "Tom Tom"
      tom.salary = 70000
      tom.role = "Devloper"
      print(libin.print_details())
      Employeed name is Libin Tom, Salary 70000 and rele Devops
      print(tom.print_details())
      Employeed name is Tom Tom, Salary 70000 and rele Devloper
  29.1. self and __init__ CONSTRUCTOR - constructes the attributes
      class Employee:
          no_of_leave_month = 4
          def __init__(self, vname, vsalary, vrole):
            self.name = vname
            self.salary = vsalary
            self.role = vrole
        
          def print_employee_details(self):
            return f"Employee name is {self.name}, Salary {self.salary} and rele {self.role} - Number of monthly leaves {Emp"
        
        libin = Employee("Libin Tom", 75000, "Junior Devops")
        Tibin = Employee("Tibin George", 200000, "Senior Devops")
        Neethu = Employee("Neethu Jose", 150000, "Project Manager")
        
        try:
            print(Tom.print_employee_details())
        except NameError as e:
            print("This employee is not in the database. Please check the spelling and search again.")
        
  29.2. @classmethod (Class methods) - can only access the instance variables of that class, can be accessed through any instance or class
      * but this will change only the class attributes values not the instance
        class Employee:
            no_of_leave_month = 10
            def __init__(self, vname, vsalary, vrole):
                self.name = vname
                self.salary = vsalary
                self.role = vrole
        
            def print_employee_details(self):
                return f"Employee name is {self.name}, Salary {self.salary} and role {self.role} - Number of monthly leaves {Employee.no_of_leave_month}"
        
            @classmethod
            def change_leaves(cls, newleaves):
                cls.no_of_leave_month = newleaves
        
        libin = Employee("Libin Tom", 75000, "Junior Devops")
        Tibin = Employee("Tibin George", 200000, "Senior Devops")
        Neethu = Employee("Neethu Jose", 150000, "Project Manager")
        
        try:
            print(Tibin.print_employee_details())
            libin.change_leaves(4)
            print(Tibin.print_employee_details())
            print(Employee.no_of_leave_month)
        
        except NameError as e:
            print("This employee is not in the database. Please check the spelling and search again.")
        
        Response:
        Employee name is Tibin George, Salary 200000 and role Senior Devops - Number of monthly leaves 10
        Employee name is Tibin George, Salary 200000 and role Senior Devops - Number of monthly leaves 4
        4
      
        * @classmethods as Alternative constructor this can be used to update the existing constructor
          class Employee:
              no_of_leave_month = 10
              def __init__(self, vname, vsalary, vrole):
                  self.name = vname
                  self.salary = vsalary
                  self.role = vrole
          
              def print_employee_details(self):
                  return f"Employee name is {self.name}, Salary {self.salary} and role {self.role} - Number of monthly leaves {Employee.no_of_leave_month}"
          
              @classmethod
              def change_leaves(cls, newleaves):
                  cls.no_of_leave_month = newleaves
          
              @classmethod
              def from_string(cls, string):
                  # param = string.split("-")
                  # return cls(param[0],param[1],param[2]) # actually whats happening
                  return cls(*string.split("-")) #one liner code
          
          
          libin = Employee("Libin Tom", 75000, "Junior Devops")
          Tibin = Employee("Tibin George", 200000, "Senior Devops")
          Neethu = Employee("Neethu Jose", 150000, "Project Manager")
          Jijo = Employee.from_string("Jijo Joseph-150000-General Manager")
          
          try:
              print(Jijo.print_employee_details())
              # print(Tibin.print_employee_details())
              # libin.change_leaves(4)
              # print(Tibin.print_employee_details())
              # print(Employee.no_of_leave_month)
              # print(Jijo.print_employee_details())
          
          except NameError as e:
              print("This employee is not in the data
          Response
          Employee name is Jijo Joseph, Salary 150000 and role General Manager - Number of monthly leaves 10

  29.3. Static Method @staticmethod
        * is used to call any string " def func_name(string): "
        * functions are used within the classes when the function is only used on the instance of the calss method
        * for example libin = class_name() is an instance of the class and using func_name() will work only for libin instance.
          
          @stringmethod
          def print_string(string):
              print(f"{string} is a good thing")

          print(Employee.print_string("book"))
          print(libin.print_string("book"))
  
  29.4. Abstraction & Encapsulation
        * Abstraction is fragments of works (mouse or keyboard or monitor is a layer of abstraction in a computer)
        * to achive abstraction we have to do encapsulation
        * encapsulation means hiding the implementation. insde a capsule
        * which means when a program spesific to a iteam (like players in games) within the class like above its called abstraction and encapsulation
          becasue this class can be called anytime anywhere and variables specific to the class will stay in that
  
  29.5. Single Inheritence
        * inheriting the functions of other class
        * class class_name(existing_class_name):
  
  29.6. Multiple Inheritence
        * inheriting multiple class in one cass
        * class class_name(existing_class_name1, existing_class_name1):
        * here the first inheritance will have higer priority
        * hence common instance in the both the inherited calsses first one will be used
  
  29.7. Multilevel Inheritence
        * is inheriting the class in one another
            class Dad:
                pass
            class Son(Dad):
                pass
            class Grandson(Son):
                pass
        * harry = Grandson()
            will check in itself and the son and then dad.
            
  29.8. Public, Protected and private access specifiers
        * are used to protect the variables
        * _ is used to protect and can be used by the child classess
          _var_name = "value"
        * __ is used to private it cannot be used outside
          __var_name = "value"
        * else to should use name angling
          class_inst = Class_name():
          print(class_inst._Class_name__var_name)
  
  29.9. Polymorphism 
        * Means ability to take various forms
        * this changes the default behaviour of the object by overwriting
  
  29.10. Super() and overriding
        * when the class is inherited in the subclass and if objects/methods are over written in the subclass the super class will not be executed
        * super is used to access the super class methods when the methods are overridden in the sub class
          Class A:
            var_name = "some string in calss A"
            def __init__(self):
                self.var1 = "I am inside class A"
                self.classvar1 = "I am in A"
                self.special = "Special string"
          Class B(A):
            var_name = "some string in class B with same var_name as class A"
            def __init__(self):
                self.var1 = "I am inside class A"
                super().__init__()
                print(super().classvar1)
          a = A()
          b = B()
          print(b.special, b.var1, 
  29.11. Dimond shape problem in multiple inheritance
        * more than a problem multiple inheritance is a confusion. when you inherit from multiple classes programer will get confused as if from where it is running in an instance
        * so it is always good to avoid multiple inheritance
  29.12. Operator overloading and dendor method
         class Employee:
          no_of_leave = 4
          
          def __init__(self, vname, vsalary, vrole):
            self.name = vname
            self.salary = vsalary
            self.role = vrole
        
          def print_employee_details(self):
            return f"Employee name is {self.name}, Salary {self.salary} and rele {self.role}"

        * any method starts with dunderscore __methodname__ they are special methods because they are constructor
        * Operator overloading -
          emp1 = Employee("libin", 3000, "Python Devops")
          emp2 = Employee("Tom", 2000, "Datacenter")
          
          * when you add any 2 objects like emp1 + emp2, an __add__ dunderscore method will run in the background

          def __add__(self, other):
            return self.salary + other.salary

          print(emp1 + emp2)

          Output:
          5000
          * this means that special __add__ method took the first argument object emp1 salary as self and second argument as other emp2 objests salary and added it

          * and this is helping us in operatory overloading
          * likewise there are many methods.. check the list in the internet https://docs.python.org/3/library/operator.html
          http://davis.lbl.gov/Manuals/PYTHON-2.4.3/lib/operator-map.html

          * __repr__(self):
              return self.print_employee_details
              or
              return f"Employee name is {self.name}, Salary {self.salary}, Role {self.role}
          
          print(emp1)
          Employee name is Libin, Salary 3000 and rele Python Devops

          * difference between __repr__(self) and __str__(self)
          __repr__(self) - Creates a full string representation of an object
          __str__(self) - Creates an informal string representation

          * str is the default selection when if both str and repr is used unless its specified like below
            print(rerp(emp1))
            pritn(str(emp1))

          * so this how we overrige the function and is called operator overloading
  
  29.13. Operator overloading and dendor method
        * Abstract base class and @abstractmethod
        * ABC - Abstract base clas is a module in python
          from abc import ABC
        * so if we inherit any calss with ABC metaclass, which will mandates to implement some methods in the child class
          
          class Shape(ABC):
              @abstractmethod
              def printarea(self):
                  return 0

          class Rectangle(Shape):
              def __init__(self):
                  self.length = 6
                  self.breadth = 7
                
              def printarea(self):
                  return self.lenght * self.breadth
          
          This way it mandates to write methods in the chiled class and in the above example if printarea method not defined, it will throgh an error when you create a object with the child class
          NOTE: That we cannot create object of the abstract class 
          
  29.13. Setters and Property Decorators
        * When object is created and only then will initialise the constructor but when you update the object it will not run the whole constructor angain for problems like below will uccor

        class Employee:
            def __init__(self, fname, lname):
                self.fname = fname
                self.lname = lname
                self.email = f"{fname}.{lname}@somedomain.com"

        objec1 = Employees("libin", "Tom")
        now it initialises the constructor with firstname libin second name tom and email as libin.tom@somedomain.com

        object1.Employee.fname = "Tibin"
        we expect it to change the email but unfortunately it change only the fname becasue the constructor runns only while creating the object

        solution:1
        rather entering email in the constructor, create a method called email and use the decorator @property above the method

        @property
        def email(self):
            if self.fname == None or self.lname == None:
              return "Email is not added. Please set it using setter"
            return f"{fname}.{lname}@somedomain.com"

        @setter - is used to change the fname and lname using the user input of email

        @email.setter
        def email(self, string):
            print("Setting now....")
            names = string.split("@")[0]
            fname = name.split(".")[0]
            lname = name.split(".")[1]


        @email.deleter
        def email(self):
            self.fname = None
            self.lname = None

        del object1.email
        will return
        None.None@somedomanin.come

        to fix that add condition in the email setter
  
  29.13. Object inrospection
      * Means knowing about the object which class, type, how it is storing, etc
      * type print(type(objectname)) - will show the type of the object (example string )
      * id print(id(objectname)) - will show the id of the object
      * dir print(dir(objectname)) - will print all the methods available in the object

30. Generators
      > Iterable
        * __iter__() or __getitem__()
        * Is getting to know if an item is iterable like callable one after one 1,2,3,4,
      > Iterator
        * __next__() 
        * If an item is iterable then iterator will iterate
      > Iteration
        * Is the process of itrator iterating basically iteration of an item

      * Normally while iterating in for loop it iterates the value and keeps in the memory but dose not stores.
      * It keeps iterating an generating
      * Like "range" is a generator 
      ## Creating generator
      def gen(n):
          for i in range(n):
              yield i
      
      * YIELD - Is a generator and will generate on the fly 
      * RETURN - Function will return with the return statment nothing else it will do after that
      * PRINT - Will print it in the console

      Generator is used to save the main memory in the system.
      Ex. if you want to pull hundrades and thousands of data from a database but if the values you will use it only one at a time lormal looing way will keep all the data in the main memory. Rather incase of generator (yield), it will only donwload the generate the one value and when __next__() is called it will generate the next data.

# 31. Comprehensions
  ## List cmoprehension
  * Writing list looping shorter
  General way:

  ```sh
  ls = []
  for i in range(100):
      if i%3 == 0:
          ls.appened(i)
  ```

  * List Comprehension
  ls = [i for i in range(100) if i%3 == 0]

  ## Dictionary cmoprehension
  dict = {i:f"items{i}" for i in range(100) if i%100==0}
  
  * reverse dictionary

  dict = {value:key for key,value in dict.items()}

  ## Set cmoprehension
  * Set will have on duplicats and will be in {} bracket unlike dictionary set is not a key value pair
  set = {dress for dress in ["dress1", "dress2", "dress3", "dress1"]}

  ## Generator cmoprehension
  * Generator is such function in which we can yield, i.e, it is capable of generating but dose not gererate until we ask it to generate and we can gerate value on the fly and it will give the next value

  evens = (i for i in range(100) if i%2==0)

# 32. For with Else
  * For loop ends in 2 ways, Normal end of the index or break statement
  * Else works only when for loop ends normally

  ## When to use else in for loop
  for i in items:
    if i == <something_not_in_the_list>
      break
  else:
    print(f"Item {i} is not available")

  Result: will be else print statement becasue i == something not in the list
  but if i == some thing in the list then the obious the loop will break

# 33. Function Caching
  * Will cache/store the function result so that function dosenot require to run everytime.
  * It stores input and output value
  * Import the function caching 
  '''sh from functools import lru_cache ```

  * lru_cache is a decorator
  * use @lru_cache(maxsize=n) above the funtion
  * maxsize will store the last n times funtion called

# 34. Else & Finally in Try Except
  ## Finally
  * Finally is used after exception to execute code after finally either it executes try or exception, i.e, in any case finally should run
  * Finally is usually used for the code cleanup
  * 
  try:
    f = open("file_name.txt")
  except Exeption as e:
    print(e)
  finally:
    print("This code must run")

  ## Else
  * Else will not run if except executes but if try executes else will execute
  * That is either except or else one of them will run, so if except runs else will not and if except dose not then else will
  try:
    f = open("file_name.txt")
  except Exeption as e:
    print(e)
  else:
    print("Else runs if except did not run")
  finally:
    print("Finally will run always")

# 35. Coroutines In Python
  * Is used in such cases when a function takes time to initialise, may be fetching data or any time consumig action.
  * And once the intialisation is completed the same data can be used again and again
  * So in the above case coroutine is used to stre the value and run the further code in the function to process the initialised data
  * It is kind of generator functionality. In the yield in funtion we stored the whole value of the loop and use them by next
  * In this scenario we will use the yield to sotre the value in between the function and then use the same value to execute the futher code
  ```sh
  def searcher():
      import time
      # lets assume below is the task which consumes around 4 seconds
      book = "This is the contents of the book which the code took to download and read and it takes 4 secods for this example"
      time.sleep(4)

      #Below run the coroutines with infinite wile loop to store the data and do search on the above fetched time consuming data

      while True:
        text = (yield) # this is the yield of the above book
        if text in book:
            print("your text is in the book")
        else:
            print("your text is not in the book")
    
    search = searcher()
    print("Search strated")
    next(search)
    print("Now run the query")

    search.send("download")
  ```

# 36. OS Module
  * Used to interact with the system OS

  ```sh
  print(os.getcwd())
  os.chdir("~/")
  os.listdir()
  os.listdir('/path_of_dir/')
  os.mkdir("dir_name")
  os.makedirs("with/trailing/path")
  os.rename("filename", "new_filename")
  os.environ.get('HOME') or Path
  os.path.join("/dir_a/", "dir_b") > /dir_a/dir_b
  os.path.exists("/dir_path/") > boolean
  os.path.isfile("/dir_path/") > false
  os.path.isdir("/dir_path") > true

  ```
# 37. Requests module
  * Is used to interact with http requests
  * About requests in pypi https://pypi.org/project/requests/

# 38. Json Modules
  * 

  ## 
  * json.loads will parse the data and will create a json dictionary
  ```sh
  import json
  data = '{"var1":"libin", "var2":"tom"}'

  parsed = json.loads(data)
  print(parsed['var1'])
  ## above data is a string not dictionary and using the json.loads will parse the data to convert it to json

  json.load #find the differance
  
  data2 = {
    "channel_name": "codewithharry",
    "cars": ['bmw', "audi a8", "ferrari"],
    "fridge": ('roti',540),
    "allowed": True
  }

  l = json.dumps(data2) #json.dumps will convert the data to work javascrip data so that this data works in the browser
  
  #output
  {"channel_name": "codewithharry", "cars": ["bmw", "audi a8", "ferrari"], "fridge": ["roti", 540], "allowed": true}

  l_sort = json.dumps(data2, sort_keys=True)

  #Output
  {"allowed": true, "cars": ["bmw", "audi a8", "ferrari"], "channel_name": "codewithharry", "fridge": ["roti", 540]}
  ```

# 39. Pickle module
  * Is to pack the object for later use

  ```sh
  import pickle
  cars = ["audi", "bmw", "maruthi", "fite"]
  file = "file-name.pkl"
  file_object = open(file, 'wb')
  pickle.dump(cars, file_object)
  file_object.close()

  #In the above code created cars list object, then cretaed and opend a file in write binary mode, then pickle.dump cars object to that file.

  file = "file-name.pkl"
  file_object = open(file, 'rb')
  cars = pickle.load(file_object)
  print(cars)
  
  Output:
  ["audi", "bmw", "maruthi", "fite"]
  ```
# 40. Regular expression
  * Used to find a specific pattern of a string
  > import re
  * regular funtions in the re is
  ```findall, search, split, sub, finditer```
  * <strong>Findall</strong> : Return the string using the regex string pattern 
  * <strong>Search</strong> : Search dose the same as findall but dose <strong>matchobject</strong>
  * <strong>Split</strong> : 
  * <strong>Sub</strong> : 
  * <strong>Findall</strong> : 
  > <strong>RAWSTRING</strong> : using rawstring r"" will remove the escape charachter and prints the charachters as is
  ```sh print("Hello people \n in the world")
      output:
      Hello people
      in the world

      print(r"Hello people \n in the world")
      output:
      Hello people \n in the world
  ```

  ```sh
  patt = re.compiler(r'\d{5}-\d{4}')
  matches = patt.finditer(mystring)
  for match in matches:
      print(match)
  ```
  [List of Regular Expressions](https://sites.ualberta.ca/~kirchner/513/OpenOffice%20regular%20expression%20list.pdf)

# 41. Converting .py to .exe
  * Install the pyinstaller
  ```sh pip install pyinstaller ```
  * Conver the python file to exe
  ```sh pyinstaller program_filename.py```
  >This will now convert the program to exe file

  * Make the same in one file
  ```sh pyinstaller --onefile program_filename.py```

# 42. Raise
  * Is a built in keyword
  * Is used to raise the exception to not run the code any futher untill the exception is rectified
  * [Python exceptions list ](https://www.tutorialspoint.com/python/python_exceptions.htm#:~:text=What%20is%20Exception%3F,object%20that%20represents%20an%20error.)
  ```sh
  if int(b)==0:
    raise ZeroFivisionError("b is 0 so stopping")
  
  -----
  if a.isnumeric():
    raise Exception("Numbers are not allowed")

  c = input("Enter your name :")
  try:
    print(a)
  except Exceptions as e:
    if c == "some_specific_string":
        raise ValueError("String is not allowed")
    print("Exception handled")
  ```

# 43. Differance between is and ==
  * == > Value equality > Two objects has same value
  * is > reference equality > Two references refer to the same object
  ```sh
  a = [1,2,3]
  b = a

  a == b > True # A and B is has same value
  a is b > True # A and B is fereing the same object

  c = a[:] # C is now copy of A

  a == c > True # A and C both has same value
  a is c > False # A and C is not refering the same object
  ```

# 44. Python V 2.x and 3.x 
  * [Watch Harry video for more details](https://www.youtube.com/watch?v=n39cxF9bQIE&list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME&index=92)

# 45. Command line argument
  * Usin this we can parse argument after the script in the command line
  
  ```sh
  import argparse
  import sys

  def calc(args):
      if args.o=='add':
          return args.x + args.y
      elif args.o=='sub':
          return args.x - args.y
      elif args.o=='mul':
          return args.x * args.y
      elif args.o=='div':
          return args.x / args.y
      else:
          print("Somethign worng. --help for mode details")

  if __name__ == '__main__'
      parser = argparse.ArgumentParser()
      parser.add_argument('--x', type=float, default=1.0, help="Enter a number")
      parser.add_argument('--y', type=float, default=1.0, help="Enter another number")
      parser.add_argument('--o', type=str, default=1.0, help="Enter the operation [add, sub, mul, div]")

      args = parser.parse_arg()
      sys.stdout.write(str(clac(args)))
  ```

# 46. Creating python library/package
  * Create prject directory
  * Inside project directory, create another directory for the package, readme file, licence file and setup.py file
  * Add the below code in setup.py
  ```sh
  from setuptools import setup
  setup(name="package_name"),
  version="1.0",
  description="this is a short intro description",
  long_description="this is a long detailed description",
  author="Name_of_the_authour",
  packages=["package_name"],
  install_requires=["name_of_the_dependency_packages"]
  )
  ```
  * Create a __init__.py file in the package directory and add your code
  ```sh
  class Someclass:
      def __init__(self):
          print("constructor created")
      def somefuntion(arg):
          print("This is my package)
          return something
  ```
  * pip install wheel
  ```sh python3 -m pip install wheel```
  * Make the wheel of the new package using wheel
  ```sh
  # Change directory to the package root directory

  python3 setup.py bdist_wheel
  ```
  > This will build the package and creates new directory
  > Change director to dist
  * Install package using the whl file
  ```sh pip install package_name-1.0xxxx.whl```

  * Import the new package in the python code
  ```import package_name```
  > Each time any new updates in the package, change the version and run the setup again


-----------
# Date time module
```sh
from datetime import date

today = date.today()

# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)

# Textual month, day and year	
d2 = today.strftime("%B %d, %Y")
print("d2 =", d2)

# mm/dd/y
d3 = today.strftime("%m/%d/%y")
print("d3 =", d3)

# Month abbreviation, day and year	
d4 = today.strftime("%b-%d-%Y")
print("d4 =", d4)
```


# Important Python Modules for DevOps Automation

## (os module)[https://docs.python.org/3/library/os.html]
os.ctermid()
Return the filename corresponding to the controlling terminal of the process.

os.environ

os.chdir(path)
os.fchdir(fd)
os.getcwd()

os.fspath(path)
Return the file system representation of the path.

os.getegid()
Return the effective group id of the current process. This corresponds to the “set id” bit on the file being executed in the current process.

os.getgid()
Return the real group id of the current process.

os.geteuid()
Return the current process’s effective user id.

os.getlogin()
Return the name of the user logged in on the controlling terminal of the process.


## [platform](https://docs.python.org/3/library/platform.html)
platform.mac_ver()
('10.14.6', ('', '', ''), 'x86_64')

platform.node()
'Macbooks-MacBook-Air.local'

platform.processor()
'i386'
## [subprocess](https://docs.python.org/3/library/subprocess.html)
Learn more on this

## [sys](https://docs.python.org/3/library/sys.html)
This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. It is always available.


## psutil
## re (Regular Expression)
## scapy
## Requests and urllib3
## logging
## getpass
## boto3
## paramiko
## JSON
## PyYAML
## pandas: One of the best data science frameworks. However, it is very useful for DevOps automation tasks dealing with CSV files.
## smtplib 
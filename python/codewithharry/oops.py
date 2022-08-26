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
    print("This employee is not in the database. Please check the spelling and search again.")
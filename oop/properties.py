class Salary:

    def __init__(self) -> None:
        # self.__salary = salary
        self.__salary = None


    # we use @ property decorator for "get_salary" function 
    @property
    def salary(self):
        return self.__salary 
    
    # we use "variablename.setter" decorator to set the salary, it is same as creating a setter function
    @salary.setter
    def salary(self,salaryValue):
        self.__salary = salaryValue

    
    @salary.deleter
    def salary(self):
        del self.__salary


sr = Salary()
print(sr.salary)

sr.salary = 6000
print(sr.salary)
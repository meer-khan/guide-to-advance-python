
# Properties of Aggregation: 
# 1- The relationship between associated classes in aggregation in defined by the keyword "has-a"
    # Employee has a salary 
# 2- Associated classes has uni directional assosication, only the salary can be passed to employee and not the other way around
# 3- Both objects are indenpendent, if one object dies then other stays e.g. if employee object deleted then salary object remains
    # Both objects can survive individually 



class Salary:
    def __init__(self, pay, bonus) -> None:
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return self.pay*12 + self.bonus


class Employee:
    def __init__(self, name, age, salary) -> None:
        self.name = name
        self.age = age
        self.salary_obj = salary

    def total_salary(self):
        return self.salary_obj.annual_salary()
    
salary = Salary( 180000, 0)
emp = Employee("Khan", "24",salary)

print(emp.total_salary())
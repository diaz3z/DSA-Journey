# Access Modifiers in Python
# Public = variable
# Protected = _variable
# Private = __variable

# class Person:
#     def __init__(self, name, age):
#         self.name = name        # public
#         self._age = age         # protected
#         self.__salary = 50000   # private

#     def show_salary(self):
#         return self.__salary

# p = Person("Alice", 25)

# print(p.name)        # OK
# print(p._age)        # Allowed (not recommended)
# # print(p.__salary)  # Error
# print(p.show_salary())


class Employee:
    def __init__(self):
        self.name = "John"
        self._department = "HR"
        self.__salary = 60000
    
    def get_salary(self):
        return self.__salary
emp = Employee()
print(emp.name)            # Public access
print(emp._department)     # Protected access (not recommended)
print(emp.get_salary())    # Accessing private variable via method
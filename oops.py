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


# class Employee:
#     def __init__(self):
#         self.name = "John"
#         self._department = "HR"
#         self.__salary = 60000
    
#     def get_salary(self):
#         return self.__salary
# emp = Employee()
# print(emp.name)            # Public access
# print(emp._department)     # Protected access (not recommended)
# print(emp.get_salary())    # Accessing private variable via method


# Getters and Setters
# Concept, Used to control access to private variables.

# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance
    
#     @property
#     def get_balance(self):
#         self.__balance

#     @get_balance.setter
#     def set_balance(self, __balance):
#         if __balance < 0:
#             print("Value is negative cannot process!!")
#         else:
#             print(__balance)

# amount = BankAccount(1000)
# print(amount.get_balance)
# amount.set_balance = -154
# # print(amount.set_balance)

# Encapsulation
# Hiding internal data in the class and only exposing only necessary.

# class zaid:
#     def __init__(self, age, salary):
#         self.age = age
#         self.__salary = salary


# diaz = zaid(23, 600)
# print(diaz.age)
# print(diaz.__salary)


# class mobile:
#     def __init__(self,brand,battery):
#         self.brand = brand
#         self.__batery = battery

# ar = mobile("samsung", "exide")
# print(ar.brand)
# print(ar.__batery)

















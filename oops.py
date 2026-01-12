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



# class Laptop:
#     def __init__(self, brand, price):
#         self. brand = brand
#         self.price = price
#     def __str__(self):
#         return f"Lapton Brand: {self.brand} and Laptop price: {self.price}"

# a = Laptop("HP", "75K")
# print(a.brand, a.price)
# print(a)

# import copy

# original = [[1, 2], [3, 4]]

# shallow = copy.copy(original)
# deep = copy.deepcopy(original)

# original[0][0] = 99

# print(shallow)  # affected
# print(deep)     # not affected

# import copy
# orig_arr = [[43, 56],[89, 23]]

# shallow = copy.copy(orig_arr)
# deep_copy = copy.deepcopy(orig_arr)

# orig_arr[0][1]= 0
# print(shallow)
# print(deep_copy)

# Destructors

# class notting:
#     def __init__(self):
#         print("object created")
        
#     def __del__(self):
#         print("Object deleted")
# obj = notting()
# del obj


# Inheritance

# class Vehicle:
#     def speed(self):
#         print("300km per hour")

# class Car(Vehicle):
#     def brand(self):
#         print("Bugatti!!!!!")

# obj = Car()
# obj.speed()
# obj.brand()

# single level inheritance and multi level inheritance

# class Person:
#     def name(self):
#         print("name of person")

# class Employee(Person):
#     def status(self):
#         print("Employee status of person")

# class Manager(Employee):
#     def designation(self):
#         print("Designation of the employee")

# obj = Manager()
# obj.name()
# obj.status()
# obj.designation()





# class Animal:
#     def sound(self):
#         return "Some generic sound"

# class Dog(Animal):
#     def sound(self):
#         return "Bark"

# class Cat(Animal):
#     def sound(self):
#         return "Meow"

# # Polymorphic behavior
# animals = [Dog(), Cat(), Animal()]
# for animal in animals:
#     print(animal.sound())



# class Circle:
#     def area(self):
#         print(" (pi * radius) ** 2")
    
# class Rectangle:
#     def area(self):
#         print("lenght * breadth")


# obj = (Circle(), Rectangle())

# for object in obj:
#     object.area()





class Parent:
    def show(self):
        print("Parent")

class Child(Parent):
    def show(self):
        print("Child")

obj = (Parent(), Child())
for object in obj:
    object.show()








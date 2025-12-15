# a = list("abc")
# a = "aBc"
# print(a)  # ['a', 'b', 'c']

# b = tuple([1, 2, 3])
# b = tuple("abc")
# print(b)  # (1, 2, 3)

# c = dict(a =1, b=3)
# c = dict([('a', 1), ('b', 2)])
# print(c)


raw = input("Enter age ")
try:
    age = int(raw)
except ValueError:
    age = None
print(age)

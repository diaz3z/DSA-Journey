# # num = [10, 20, 30]

# # for i, val in enumerate(num):
# #     print(i, val)


# names = ['John', 'Jane', 'Bob', 'Alice']

# for i, name in enumerate(names):
#     print(i, name)

# for i in range(5):
#     print(i)

# for i in range(20):
#     print(i)

# for i in range(0, 20, 2):
#     print(i, end=" ")


# a = [1, 2, 4]
# b = [10, 30, 20]

# for x, y in zip(a, b):
#     print(x, y)
#     # print(f"Sum{x, y} = {x+y}")

# for x in reversed([1, 2, 3]):
#     print(x, end=" ")

# x = "zaid"
# for i in reversed(x):
#     print(i, end="")


# # a = list(map(int, input("Enter 3 numbers: ").split()))
# num = input("Enter numbers: ").split()
# # print(len(a))
# print(min(num))

# num = [10, 20, 5, 30, 15]
# print(max(num))

# sum of all even numbers from 0 to 100

# total = []
# for i in range(0, 101):
#     if i % 2 == 0 :
#         # total += i
#         total.append(i)
# print(sum(total))
# # print(total)

# words = ['apple','cherry', 'banana']
# alphabets = ['b', 'a', 'd', 'c']
# # print(sorted(alphabets))
# # print(sorted(words))
# print(sorted(alphabets, reverse=True))


# def myfunc(n):
#   return abs(10-n)

# a = (5, 3, 1, 11, 2, 12, 17)
# x = sorted(a, key=myfunc)
# print(x)

# a = ("Jenifer", "Sally", "Jane")
# x = sorted(a, key=len)
# print(x)

# temp = [1, 45, -2, 46]
# print(any(t<0 for t in temp))

# temp = [1, 45, 2, 46]
# print(all(t % 2 == 0 for t in temp))
# print(any(t % 2 == 0 for t in temp))

# sent = "This is a sample sentence"
# print(set(sent.split()))

# temnp = "thisisimagevisionai"
# print(set(temnp))

# sentence = "The quick brown fox jumps over the lazy dog"
# unique_words = set(sentence.split())
# print(unique_words)

# sq = []
# for i in range(1, 11):
#     sq.append(i**2)
# print(sq)

# stack = []

# stack.append(1)
# stack.append(2)
# stack.append(3)

# print(stack)
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack)


# list1 = [1, 2, 3, 4, 5]
# list2 = ['a', 'b', 'c', 'd', 'e']
# list1.extend(list2)
# print(list1)

# a = 10
# b = 13
# # dif = abs(a - b)
# dif = a - b
# print(dif)

# print(pow(7,5))

# int1 = 10
# int2 = 3

# print(divmod(int1, int2))  # (3, 1)

# string1 = "Hello"
# for i in string1:
#     print(ord(i), end=" ")  # 72 101 108 108 111


# for i in range(97, 103):
#     print(chr(i), end=" ")  # a b c d e f

# sent = "The quick brown fox"
# # print(sent.split())
# for i in sent.split():
#     print(i)



# char = ['b', 'r', 'o', 'w', 'n']
# print(''.join(char))  # brown

# nums = [10, 20, 30]
# it = iter(nums)
# print(next(it))  # 10


# d1 = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964,
#     "year": 2020
# }
# # print(d1["brand"])
# print(len(d1))

d2 = dict(brand="Ford", model="Mustang", year=1964)
print(d2)
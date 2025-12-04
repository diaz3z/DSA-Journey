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

# sentence = "The quick brown fox jumps over the lazy dog"
# unique_words = set(sentence.split())
# print(unique_words)


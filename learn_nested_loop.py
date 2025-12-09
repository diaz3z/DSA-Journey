# for i in range(2, 4):
#     for j in range(1, 11):
#         print(f"{i} times {j}: {i*j}")


# # Initialize list1 and list2
# # with some strings
# list1 = ['I am ', 'You are ']
# list2 = ['healthy', 'fine', 'geek']
# list3 = ['chetan', 'peddabuddi', 'elon']

list1 = [1, 2, 3]
list2 = [5, 6, 7]
list3 = [ 9, 10, 11]


for i in list1:
    print(f"Printing first loop {i}")
    for j in list2:
        # print(f"Printing second loop: {j}")
        print(f"printing first and second loop together: {i, j}")
        for k in list3:
            # print(f"Printing third loop: {k}")
            print(f"printing first, second and third loop together: {i, j, k}")



# # Store length of list2 in list2_size
# list2_size = len(list2)

# # Running outer for loop to
# # iterate through a list1.
# for item in list1:
  
#     # Printing outside inner loop
#     print("start outer for loop ")
#     # Initialize counter i with 0
#     i = 0
#     # Running inner While loop to
#     # iterate through a list2.
#     while(i < list2_size):
      
#         # Printing inside inner loop
#         print(item, list2[i])
#         # Incrementing the value of i
#         i = i+1
#     # Printing outside inner loop
#     print("end for loop ")
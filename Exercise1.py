# Напишите программу, которая на вход принимает 5 чисел (можно списком) и находит максимальное из них. 

# my_list = [4, 5, 32, 9, 910]
# max_number = my_list[0]
# i = 0
# while i < len(my_list):
#     if max_number < my_list[i]:
#         max_number = my_list[i]
#     i += 1

# print(f'{max_number}')



# Напишите программу, которая на вход принимает 5 чисел (можно списком) и находит максимальное из них

my_list = [3, 5, 33, 95, 85]
max_number = my_list[0]
i = 0
while i < len(my_list):
    if max_number < my_list[i]:
        max_number = my_list[i]
    i += 1

print(f'{max_number}')


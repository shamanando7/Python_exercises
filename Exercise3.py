# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
# Примеры:
# 6,78 -> 7
# 5 -> нет
# 0,34 -> 3

# import math
# a = float(input('Введите число '))
# result_a =  a*10 % 10
# print(f'{int(result_a)}')


# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

a = float(input('Введите число '))
result_a = a * 10 % 10
print(f'{int(result_a)}')


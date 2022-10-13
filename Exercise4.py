# Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

# a = int(input('Введите число '))

# if (a % 5 == 0 and a % 10 == 0 or a % 15 == 0) and not (a % 30 == 0):
#     print(f'кратно ')
# else:
#     print(f'не кратно')
 


Number = int(input("Введите число: "))

if Number%10 == 0 or Number %15 == 0 and Number%30 != 0:
    print("Верно") 
else:
    print("Не верно")
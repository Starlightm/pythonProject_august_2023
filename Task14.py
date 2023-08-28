# Задача 14: Требуется вывести все целые степени двойки
# (т.е. числа вида 2k), не превосходящие числа N.
#
# 10 -> 1 2 4 8
N = int(input("Введите натуральное число: "))
exponent = 0
result = 1
while result < N:
    print(f"2 ^ {exponent} = {result}")
    exponent += 1
    result = 2**exponent

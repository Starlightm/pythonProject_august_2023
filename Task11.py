# Задача No11.
# Дано натуральное число A > 1.
# Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что φ(n)=A.
# Если А не является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

#0, 1, 1, 2, 3, 5

A = 5
if A < 0:
    print(-1)
elif A == 0:
    print(1)
else:
    next = 1
    previous = 0

    i = 0

    while i <= A:
        previous, next = next, previous + next
        i += 1

    print(i)

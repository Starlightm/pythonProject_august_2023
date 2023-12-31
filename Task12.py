# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.

# 4 4 -> 2 2
# 5 6 -> 2 3

import random
import math

hid_nums = (random.randint(1,1000), random.randint(1,1000))

nums_sum = hid_nums[0] + hid_nums[1]
nums_product = hid_nums[0] * hid_nums[1]

print(f"Brother's numbers: {hid_nums[0], hid_nums[1]}")
print(f"The sum of two numbers is {nums_sum}, the product is {nums_product}.")
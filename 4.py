"""
Напишите программу, которая запрашивает целое число, назовем его X, и затем находит сумму первых X натуральных чисел.
Так, если X = 5, то искомая сумма 1 + 2 + 3 + 4 + 5 = 15.
"""

x = int(input("введите X\n"))
summ = 0
for i in range(x+1):
    summ += i

print(summ)

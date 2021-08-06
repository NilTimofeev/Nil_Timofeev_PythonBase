# Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти
# чётные числа от 100 до 1000 (включая границы). Нужно получить результат вычисления произведения
# всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce

new_list = [num for num in range(100, 1001) if num % 2 == 0]
print(new_list)
print(reduce(lambda x, y: x * y, new_list))

#Реализовать два небольших скрипта:
# итератор, генерирующий целые числа, начиная с указанного;
# итератор, повторяющий элементы некоторого списка, определённого заранее.

from itertools import count, cycle

for val in count(10):
    if val > 15:
        break
    else:
        print(val)

i = 0
for val in cycle(['q', 'w', 'e', 'r']):
    if i > 5:
        break
    else:
        print(val)
        i += 1

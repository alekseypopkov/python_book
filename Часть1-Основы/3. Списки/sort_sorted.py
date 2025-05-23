# 1. Упорядочение списка 
 
# 1.1. Постоянная сортировка списка с помощью метода sort()
# Метод sort() изменяет порядок элементов в списке навсегда. 
# Названия машин располагаются в алфавитном порядке, и вернуться 
# к исходному порядку уже не удастся:

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# Список также можно отсортировать в обратном алфавитном порядке; 
# для этого методу sort() следует передать аргумент reverse=True.
# И снова порядок элементов изменяется навсегда:

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

# 1.2. Временная сортировка списка с помощью функции sorted()

# Чтобы сохранить исходный порядок элементов списка, но временно представить 
# их в отсортированном порядке, можно воспользоваться функцией sorted().
# Она позволяет представить список в определенном порядке, но не изменяет 
# фактический порядок элементов в списке.

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

# Функции также можно передать аргумент reverse=True, 
# чтобы список был представлен в порядке, обратном алфавитному.

# ПРИМЕЧАНИЕ
# Сортировка списка по алфавиту немного усложняется, если не все значения записаны
# в нижнем регистре. При определении порядка сортировки появляются разные способы
# интерпретации прописных букв, и точное определение порядка может оказаться более
# сложной задачей, чем нам хотелось бы в текущий момент. Однако большинство подходов
# к сортировке строятся на принципах, описанных в этом подразделе.

# 1.3 Вывод списка в обратном порядке
# 
# Чтобы переставить элементы списка в обратном порядке, используйте метод
# reverse(). Например, если список машин первоначально хранился в хронологическом порядке, 
# соответствующем дате приобретения, то элементы можно переставить в обратном хронологическом порядке:

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)


# Обратите внимание: метод reverse() не сортирует элементы в обратном алфавитном порядке, 
# а просто меняет порядок списка на обратный:

['bmw', 'audi', 'toyota', 'subaru']
['subaru', 'toyota', 'audi', 'bmw']
# Метод reverse() изменяет порядок элементов навсегда, но вы можете легко вернуться к исходному порядку, 
# снова применив reverse() к обратному списку.

#Определение длины списка

# Быстро определить длину списка позволяет функция len(). Список в нашем примере состоит 
# из четырех элементов, поэтому его длина равна 4:

print(len(cars))
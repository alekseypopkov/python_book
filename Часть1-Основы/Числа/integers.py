print()
print("""Целые числа
В Python с целыми числами можно выполнять операции сложения (+), вычитания (–), умножения (*) и деления (/).""")
print()
a = 2 + 3
print("a = 2 + 3 \n\ta =", a)
b = 3 - 2
print("b = 3 - 2 \n\tb =", b)
c = 2 * 3
print("c = 2 * 3 \n\tc =", c)
d = 3 / 2
print("d = 3 / 2 \n\td =", d)
print()

print("""В терминальном сеансе Python просто возвращает результат операции. Для пред-
ставления операции возведения в степень в Python используется сдвоенный знак
умножения:""")
print()
a = 3 ** 2
print("a = 3 ** 2 \n\ta =", a)
b = 3 ** 3
print("b = 3 ** 3 \n\tb =", b)
c = 10 ** 6
print("c = 10 ** 6 \n\tc =", c)
print()

print("""Кроме того, в Python существует определенный порядок операций, что позволяет
# использовать несколько операций в одном выражении. Круглые скобки приме-
# няются для изменения порядка операций, чтобы выражение могло вычисляться
# в нужном порядке. Пример:""")
print()
a = 2 + 3*4
print("a = 2 + 3*4 \n\ta =", a)
b = (2 + 3) * 4
print("b = (2 + 3) * 4 \n\tb =", b)
print()
print('''Пробелы в этих примерах не влияют на то, как Python вычисляет выражения; они
просто помогают быстрее найти приоритетные операции при чтении кода.''')
print()
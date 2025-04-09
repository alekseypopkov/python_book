# Удаление префиксов

# URL с префиксом https://. Попробуем удалить этот префикс, чтобы работать только с той частью URL, которую 
# пользователи должны ввести в адресной строке. Вот как это сделать:
nostarch_url = 'https://nostarch.com'
nostarch_url.removeprefix('https://')
'nostarch.com'

#Укажите имя переменной, затем точку и метод removeprefix(). В круглых скобках
# укажите префикс, который нужно удалить из исходной строки.
# Как и в случае удаления пробельных символов, метод removeprefix() не изменяет
# исходную строку. Если вы хотите сохранить в переменной новое значение с удаленным
#  префиксом, то присвойте его либо исходной, либо новой переменной:

simple_url = nostarch_url.removeprefix('https://')
print(simple_url)
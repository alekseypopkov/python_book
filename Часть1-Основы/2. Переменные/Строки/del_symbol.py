# Удаление пробельных символов

# Чтобы убедиться в том, что у правого края (в конце) строки нет пробельных 
# символов, вызовите метод rstrip():

favorite_language = 'python    '
a = 1
print(favorite_language, a)
print()
print(favorite_language.rstrip(), a) # удаление временное — если вы снова запросите значение favorite_language, 
print()                                     #то увидите, что строка совпадает с исходной, включая лишний пробельный символ

# Чтобы навсегда удалить пробельный символ из строки, следует записать 
# исправленное значение обратно в переменную:

favorite_language = 'python        '
a = 2
favorite_language = favorite_language.rstrip()
print(favorite_language, a)

# Пробельные символы также можно удалить у левого края (в начале) строки с помощью метода lstrip(), 
# а метод strip() удаляет пробельные символы с обоих концов:

favorite_language = ' python '
favorite_language.rstrip()
' python'

favorite_language.lstrip()
'python '

favorite_language.strip()
'python'
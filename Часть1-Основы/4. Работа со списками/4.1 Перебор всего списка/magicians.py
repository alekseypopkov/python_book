# Все начинается с определения списка. 
# Затем определяется цикл for.
# С помощью этой строки Python получает указание — взять очередное имя из списка
# и сохранить его в переменной magician. Далее выводится имя, только что сохраненное 
# в переменной magician. Затем строки повторяются для каждого имени в списке.
# Этот код можно описать так: «Для каждого фокусника в списке вывести его имя».
# Результат представляет собой простой перечень имен из списка:
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
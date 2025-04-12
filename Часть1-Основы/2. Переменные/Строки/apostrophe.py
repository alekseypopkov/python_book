# Предотвращение синтаксических ошибок в строках

#Разберемся, как же правильно использовать одиночные или двойные кавычки.
#Сохраните следующую программу как файл apostrophe.py и запустите ее:

message = "One of Python's strengths is its diverse community." # Апостроф находится в строке, заключенной в двойные кавычки, 
                                                                #так что у интерпретатора Python не возникает проблем с правильным пониманием строки.
print(message)

#Однако при использовании одиночных кавычек Python не сможет определить, где
#должна заканчиваться строка:

# message = 'One of Python's strengths is its diverse community.'  - SyntaxError: unterminated string literal (detected at line ___)
#print(message)
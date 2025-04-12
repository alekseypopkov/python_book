first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
print()

# С помощью f-строк можно выполнять много интересных действий. Например,
# составлять сложные сообщения с информацией, хранящейся в переменных.

print(f"Hello, {full_name.title()}!")
print()

#Кроме того, f-строки можно использовать для составления сообщения, которое 
# затем сохраняется в переменной:

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)

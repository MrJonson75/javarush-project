# Доступ запрещен

# Напишите программу, которая запрашивает у пользователя имя пользователя и пароль.
# Если имя пользователя равно "admin" и пароль равен "1234", программа должна вывести
# сообщение "Доступ разрешен".
# В противном случае программа должна вывести сообщение "Доступ запрещен".

# Напишите тут ваш код
login = input("Введите логин: ")
password = input("Введите пароль: ")

if login == "admin" and password == "1234":
    print("Доступ разрешен")
else:
    print("Доступ запрещен")
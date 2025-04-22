# Хеширование паролей

# Напишите программу для хеширования паролей.
# Ваша задача — создать функцию, которая принимает строку пароля и возвращает его хеш-значение.
import hashlib
def hash_password(password: str) -> str:
# Напишите тут ваш код
    return hashlib.sha256(password.encode()).hexdigest()


# Пример использования:
password = "my_secure_password"
hashed_password = hash_password(password)
print(hashed_password)



# Авторизация

# Напишите программу имитации логина пользователей.
# Программа должна содержать функцию login(email, password)
# и register(email, password).
# При регистрации пользователя нужно вызвать функцию register и добавить
# пользователя в список пользователей.
# Вместо пароля нужно хранить его hash.
# При логине пользователя нужно вызвать функцию login где проверить, что hash
# пароля совпадает с одним из сохраненных хешей.

import hashlib
users = {}

def hash_password(password):
# Напишите тут ваш код
    return hashlib.sha256(password.encode()).hexdigest()

def register(email, password):
# Напишите тут ваш код
    users[email] = hash_password(password)

def login(email, password):
# Напишите тут ваш код
    if email in users:
        return hash_password(password) == users[email]

# Example usage
register("user@example.com", "securepassword123")
login("user@example.com", "securepassword123")
login("user@example.com", "wrongpassword")
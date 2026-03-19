users = {
    "joao": {"password": "123456"},
    "maria": {"password": "abcdef"}
}

user_input = input("Write the username: ")
password_input = input("Write the password: ")

if user_input in users and users[user_input]["password"] == password_input:
    print("Login successful!")

else:
    print("Wrong username or password, contact the administrator.")
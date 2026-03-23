users = {
    "joao": {"password": "123456", "role": "user"},
    "maria": {"password": "abcdef", "role": "admin"}
}

user_input = input("Write the username: ")
password_input = input("Write the password: ")

if user_input in users and users[user_input]["password"] == password_input:
    print("Login successful!")

    role = users[user_input]["role"]

    if role == "admin":
        print("You have owner privileges")
    else:
        print("You have writing privileges")

else:
    print("Wrong username or password, contact the administrator.")
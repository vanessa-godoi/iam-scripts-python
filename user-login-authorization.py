users = {
    "joao": {"password": "123456", "role": "writer"},
    "maria": {"password": "abcdef", "role": "admin"},
    "carlos": {"password": "999999", "role": "viewer"}
}

user_input = input("Write the username: ")
password_input = input("Write the password: ")

if user_input in users and users[user_input]["password"] == password_input:
    print("Login successful!")

    role = users[user_input]["role"]

    if role == "admin":
        print("You have owner privileges")
    elif role == "writer":
        print("You have writing privileges")
    elif role == "viewer":
        print("You have viewer privileges")

    else:
        print("You don't have permissions attached")

else:
    print("Wrong username or password, contact the administrator.")
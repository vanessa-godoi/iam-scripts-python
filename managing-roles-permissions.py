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

    action = input ("Choose an action ➝ read | write | delete: ")

    if action not in ["read", "write", "delete"]:
        print("Invalid action, try again or contact the administrator.")

    elif role == "admin":
        print("Access allowed")

    elif role == "writer":
        if action == "read" or action == "write":
            print("Access allowed")
        else:
            print("Access denied")

    elif role == "viewer":
        if action == "read":
            print("Access allowed")
        else:
            print("Access denied")

else:
    print("Wrong username or password, try again or contact the administrator.")
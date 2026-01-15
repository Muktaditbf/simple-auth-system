pass_dictionary = {'user1': '12345', 'nur': 'hello', 'tan':'1234'}

# 1. Ask for Username
username = input("Enter Username: ")

# 2. Check if User Exists
if username in pass_dictionary:
    # 3. If yes, Ask for Password
    password = input("Enter Password: ")

    # 4. Check if Password Matches the one in Dictionary
    if password == pass_dictionary[username]:
        print("You got it! Access Granted.")
    else:
        print("Wrong password.")
else:
    print("Get lost (User not found)")
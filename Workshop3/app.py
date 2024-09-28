from donations_pkg.homepage import show_homepage
from donations_pkg.user import login
from donations_pkg.user import register
from donations_pkg.homepage import donate
from donations_pkg.homepage import show_donations


database = {"admin": "password123"}
donations = []
authorized_user = ""

show_homepage()
if authorized_user == "":
    print("You must be logged in to donate.")
else:
    print(f"Logged in as: {authorized_user}")

while True:
    user_choice = input("Choose an option: ")
    if user_choice == "1":
        print("\n")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        print("\n")
        authorized_user = login(database, username, password)
    elif user_choice == "2":
        print("\n")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        authorized_user = register(database, username)
        if authorized_user != "":
            database[username] = password
            print(f"User '{username}' has been successfully registered.")
    elif user_choice == "3":
        if authorized_user == "":
            print("You are not logged in.")
        else:
            print("\n")
            donation_string = donate(authorized_user)
            donations.append(donation_string)
            print("\n")
    elif user_choice == "4":
        show_donations(donations)
    elif user_choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option.")

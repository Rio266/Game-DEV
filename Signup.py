username = ""
password = ""
print("=== WELCOME TO THE SIGN UP PROJECT ===")
while True:
    options = input("\nWhat action would you like to perform? \n1. Sign Up \n2. Sign In \n3. Reset Password \n4. Exit\n")
    if options == "1":
        username_counter = 0
        password_counter = 0
        while username_counter < 3: 
            username = input("\nWhat would you like your username to be? ").strip()
            if len(username) >= 3:
                print("/username is valid")
                break
            elif len(username) < 3:
                 print("/username has to have at least 3 letters")
                 username_counter += 1
                 continue
        else:
            print("/username counter exceeded limit")
            print("/redirecting to menu")
            continue
        while password_counter < 3:
            password = input("\nWhat would you like your password to be? ")
            number = False
            upper = False
            for i in password:
                if i.isdigit():
                    number = True
                if i.isupper():
                    upper = True
            if len(password) >= 3 and number and upper:
                print("/password is valid")
            else:
                print("\n=== Password Rules ===")
                print("/password must be at least 3 characters")
                print("/password must contain an uppercase letter")
                print("/password must contain a number")
                password_counter += 1
                continue
            confirmpassword = input("\nPlease confirm your password: ")
            if password == confirmpassword:
                print("/both passwords match")
                print("/information is stored")
                break
            else:
                print("/passwords do not match")
                password_counter += 1
                continue
        else:
            print("/password counter exceeded limit")
            print("/redirecting to menu")
            continue
    elif options == "2":
        username_counter = 0
        password_counter = 0
        while username_counter < 3:
            username_requested = input("\nWhat is your username? ")
            if username == username_requested:
                print("/username successful")
                break
            else:
                print("/username unsuccessful")
                username_counter += 1
                continue
        else:
            print("/username counter limit exceeded")
            print("/redirecting to menu")
            continue
        while password_counter < 3:
            password_requested = input("\nWhat is your password? ")
            if password == password_requested:
                print("/password successful")
                break
            else:
                print("/password unsuccessful")
                password_counter += 1
                continue
        else:
            print("/username counter limit exceeded")
            print("/redirecting to menu")
            continue
    elif options == "3":
        while True:
            username_reset = input("\nWhat is your username? ")
            if username == username_reset:
                print("/username found")
                break
            else:
                print("/username not found")
                continue
        while True:
            password_reset = input("\nWhat password would you like to add? ")
            password = password_reset
            print("/password changed successfully")
            break
    elif options == "4":
        print("\nThank you for using the Sign Up Project \nGoodbye.")
        exit()
    else:
        print("\nPlease choose a valid option below.")
        continue
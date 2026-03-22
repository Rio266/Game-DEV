print("=== WELCOME TO THE CALCULATOR ===")
history = []
while True:
    while True:
        number_one = input("Choose First Number: \n").strip()
        try:
            a = float(number_one)
            break
        except ValueError:
            print("Please enter a valid number. \n")
            continue
    while True:
        number_two = input("Choose Second Number: \n").strip()
        try:
            b = float(number_two)
            break
        except ValueError:
            print("Please enter a valid number. \n")
            continue
    while True:
        operation = input("What is your operation? \n 1. + 2. - 3. * 4. / \n").strip()
        if operation == "+" or operation == "1":
            answer = a + b
            print("The answer is {}.".format(answer))
            break
        elif operation == "-" or operation == "2":
            answer = a - b
            print("The answer is {}.".format(answer))
            break
        elif operation == "*" or operation == "3":
            answer = a * b
            print("The answer is {}.".format(answer))
            break
        elif operation == "/" or operation == "4":
            if b == 0:
                answer = "Infinity"
            else:
                answer = a / b
            print("The answer is {}.".format(answer))
            break
        else:
            print("Please select a valid operation. \n 1. + 2. - 3. * 4. / \n")
    while True:
        repeat = input("Would you like to do another calculation? \n").strip().lower()
        if repeat == "yes":
            break
        elif repeat == "no":
            print("Thank you for using the calculator.")
            break
            break  
        else:
            print("Please choose either Yes or No.")
            continue
        continue
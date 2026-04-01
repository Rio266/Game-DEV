from datetime import datetime

GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RED = "\033[91m"
RESET = "\033[0m"

print(f"{GREEN}=== WELCOME TO THE CALCULATOR ==={RESET}")
print(f"{CYAN}Type 'help' for usage, 'history' to show previous calculations, 'exit' to quit.{RESET}")
history = []
def Help():
    while True:
        if operation == "Help":
            help_choice = input(" \n=== Help === \n1. About \n2. How to Use \n3. Common Issues \n'e' to exit help \n").strip().lower()
            if help_choice == "1" or help_choice == "about":
                print("= About =")
                print("+ This calculator is a simple project where you can add, subtract, multiply or divide nummbers.")
                print("+ The project supports integer and decimal values.")
                print("+ Version 1.3, new version to support help and history.")
            elif help_choice == "2" or help_choice == "howtouse":
                print("= Usage =")
                print("+ Enter first number")
                print("+ Enter second number")
                print("+ Enter chosen operation")
                print("+ Answer will be shown")
            elif help_choice == "3" or help_choice == "commonissues":
                print("= Common Issues")
                print("+ Division by 0 is not allowed")
                print("+ Invalid inputs are shown when you have to repeat step")
                print("+ Fix invalid inputs by reading suggested fixes")
            elif help_choice == "e":
                break
            else:
                print("Please choose a valid option")
                continue
        else:
            return

while True:
    while True:
        number_one = input("\nChoose First Number: \n").strip()
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
        operation = input(f"{YELLOW}Operation (+, -, *, /, history, help, exit): {RESET}").strip()
        if operation.lower() == "help":
            print(f"{CYAN}\n=== Help ==={RESET}")
            print("+ Enter two numbers and choose one of + - * /.")
            print("+ Commands: history, clear, exit")
            print("+ Division by zero returns Infinity")
            continue
        if operation.lower() == "exit":
            print(f"{GREEN}Goodbye!{RESET}")
            exit()
        if operation.lower() == "history":
            if history:
                print(" \n=== History ===")
                for item in history:
                    print("• {}".format(item))
            else:
                print("There is no history.")
                continue
        if operation == "+" or operation == "1":
            answer = a + b
            print(f"{CYAN}The answer is {answer}.{RESET}")
            timeanddate = datetime.now().strftime("On %d.%m.%Y at %H:%M:%S")
            history.append("{} => {} + {} = {}".format(timeanddate, a, b, answer))
            break
        elif operation == "-" or operation == "2":
            answer = a - b
            print(f"{CYAN}The answer is {answer}.{RESET}")
            timeanddate = datetime.now().strftime("On %d.%m.%Y at %H:%M:%S")
            history.append("{} => {} - {} = {}".format(timeanddate, a, b, answer))
            break
        elif operation == "*" or operation == "3":
            answer = a * b
            print(f"{CYAN}The answer is {answer}.{RESET}")
            timeanddate = datetime.now().strftime("On %d.%m.%Y at %H:%M:%S")
            history.append("{} => {} * {} = {}".format(timeanddate, a, b, answer))
            break
        elif operation == "/" or operation == "4":
            if b == 0:
                answer = "Infinity"
            else:
                answer = a / b
            print(f"{CYAN}The answer is {answer}.{RESET}")
            timeanddate = datetime.now().strftime("On %d.%m.%Y at %H:%M:%S")
            history.append("{} => {} / {} = {}".format(timeanddate, a, b, answer))
            break
        else:
            print("Please select an operation. \n 1. + 2. - 3. * 4. / \n")
    while True:
        repeat = input("Would you like to do another calculation? \n").strip().lower()
        if repeat == "yes" or repeat == "y":
            break
        elif repeat == "no" or repeat == "n":
            print("Thank you for using the calculator.")
            break
            break  
        else:
            print("Please choose either Yes or No.")
            continue
        continue
groups = []
repeats = 0

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m' 
BLUE = '\033[34m'
CYAN = '\033[36m'
MAGENTA = '\033[35m'
RESET = '\033[0m' 
for i in range(5):
    repeats = repeats + 1
    # print(f"{CYAN}Information for Group {}{RESET}".format(repeats))
    print(f"{CYAN}Information for Group {repeats}{RESET}")
    groupname = input(f"{YELLOW}What is the name of the group? ")
    sizeofgroup = input("What is the size of the group? ")
    dateofcompetition = input("When did the competition happen? ")
    venue = input("What was the venue? ")
    typeofmedal = input(f"What is the type of medal? ")
    print(f"\n{GREEN}Information Appended to Tuple\n{RESET}")
    grouptuple = (groupname, sizeofgroup, dateofcompetition, venue, typeofmedal)

    groups.append(grouptuple)

print(f"{RED}=== Information ==={RESET}")
print(f"{MAGENTA}GROUP NAME, SIZE OF GROUP, DATE OF COMPETITION, VENUE, TYPE OF MEDAL")
for j in groups:
    print("• {}".format(', '.join(j)))

print(f"{RESET}Thank you for using the Tuple Homework Project")
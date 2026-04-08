groups = []
for i in range(5):
    groupname = input("What is the name of the group? ")
    sizeofgroup = input("What is the size of the group? ")
    dateofcompetition = input("When did the competition happen? ")
    venue = input("What was the venue? ")
    typeofmedal = input("What is the type of medal? ")
    print("\n+++ Information Appended to Tuple +++ \n")
    grouptuple = (groupname, sizeofgroup, dateofcompetition, venue, typeofmedal)

    groups.append(grouptuple)

print("=== Information ===")
print("GROUP NAME, SIZE OF GROUP, DATE OF COMPETITION, VENUE, TYPE OF MEDAL")
for j in groups:
    print("• {}".format(', '.join(j)))
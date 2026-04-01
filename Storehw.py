textbooks = {
    "Physics Book" : 300,
    "Maths Book" : 400,
    "English Book" : 200,
    "Chemistry Book" : 300
}
print(textbooks)
textbooks["Physics Book"] = 200
print(textbooks)

textbooks["Biology Book"] = 300
textbooks["History Book"] = 250
print(textbooks)

while True:
    bookchoice = input("What book would you like to find the cost of? ")
    if bookchoice not in textbooks:
        print("Your choice of book is not in the dictionary of textbooks.")
        continue
    else:
        print(textbooks[bookchoice])
        print(textbooks)
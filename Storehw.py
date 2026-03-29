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


bookchoice = input("What book would you like to find the cost of?")
print(textbooks[bookchoice])
print(textbooks)
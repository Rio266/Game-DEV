dictionary = {

}
while True:
    option = input("Which option would you like to choose? \n1. Insert \n2. Get Capital Values \n3. Get Country Values \n4. Get Capital from Country \n5. Delete Pair \n6. Exit \n")
    if option == "1":
        country = input("What country would you like to choose? ")
        capital = input("What capital would you like to choose? ")
        dictionary[country] = capital
    elif option == "2":
        print(dictionary.values())
    elif option == "3":
        print(dictionary.keys())
    elif option == "4":
        country_chosen = input("What country would you like to find the capital of? ")
        if country_chosen not in dictionary:
            print("The chosen country is not in the dictionary.")
        else:
            print(dictionary[country_chosen])
    elif option == "5":
        country_delete = input("What country would you like to remove from the dictionary? ")
        if country_delete not in dictionary:
            print("The chosen country is not in the dictionary.")
        else:
            dictionary.pop(country_delete)
            print("The country capital pair is deleted.")
    elif option == "6":
        print("Thank you for using the Dictionary_practice project.")
        break
    else:
        print("Please choose a number from the question.")
        continue
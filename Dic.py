# Create a Dictionary
sample_dictionary = {
    "name": "Akshar",
    "age" : 13,
    "city": "London"
}

# Print the Dictionary
print(sample_dictionary)

# Accessing Values in a Dictionary
print(sample_dictionary["city"])

# Adding Items to a Dictionary  
sample_dictionary["Favourite Food"] = "Burger"
print(sample_dictionary)

# Updating Items in a Dictionary
sample_dictionary["city"] = "Paris"
print(sample_dictionary)

# Removing Items from a Dictionary
#1. Using del keyword
del sample_dictionary["age"]
print(sample_dictionary)
#2. Using pop() method
sample_dictionary.pop("Favourite Food")
print(sample_dictionary)

#Print all keys
print(sample_dictionary.keys())

#Print all values
print(sample_dictionary.values())

#Add list into dictionary
sample_dictionary["marks"] = [3, 6, 9, 12]
print(sample_dictionary)

#Access value in list in dictionary
print(sample_dictionary["marks"][2])

#Create nested dictionary
dictionary_2 = {
    "Aarav" : {
        "age" : 12,
        "hobby" : "cycling"
    },
    "Rohan" : {
        "age" : 15,
        "hobby" : "football"
    }
}

#Print all the keys and values
print(dictionary_2.values())
print(dictionary_2.keys())

#Access value in nested dictionary
print(dictionary_2["Rohan"]["age"])

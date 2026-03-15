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
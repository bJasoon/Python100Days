#========================================
#Dictionaries
#{key:value, key:value}
# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.", 
#     "Function": "A piece of code that you can easily call over and over again.",
#     #"Loop" : "The action of doing something over and over again",
# }

# print(programming_dictionary["Bug"])

# programming_dictionary["Loop"] = "The action of doing something over and over again"

# print(programming_dictionary)

# empty_dictionary = {}

# # programming_dictionary = {}
# print(programming_dictionary)

# print(programming_dictionary["Bug"])
# programming_dictionary["Bug"] = "A moth in your computer"


# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

#========================================
# Nesting

# {Key: [List],
#  Key: {Dict},}

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"],
# }

#print(travel_log["France"][1])

nested_list =["A","B", ["C","D"]]

print(nested_list[2][1])

travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
    },
}

print(travel_log["Germany"]["cities_visited"][2])
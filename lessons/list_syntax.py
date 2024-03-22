"""Demostrate basic list syntax"""

# Initialize a empty list
grocery_list: list[str] = list() # <- list constructor
grocery_list: list[str] = [] # <- literal

print(grocery_list)

# Add item to a list
grocery_list.append("bananas")
grocery_list.append("milk")
grocery_list.append("bread")

print("After appending: ")
print(grocery_list)

# create an already populated list
grocery_list2: list[str] = ["bananas", "milk", "bread"]
print("Populated list:")
print(grocery_list2)
grocery_list2.append("eggs")
print(grocery_list2)

# indexing
print ("Print first element of string")
print(grocery_list[0])

# modifying by index
print("Before change: ")
print(grocery_list)
grocery_list[1] = "almond milk"
print("After change: ")
print(grocery_list)

# you can have duplicates
grocery_list.append("almond milk")
print("Add almond milk again")
print(grocery_list)

# measuring length 
print(grocery_list)
print(len(grocery_list))

# removing an item
grocery_list.pop(1)
print("after removing almond milk: ")
print(grocery_list)

# function name: display
# parameter: list[str]
# return  nothing
# print out the list

def display(word: list[str]):
    print(word)

display(grocery_list)
x = display(["Alyssa", "Erin", "AK"])
print(x)

# create a list!
# name: create
# parameters: str and str
# RV: list[str]
# put both parameters into list and return that list

def create(word1 : str, word2: str) -> list[str]:
    my_list: list[str] = [word1, word2]
    return my_list

x: list[str] = create("Hello", "World")
print(x)
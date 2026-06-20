dict = {
    "Name" : "Abdurrahman",
    "cgpa" : 9.60,
    "marks" : [98, 87, 75] # List
}

print(dict.keys()) # Print all the key of the dictionary
print(dict.values()) # Print all the values of the dictionary
print(dict.items()) # returns all (key, value) pairs as a tuple
print(dict.get("Name")) # returns value according to key [It returns NONE when no key is matched in the dictionary]

dict.update({
    "city" : "Ballia"
})  # insert the specified items to the dictionary

print(dict)

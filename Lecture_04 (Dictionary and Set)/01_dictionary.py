# DICTIONARY:- Dictionaries are used to store data values in a "key:value" pair.

# NOTE - All type of datatype can be store in the dictionary as a value.
#        All type of datatype can be named as key except list in the dictionary. # IMPORTANT

# PROPERIES:- Unordered, Mutable(Changeable) & don't allow duplicate key.

dict = {
    "Name" : "Abdurrahman",
    "cgpa" : 9.60,
    "marks" : [98, 87, 75] # List

}

print(dict["marks"])

dict["Name"] = "Abdurrahman Ansari"  # Overwrite
dict["surname"] = "Ansari"  # New key formation

print(dict) # OUTPUT- {'Name': 'Abdurrahman Ansari', 'cgpa': 9.6, 'marks': [98, 87, 75], 'surname': 'Ansari'}


#  EMPTY DICTIONARY

null_dictionary = {}
print(type(null_dictionary))

# NESTED DICTIONARY

student = {
    "name" : "rahul",
    "subject" : {
        "physics" : 97,
        "chemisty" : 98,
        "math" : 95
    }
}

print(student["subject"])
print(student["subject"]["chemisty"])
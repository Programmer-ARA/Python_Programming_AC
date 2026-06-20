# SET :- Set is a COLLECTION of the "UNORDERED" ITEMS.
# Each element in the set must be "UNIQUE" & "IMMUTABLE" but set in itself is "MUTABLE".
# lIST & DICTIONARY can't be stored in the set

set_0 = {1, 2, "Hello"}
print(type(set))

set_1 = {1, 2, 2, 2, "Hello", "World", "World"} # is  same as {1, 2, "Hello", "World"} beacouse set ignore duplicate value.
print(set_1)


# EMPTY SET

set_2 = {}  # empty dictionary
set_3 = set() # empty set 

print(type(set_2))
print(type(set_3))
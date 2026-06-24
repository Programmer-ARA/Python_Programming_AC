# Note-- Tuple is IMMUTABLE(Can't be changed) just like string in python.

Tup = (2, 1, 3, 1)
Tup_with_1_element = (1,)

print(Tup)
print(type(Tup))
print(Tup[3])

# Tup[0] = 4        -----Note- NOT ALLOWED for tuple!!!

# TUPLE SLICING is similar to string

print(Tup[1:3]) # Ending index is not included
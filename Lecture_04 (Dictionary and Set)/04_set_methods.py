collection = {"beta", 1, "asdf"}

collection.add(1) # adds element in the set
collection.add("baap")
collection.add((45,345,3453)) # list
collection.add(3)

collection.remove(3) # removes element in the set.

print(collection)

collection.pop() # randomly removes element of the set
print(collection)

collection.clear() # empties the set
print(collection)


# UNION & COLLECTION

set1 = {1, 2, 3}
set2 = {2, 3, 4, 5}

print(set1.union(set2))
print(set1.intersection(set2))

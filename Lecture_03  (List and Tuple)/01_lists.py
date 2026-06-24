# LISTS IN PYTHON:- A built-in data type that stores set of values. It can store elements of different types (integer, float, string etc.)

marks = [94.4, 87.5, 95.2, 66.4, 45.1]

print(marks)
print(type(marks))
print(marks[4])
print(len(marks))

# list can store all type of datatype. Ex---

student = ["Karan", 54, 94.5, "Delhi"]
print(student)

# Note-- List is MUTABLE(Can be changed) in python.
student[0] = "Arjun"
print(student)

# LIST SLICING is similar to string

print(student[1:4]) # Ending index is not included


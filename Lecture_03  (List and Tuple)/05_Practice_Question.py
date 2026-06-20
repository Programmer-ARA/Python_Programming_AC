# # -----{QUESTION-01: WAP to ask the user to enter names of their 3 favorite movie and store them in a list.}-----

# list = []

# list.append(input("Enter your 1st favorite movie name: "))
# list.append(input("Enter your 2nd favorite movie name: "))
# list.append(input("Enter your 3rd favorite movie name: "))

# print(list)


# # -----{QUESTION-02: WAP to check if a list contains a palindrome of elements.}-----

# list = [1, 2, 3, 2, 1]

# clone = list.copy()
# clone.reverse()

# if(list == clone):
#     print("THE LIST IS PALINDROME")
# else:
#     print("THE LIST IS NOT PALINDROME")


# -----{QUESTION-03: WAP to count the number of students with the "A" grade in the following tuple.}-----

tup = ("C", "D", "A", "A", "B", "B", "A")
print(tup.count("A"))

list = ["C", "D", "A", "A", "B", "B", "A"]
list.sort()
print(list)

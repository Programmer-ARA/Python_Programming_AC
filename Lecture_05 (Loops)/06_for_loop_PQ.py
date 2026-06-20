# # ----------- QUESTION - 01 ----------

# num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# for val in num:
#     print(val)


# ----------- QUESTION - 02 ---------

num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49)

target = int(input("Enter the number you want to find: "))

index = 0
for val in num:
    if (val == target):
        print("Number found in the list at index", index)
    index += 1



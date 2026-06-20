# # ----------- QUESTION - 01 ----------
# # WAP to find the sum of first n natural numbers.(using while)

# num = int(input("Enter the number: "))
# sum = 0

# while num > 0:
#     sum = sum + num
#     num = num - 1

# print(sum)


# # WAP to find the sum of first n natural numbers.(using for)

# num = int(input("Enter the number: "))
# sum = 0

# for i in range(1, num+1):
#     sum += i

# print("Total Sum = ",sum)


# # ----------- QUESTION - 02 ----------
# # WAP to find factorial of first n numbers.(using for)

num = int(input("Enter the number: "))
fac = 1

for i in range(1, num+1):
    fac *= i

print("The factorial of the number is = ", fac)

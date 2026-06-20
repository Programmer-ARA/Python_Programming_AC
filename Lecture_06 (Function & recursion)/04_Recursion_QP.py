# # ----------- QUESTION - 01 ----------
# # Write a recursive program to calculate the sum of first n natural number.

# def sum(n):
#     if(n == 0):
#         return 0
#     else:
#         return n + sum(n-1)

# print(sum(35))

# # ----------- QUESTION - 02 ----------
# # Write a recursive function to print all elements in a list.

def print_list(list, n):
    if(n == -1):
        return
    else:
        print(list[n])
        return print_list(list, (n-1))
    
num = [1, 2, 3, 4, 5, 6]

print_list(num, 5)
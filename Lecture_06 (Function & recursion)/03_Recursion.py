# RECURSION:- When a function call itself repeatedly.

def show(n):
    if(n==0): #base case
        return
    print(n)
    show(n-1)
    print("end")

show(4)

# QUESTION:- Finding factorial using recusion

def fact(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * fact(n-1)
    

print(fact(3))

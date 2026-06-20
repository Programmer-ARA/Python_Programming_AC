# FUNCTION:- Block of statements that perform a specific task.

# function definition
def sum(a, b): # a, b are parameters
    s = a + b
    print(s)
    
sum(9,10) # function call; arguments

def print_hello():
    print("Hello")

print_hello()

def prod(a=1, b=1): #default parameter 
    print(a*b)

prod()

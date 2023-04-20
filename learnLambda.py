"""
Normal functions
"""
def exponentiation(x):
    return x*x

def sum(x,y):
    return x+y

def cube(x):
    return x**3

"""
Lambda functions
"""
lamb_exponentiation = lambda x: x*x
lamb_sum = lambda x,y: x+y
lamb_cube = lambda x: x**3

"""
Prints
"""

print("Normal: ", exponentiation(2), sum(5,2), cube(2))
print("Lambda: ", lamb_exponentiation(2), lamb_sum(5,2), lamb_cube(2))

numbers = [1, 2, 3, 4, 5]
print("Normal: ", list(map(cube,numbers)))
print("Lambda: ",list(map(lambda x: x**3, numbers)))
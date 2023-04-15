"""
Normal functions
"""
def exponentiation(x):
    return x*x

def sum(x,y):
    return x+y

def reverse(text):
    return text[-1]

"""
Lambda functions
"""
lamb_exponentiation = lambda x: x*x
lamb_sum = lambda x,y: x+y

"""
Prints
"""

print("Normal: ", exponentiation(2), sum(5,2))
print("Lambda: ", lamb_exponentiation(2), lamb_sum(5,2))
print(reverse("siemanko"))
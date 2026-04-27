# Factorial Functions

fac = (lambda f: f(f))(lambda f: lambda x: 1 if x == 0 else x * f(f)(x - 1))

# def visualisatiom
def factorial(x):
    return 1 if x == 0 else x * factorial(x - 1)
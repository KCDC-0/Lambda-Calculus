# Factorial Functions

fac = (lambda f: f(f))(lambda f: lambda x: 1 if x == 0 else x * f(f)(x - 1))

# def visualisatiom
def factorial(x):
    return 1 if x == 0 else x * factorial(x - 1)

# This one uses a Z-combinator
Z = lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v)))
fac_z = Z(lambda f: lambda x: 1 if x == 0 else x * f(x - 1))

# A Y combinator will cause an infinite recursive loop due to pythons 'eager' evaluation order

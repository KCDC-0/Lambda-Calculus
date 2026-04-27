# Prime finder functions

# Iterative function using the theory behind fixed point operators
f1 = (lambda x: x(x))(lambda x: lambda end, n = 2, l = [], P = 1: l if  n > end else (x(x)(end, n+1, l+[n], P*n) if __import__("math").gcd(P, n) == 1 else x(x)(end, n+1, l, P)))

# This one uses recursion raher than iteration
f = lambda n, P = 1: [(i, P := P * i)[0] for i in range(2, n) if __import__("math").gcd(P, i) == 1]

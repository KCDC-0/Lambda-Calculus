# Prime finder functions

# Iterative function using the theory behind fixed point operators
func1 = (lambda x: x(x))(lambda x: lambda end, n = 2, l = [], P = 1: l if  n > end else (x(x)(end, n+1, l+[n], P*n) if __import__("math").gcd(P, n) == 1 else x(x)(end, n+1, l, P)))

# This one uses iteration rather than recursion
func1_iter = lambda n, P = 1: [(i, P := P * i)[0] for i in range(2, n) if __import__("math").gcd(P, i) == 1]

# This is a faster method using trial division rather than gcd
func2_iter = lambda n: [x for x in range(2, n + 1) if all(x % i > 0 for i in range(2, int(x**0.5) + 1))]

# Here are some more efficient functions that use seiving
func3 = lambda n: set(range(2, n)) - {j for i in range(2, int(n**0.5) + 1) for j in range(i*i, n, i)}

# Gemini created this one based on broken code, its the fastest as it uses the sieve of eratosthenes
func4 =  (lambda x: x(x))(lambda x: lambda n, c=0, cache=None: (x(x)(n, 1, [False, False] + [True] * (n - 1))) if cache is None else ([p for p, alive in enumerate(cache) if alive] if c > int(n**0.5) else ([cache.__setitem__(slice(c*c, n+1, c), [False] * len(range(c*c, n+1, c))) for _ in [1] if cache[c]], x(x)(n, c + 1, cache))[-1]))




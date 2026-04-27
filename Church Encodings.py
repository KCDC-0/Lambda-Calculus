## Implementation of church numerals, logic gates and arithmetic

# Numbers and arithmetic
zero = lambda f: lambda x: x
one = lambda f: lambda x: f(x)
two = lambda f: lambda x: f(f(x))

succ = lambda n: lambda f: lambda x: f(n(f(x)))
plus = lambda m: lambda n: lambda f: lambda x: m(f)(n(f(x)))
mult = lambda m: lambda n: lambda f: lambda x: m(n(f(x)))
exp = lambda b: lambda n: n(b)

church_to_int = lambda n: n(lambda x: x + 1)(0)
int_to_church = (lambda x: x(x))(lambda f: lambda i: zero if i == 0 else succ(f(f)(i-1)))


# Booleans and logic gates
t = lambda x: lambda y: x
f = lambda x: lambda y: y

and_gate = lambda x, y: x(y)(f)
or_gate = lambda x, y: x(t)(y)
not_gate = lambda x: x(f)(t)

void = lambda x: x

# Pairs and tuples
pair = lambda a: lambda b: lambda f: f(a)(b)
left = lambda p: p(lambda a: lambda b: a)
right = lambda p: p(lambda a: lambda b: b)

# Combinators
U = lambda f: f(f)
Z = lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v)))
Y = ((lambda h: lambda F: F(lambda x:h(h)(F)(x)))(lambda h: lambda F: F(lambda x:h(h)(F)(x))))

Y(lambda f: lambda n: 1 if n <= 0 else n*f(n-1))(5)
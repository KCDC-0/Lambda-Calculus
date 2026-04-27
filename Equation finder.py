# My addtions to Equation-finder

# - 175 chars (uses eval, recursion)
func5 = (lambda x: x(x))(lambda x: lambda n, m = '1', c = 2: (print(m) if eval(m) == n else ()) if c > 9 else any(x(x)(n, m + i + str(c), c+1) for i in ['+', '-', '']))

# the any() finction is to ensure python runs the recursive steps, since the fucntion only prints, the result of any doesn't matter
# memory is not the concern here and generators are not wanted

# def representation of func5
def func5_visual (n, m = '1', c = 2):
    if c == 10:
        if eval(m) == n:
            print(m)
    else:
        for i in ['+', '-', '']:
            func5_visual(n, m + i + str(c), c+1)


# Exteneded version to include * and /, extremely inefficient though
func5_extended = (lambda x: x(x))(lambda x: lambda n, m = '1', c = 2: (print(m) if eval(m) == n else ()) if c > 9 else any(x(x)(n, m + i + str(c), c+1) for i in ['+', '-', '', '*', '/']))



"""Lab1.1"""
def is_multiple(n,m):
    """Lab1.1"""
    if n % m == 0:
        return "True"
    else:
        return "False"
print(is_multiple(int(input()),int(input())))

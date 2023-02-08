"""Lab1.2"""
def is_even(k):
    """Lab1.2"""
    k = abs(k)
    while True:
        k -= 2
        if k == 0:
            return "True"
        elif k < 0:
            return "False"
print(is_even(int(input())))

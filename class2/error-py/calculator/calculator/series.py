def factorial(n):
    if n<0:
        raise ValueError("Factorial no está definido para números negativos")
    if n == 0:
        return 1
    return n* factorial(n-1)


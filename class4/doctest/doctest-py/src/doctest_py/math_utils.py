""""
Esto es un modulo que contiene algunas funciones matemáticas con doctests.
"""

def factorial(n):
    """Calcula el factorial de un numero entero no negativo.

    Args:
        n (int): Número entero no negativo.

    Returns:
        int: El factorial de n.

    Raises:
        ValueError: Si n es un número negativo.
    
    Examples:
        >>> factorial(0)
        1
        >>> factorial(1)
        1
        >>> factorial(2)
        2
        >>> factorial(3)
        6
        >>> factorial(4)
        24
        >>> factorial(5)
        120
        >>> factorial(6)
        720

        # Error cases
        >>> factorial(-1)
        Traceback (most recent call last):
            ...
        ValueError: No existe el factorial de un número negativo
    """
    if n <0:
        raise ValueError("No existe el factorial de un número negativo")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

def add(a, b):
    """Suma dos números.

    Args:
        a (int): Primer número.
        b (int): Segundo número.

    Returns:
        int: La suma de a y b.

    Examples:
        >>> add(1, 1)
        2
        >>> add(2, 3)
        5
        >>> add(5, 5)
        10
        >>> add(10, 10)
        20
    """
    return a + b
from calculator import series

def calculate_factorial(n):
    try:
        return(series.factorial(5))
    except ValueError as e:
        print("Warning: ",e)
        return(0)

print(calculate_factorial(5))
print(calculate_factorial(3))
print(calculate_factorial(-1))
import math

def calculate_y(a, b, c, d):
    if a < b:
        raise ValueError("Подкоренное выражение (a - b) не может быть отрицательным!")
    if c == d:
        raise ZeroDivisionError("Деление на ноль (c равно d)!")
    
    return math.sqrt(a - b) / (c - d)
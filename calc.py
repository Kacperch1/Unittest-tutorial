def add(x, y):
    return x + y

def sub(x, y):
    return  x - y

def multi(x, y):
    return  x * y

def div(x, y):
    if y == 0:
        raise ValueError("Can not devide by zero!")
    return x / y
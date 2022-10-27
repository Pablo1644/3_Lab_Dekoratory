import time
import numpy as np


def dekorator(func):  # function is a parameter
    def wrapper(*args, **kwargs):
        start = time.time()  # return actual time
        # construction when we're not sure about how many parameters are
        # Non/-.- Keyboard arguments
        result = func(*args, **kwargs)
        end = time.time()  # return time after making a function
        print(func.__name__, "wykonywała się", end - start, "sekund.")
        return result

    return wrapper


# In different functions we've got different numbers of parameters
@dekorator  # different decorators
def add(a, b):
    return a + b


@dekorator
def substract(a, b):
    return a - b


@dekorator
def multiply(a, b):
    time.sleep(1)
    return a * b


@dekorator
def divide(a, b):
    time.sleep(1)
    try:
        return a / b
    except ZeroDivisionError:
        return 0


@dekorator
def add_three(a, b, c):
    time.sleep(1)
    return a + b + c


@dekorator
def average(a, b, c):
    time.sleep(1)
    return (a + b + c) / 3


@dekorator
def maximum(a, b, c, d):
    time.sleep(1)
    return maximum(a, b, c, d)


@dekorator
def minimum(a, b, c, d, e):
    time.sleep(1)
    return minimum(a, b, c, d, e)


@dekorator
# Checking what is more time consuming,multiply,or np.multiply
def multiply_numpy(a, b):
    time.sleep(1)
    return np.multiply(a, b)


@dekorator
def list_operation(l1, l2):
    time.sleep(1)
    k = np.concatenate((np.array(l1).T, np.array(l2).T, np.zeros(l1.__len__())), axis=0)
    k = np.append(k, [1, 1, 1, 19])
    return k


list_1 = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 23, 57, 1239, 1, 10]
list_2 = [1, 2, 192, 1230, 18, -4, 5, 6, 7, 8, 9, 10, 11, 0, 15]

# example prints
print(multiply_numpy(5, 7))
print(multiply(5, 7))
print(list_operation(list_1, list_2))
print(minimum(100, 20, 1, -9, 15))
print(maximum(100, 20, 1, -9, 15))

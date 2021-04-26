from time import time


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time()
        operation = func(*args, **kwargs)
        end = time()
        print(f"Runtime of {func.__name__} is: {(end - start)*1000} ms")
        return operation
    return wrapper
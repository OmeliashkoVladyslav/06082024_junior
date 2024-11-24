def wrap_result_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        return  result

    return wrapper

@wrap_result_decorator
def foo1():
    return 1

@wrap_result_decorator
def foo2():
    return 100

@wrap_result_decorator
def foo3():
    return []

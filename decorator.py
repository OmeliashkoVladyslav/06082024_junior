def check_number(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if type(result) is int:
            new_result = {'result': result + 10}
        else:
            new_result = {'result': result}
        return new_result
    return wrapper

@check_number
def test_function(x):
    return x

print('Yes, it is integer number, lets add 10 -', test_function(4))
print('No, it is not integer number -', test_function(4.5))

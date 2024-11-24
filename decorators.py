# n = 11
#
# print(id(n))
#
# m = n + 2
#
# def foo():
#     pass
#
# print(id(foo))
# print( foo )
from typing import Callable

# n = 111
# print(id(n))
#
# alternative = print
#
# print(alternative)
# alternative(n)
# print(print)

def log_decorator(func: Callable):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('logs', mode='a', encoding='utf-8') as file:
            file.write(f'{func.__name__}{result}\n')
        # print(func.__name__, result)
        return result

    return wrapper



@log_decorator
def add_two_numbers(number_1: float, number_2: float) -> float:
    result = number_1 + number_2
    return float(result)

add_two_numbers(5555, 6666)

def add_three_numbers(number_1: float, number_2: float, number_3: float) -> float:
    result = number_1 + number_2 + number_3
    return float(result)



# add_two_numbers = decorator(add_two_numbers)

add_two_numbers(555, 5555)

pass

# wrapper(add_two_numbers, 2.6, number_1=78)
# wrapper(add_three_numbers, 2.6, 78, number_3=0.69)

# res = add_two_numbers(2.5, number_2=3.6)
# res = add_two_numbers(2.5, number_2=3.6, number_3=4.6)
#
# add_two_numbers = wrapper(add_two_numbers)
#
# res = add_two_numbers(2.5, number_2=2.6)
# pass
"""
A decorator is a function that takes another function as an argument , adds some kind of functionality and
then returns another function. All of these without altering the source code of the original function that you passsed in

"""


def decor1(func):
    def inner():
        x = func()
        return x * x

    return inner


def decor(func):
    def inner():
        x = func()
        return 2 * x

    return inner


@decor1
@decor
def num():
    return 10


print(num())


#####################################################################

def hello_decorator(func):
    def inner1(*args, **kwargs):
        print("Before execution")

        returned_value = func(*args, **kwargs)
        print("After execution")

        return returned_value

    return inner1


@hello_decorator
def sum_two_numbers(a, b):
    print("Inside the function")
    return a + b


a, b = 1, 2

print("Sum = ", sum_two_numbers(a, b))

args = 1 ,2 ,3 ,4
print("sum = ",sum_two_numbers(*args))

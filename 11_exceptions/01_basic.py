orders = ["masala", "ginger"]

# print(orders[2])  # getting IndexError because index 2 does not exist


try:
    print(orders[2])
except IndexError:
    print("The index you are trying to access does not exist")


from functools import wraps


def addition(func):
    @wraps(func)
    def wrappers(*args, **kwargs):
        print("print before")

        print(f"Mutiplication {args[0]} * {args[1]} = {args[0] * args[1]}")
        func(*args, **kwargs)
        print("print after")

    return wrappers


@addition
def abc(a, b):
    print("function call")
    print(f"Addition -> {a} + {b} = {a+b}")


abc(4, 5)

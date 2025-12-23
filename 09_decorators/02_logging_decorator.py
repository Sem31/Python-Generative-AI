from functools import wraps


def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function '{func.__name__}'...")
        result = func(*args, **kwargs)
        print(
            f"Function '{func.__name__}' was called with arguments: {args} and keyword arguments: {kwargs}"
        )
        return result

    return wrapper


@log_activity
def brew_chai(type):
    print(f"Brewing a cup of {type} chai...")


brew_chai("masala")
brew_chai(type="ginger")


@log_activity
def add(a, b):
    return a + b


add(3, 5)
add(a=10, b=20)

from functools import wraps


def taking_cookies(func):
    @wraps(func)
    def wrapper():
        print("Before calling preparing chai function: Taking cookies from the jar.")
        func()
        print("After calling preparing chai function: Returning cookies to the jar.")

    return wrapper


@taking_cookies
def preparing_chai():
    print("Preparing chai now... Enjoy your drink!")


preparing_chai()
print(
    preparing_chai.__name__
)  # Without functools.wraps, this would print 'wrapper', not 'preparing_chai'.

from functools import wraps


def require_authentication(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print("Access denied: User is not authenticated as admin.")
            return None
        else:
            return func(user_role)

    return wrapper


@require_authentication
def access_sensitive_data(role):
    print("Accessing sensitive data... role:", role)


access_sensitive_data("admin")  # Should succeed
access_sensitive_data("guest")  # Should raise PermissionError

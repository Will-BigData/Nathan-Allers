import functools

def handle_with_message(exception=Exception, message="An error occurred"):
    def decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception:
                print(message)
        return inner
    return decorator

def reraise_with_message(exception=Exception, message="An error occured"):
    def decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception:
                print(message)
                raise exception
        return inner
    return decorator

def handle_with_func(exception=Exception, handler=lambda: None):
    def decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception:
                return handler()
        return inner
    return decorator


def get_user_int(prompt: str, requirements: str="Invalid input.", valid_func=lambda x: True) -> int:
    valid = False
    result = None
    while not valid:
        try:
            result = int(input(prompt))
            valid = valid_func(result)
            if not valid:
                print(requirements)
        except ValueError:
            print("Input must be an integer.\n")
    return result
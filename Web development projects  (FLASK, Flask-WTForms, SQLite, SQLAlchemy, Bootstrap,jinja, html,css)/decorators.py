# Advanced Python Decorator Functions

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated_decorator(function_):
    """Triggers a function is the user a condition (is_logged_in) if fulfilled."""
    def wrapper(*args, **kwargs):
        # checks if a user (passed as the first argument) is logged in
        if args[0].is_logged_in:
            function_(args[0])

    return wrapper


@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")


# Create a logging_decorator() which is going to log the name of the function that was called,
# the arguments it was given and finally the returned output.
def logging_decorator(fn):
    def wrapper(*args, **kwargs):
        print(f"You called {fn.__name__}{args}")
        result = fn(*args)
        print(f"It returned: {result}")

    return wrapper


@logging_decorator
def function(*args):
    result = args[0]
    for args in args[1:]:
        result *= args
    return result


function(1, 2, 3, 98, 100)

new_user = User("new user")
new_user.is_logged_in = True
create_blog_post(new_user)

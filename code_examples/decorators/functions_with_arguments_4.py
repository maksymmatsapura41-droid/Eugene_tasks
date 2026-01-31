def do_it_twice(func):
    def wrapper(name, *args, **kwargs):
        func(name, *args, **kwargs)
        func(name, *args, **kwargs)
    return wrapper


@do_it_twice
def do_something_twice(name):
    print(f"Something is happening before the function is called. {name}")

@do_it_twice
def another_function(age):
    print(f"Something is happening before the function is called. {age}")

do_something_twice("john")
another_function(18)
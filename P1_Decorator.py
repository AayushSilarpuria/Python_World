def decorator_func(func):
    def wrapper_func():
        print("wrapper_func Worked")
        return func()
    print("decotator_func worked")
    return wrapper_func

def show():
    print("Show Worked")
decorator_show = decorator_func(show)
decorator_show()
#greet is a decorator function.

def greet(add):
    def mfx():
        print("Good Morning Ayush")
        add()
        print("Have a nice Day")
    return mfx()
    


@greet
def add(x=2, y=7):
    print(f"Sum of {x} and {y} is {x+y}")
    
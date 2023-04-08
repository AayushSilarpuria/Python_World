#greet is a decorator function.

def greet(fx):
    def mfx():
        print("Good Morning Ayush")
        fx()
        print("Have a nice Day.")
        print()
    return mfx()

@greet
def add(x=2, y=7):
    print(f"The addition of {x} and {y} is {x+y}")
 
@greet   
def sub(x=7, y=2):
    print(f"The subraction of {x} and {y} is {x-y}")
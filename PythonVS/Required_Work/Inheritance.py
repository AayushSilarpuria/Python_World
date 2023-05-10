class A:
    def display(self):
        print("A Display")
    
class B(A):
    def show(self):
        print("B show")
    
d = B()
d.show()
d.display()
from tkinter import *

root = Tk() 
root.title("Change Temperature")
root.geometry("1200x500")
root.config(bg = "#00076e")

def plus():
    c = cel.cget("text")
    c1 = c.strip("ºC")
    c2 = float(c1) + 0.5
    c3 = str(c2) + "ºC"
    cel.config(text=c3)


    f = (c2*1.8) + 32
    f1 = str(round(f,2)) + "ºF"
    fer.config(text=f1)


def minus():
    m = cel.cget("text")
    m1 = m.strip("ºC")
    m2 = float(m1) - 0.5
    m3 = str(m2) + "ºC"
    cel.config(text = m3)

    f = (m2*1.8) + 32
    f1 = str(round(f,2)) + "ºF"
    fer.config(text=f1)   



window = Label(root, bg="#0185c0")
window.place(x=50, y=50, width = 1100, height= 400)

cel = Label(root, bg= "#00dbfd", text= "27ºC", font=("Arial", 100, "bold",), fg="#ffffff" )
cel.place(x=380, y= 55, width= 460, height =120)

fer = Label(root, bg="#00dbfd", text= "98ºF" , font=("Arial", 100, "bold"), fg="#ffffff" )
fer.place(x=380, y=325, width = 460, height = 120)

p_but = Button(root, bg="#d2f1f0", text = "+", font =("Arial", 100, "bold"), fg="#ba0000", borderwidth=5, command = plus)
p_but.place(x=58, y=120, )

m_but = Button(root, bg="#d2f1f0", text = "–", font=("Arial", 100, "bold"), fg= "#ba0000", borderwidth=5, command= minus)
m_but.place(x=946, y =120)
# The character U+2013 "–" could be confused with the ASCII character U+002d "-", which is more common in source code.

root.mainloop()
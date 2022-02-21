from tkinter import *
root=Tk()
root.geometry("655x333")

def hello():
    print("Hello tkinter Buttons")
def name():
    print("Name is Leena")
def python():
    print("Python is very popular and esy language")
def auther():
    print("Auther of Python is Guido Van Rossum")

frame=Frame(root,borderwidth=6,bg="grey",relief=SUNKEN)
frame.pack(side=LEFT,anchor="nw")
b1=Button(frame,fg="red",text="Welcome",command=hello)
b1.pack(side=LEFT,padx=23)
b2=Button(frame,fg="red",text="Tell me Your Name now",command=name)
b2.pack(side=LEFT,padx=23)
b3=Button(frame,fg="red",text="What is Python?",command=python)
b3.pack(side=LEFT,padx=23)
b4=Button(frame,fg="red",text="Show auther name?",command=auther)
b4.pack(side=LEFT,padx=23)


root.mainloop()
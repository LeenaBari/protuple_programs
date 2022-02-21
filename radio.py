from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("455x233")
root.title("Radio Buttons")
def order():
    tmsg.showinfo("Order Received!", f"We have received order{var.get()}.thanks for ordering")

# var=IntVar()
# var.set(1)
var=StringVar()
var.set("Radio")
Label(root,text="What would you like to have?",justify=LEFT,padx=14).pack()
radio=Radiobutton(root,text="Dosa",padx=14,variable=var,value="Dosa").pack(anchor="w")
radio=Radiobutton(root,text="Idly",padx=14,variable=var,value="Idly").pack(anchor="w")
radio=Radiobutton(root,text="PaniPuri",padx=14,variable=var,value="PaniPuri").pack(anchor="w")
radio=Radiobutton(root,text="Paratha",padx=14,variable=var,value="Paratha").pack(anchor="w")
Button(text="Order now",command=order).pack()


root.mainloop()

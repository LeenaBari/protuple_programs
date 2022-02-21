from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("455x233")
root.title("Slider tutorial")
def getdollar():
    print(f"we have credited{myslider2.get()} dollars to your account")
    tmsg.showinfo("Amount credited!",f"We have credited{myslider2.get()}dollars to your accont")

# myslider=Scale(root,from_=0,to=100)
# myslider.pack()

Label(root,text="how many dillas do you want?").pack()
myslider2=Scale(root,from_=0,to=100,orient=HORIZONTAL,tickinterval=50)
# myslider2.set(34)
myslider2.pack()
Button(root,text="Get dollars!", pady=5,command=getdollar).pack()
myslider2.pack()


root.mainloop()
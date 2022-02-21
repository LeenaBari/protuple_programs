from tkinter import *
img_root=Tk()
img_root.geometry("500x500")
photo=PhotoImage(file="C:\\Users\\leena\\Downloads\\ballon.png")
pic_label=Label(image=photo)
pic_label.pack()
img_root.mainloop()
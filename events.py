from tkinter import *
def leena(event):
    print(f"you cliked ont the button at {event.x},{event.y}")
root=Tk()
root.title("Events of tkinter")
root.geometry("644x334")
widget=Button(root,text='click me please')
widget.pack()
widget.bind('<Button-1>',leena)
widget.bind('<Double-1>',quit)
root.mainloop()
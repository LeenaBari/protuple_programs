from tkinter import *
root=Tk()
root.geometry("444x233")
root.title("My GUI")

# Important label option
# text=adds text
# bd=background
# fg=foreground
# font=set the font
# 1.font=("comisansms",19,"bold")
# 2.font=("comisansms 19 bold")


title_label=Label(text='''Python is a general-purpose programming language that can be used on any modern 
computer operating system. It can be used for processing text, numbers, images, scientific data and just
about anything else you might save on a computer. It is used daily in the operations of the Google search 
engine, the video-sharing website YouTube, NASA and the New York Stock Exchange. These are but a few of the 
places where Python plays important roles in the success of the business, government, and non-profit organizations; 
there are many others.''',bg="black",fg="white",padx=90,pady=90,font="comicsansms 19 bold",borderwidth=3,relief=SUNKEN)


# Important pack options
# anchor=nw
# side=top,bottom,left,right
# fill
# padx
# pady

title_label.pack(side=TOP,anchor="sw",fill=X)




root.mainloop()
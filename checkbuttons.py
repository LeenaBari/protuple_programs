from tkinter import *
root=Tk()

def getvals():
    print("It works")
root.geometry("644x344")
# heading
Label(root,text="Welcome to Travels",font="comicsansms 13 bold",pady=15).grid(row=0,column=3)

# text for forms
name=Label(root,text="Name")
phone=Label(root,text="Phone")
gender=Label(root,text="Gender")
emergency=Label(root,text="Emergency Contact")
paymentmode=Label(root,text="Payment Mode")

# pack the text
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
paymentmode.grid(row=5,column=2)

# variable for storing
namevalue=StringVar()
phonevalue=StringVar()
gendervalue=StringVar()
emergencyvalue=StringVar()
paymentmodevalue=StringVar()
foodservicevalue=IntVar()

# entry for form
nameentry=Entry(root,textvariable=namevalue)
phoneentry=Entry(root,textvariable=phonevalue)
genderentry=Entry(root,textvariable=gendervalue)
emergencyentry=Entry(root,textvariable=emergencyvalue)
paymentmodeentry=Entry(root,textvariable=paymentmodevalue)


# packing the entry
nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
emergencyentry.grid(row=4,column=3)
paymentmodeentry.grid(row=5,column=3)

# checkbox and packing
foodservice=Checkbutton(text="want to prebook your meal?",variable=foodservicevalue)
foodservice.grid(row=6,column=3)

# button and packing it
Button(text="Submit to travels",command=getvals).grid(row=7,column=3)
root.mainloop()
from tkinter import *
root=Tk()
canvas_width=800
canvas_height=400
root.geometry(f"{canvas_width}x{canvas_height}")
root.title("GUI")
can_widget=Canvas(root,width=canvas_width,height=canvas_height)
can_widget.pack()
can_widget.create_line(0,0,800,400,fill="green")
can_widget.create_line(0,400,800,0,fill="green")

can_widget.create_rectangle(3,5,700,300)
can_widget.create_text(200,200,text="python")
can_widget.create_oval(344,233,244,355)


root.mainloop()
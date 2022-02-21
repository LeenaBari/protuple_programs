from tkinter import *
root=Tk()
root.geometry("455x233")
root.title("Scrollbar Tutorial")
# for connecting scrollbar to widget
# 1.widget(yscrollbar=scrollbar.set)
# 2.scrollbar.config(command=widget.yview)
scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
listbox=Listbox(root,yscrollcommand=scrollbar.set)
for i in range(344):
    listbox.insert(END,f"Item{i}")
    listbox.pack(fill="both",padx=22)
    scrollbar.config(command=listbox.yview)

root.mainloop()
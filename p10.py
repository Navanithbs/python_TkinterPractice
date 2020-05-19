from tkinter import *
root=Tk()
hello=None
# create a toplevel menu
menubar = Menu(root)
# create a pulldown menu, and add it to the menu bar
filemenu = Menu(menubar)
filemenu.add_command(label="Open",command=hello)
filemenu.add_separator()
filemenu.add_command(label="Exit" ,command=root.destroy)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)
root.mainloop()

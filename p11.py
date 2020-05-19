from tkinter import *
root=Tk()
hello=None
menubar=Menu(root)
helloMenu = Menu(menubar)
helloMenu.add_command(label="Namaskar", command=hello)
menubar.add_cascade(label="Hello", menu=helloMenu)
# Create a submenu under the Hello Menu
subHello = Menu(helloMenu) # My parent is the helloMenu
subHello.add_command(label="English", command=hello) # Menu Item 1
subHello.add_command(label="Spanish", command=hello) # Menu Item 2
subHello.add_command(label="Chinese", command=hello) # Menu Item 3
subHello.add_command(label="French", command=hello) # Menu Item 4
# Add sub menu into parent with the label International Hello
helloMenu.add_cascade(label="Lanuages", menu=subHello)
root.config(menu=menubar)
root.mainloop()

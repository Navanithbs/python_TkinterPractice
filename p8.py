from tkinter import *
root = None
count = 0
def addButton(root,sideToPack):
 global count
 name = "Button "+ str(count) +" "+sideToPack
 button = Button(root, text=name)
 button.pack(side=sideToPack)
 count +=1
def hello():
 print("hello")
def main():
 global root
 root=Tk()
 for i in range(5):
 	addButton(root,LEFT)#left,right,buttom,top are the sides
 menubar = Menu(root)
 filemenu = Menu(menubar)
 filemenu.add_command(label="Open", command=hello)
 root.mainloop()
main() 

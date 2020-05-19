from tkinter import *
root = None
count = 0
def addButton(root,sideToPack):
 global count
 name = "Button "+ str(count) +" "+sideToPack
 button = Button(root, text=name)
 button.pack(side=sideToPack)
 count +=1
def main():
 global root
 root=Tk()
 frame1=Frame(root)
 for i in range(5):
 	addButton(root,LEFT)#left,right,buttom,top are the sides
 for i in range(5):
 	addButton(root,TOP)
 for i in range(5):
 	addButton(root,RIGHT)
 menubar = Menu(root)
 root.mainloop()
main() 

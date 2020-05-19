from tkinter import *
def bp():
	print("Button pushed")
root=Tk()
w=Label(root,text="hello world")
w.pack()
r=Button(root,text="red",command=bp)
r.pack()
b=Button(root,text="blue",command=bp)
b.pack()
root.mainloop()


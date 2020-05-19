from tkinter import *
def bp():
	root.destroy()
root=Tk()
w=Label(root,text="hello world")
w.pack()
r=Button(root,text="exit",command=bp)
r.pack()
tBox=Entry(root)
tBox.pack()
root.mainloop()


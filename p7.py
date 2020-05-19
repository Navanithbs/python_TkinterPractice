from tkinter import *
root=None
count=0
def create():
	global count
	count=count+1
	print("the btn clicked"" "+str(count)+" ""times")
	x=Entry(root)
	x.pack()
def main():
	global root
	root=Tk()
	x=Label(root,text="hello")
	x.pack()
	b=Button(root,text="save",command=create)
	b.pack()
	root.mainloop()
main()

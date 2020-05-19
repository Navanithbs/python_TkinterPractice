from tkinter import *
root=None
entrybox=None
def ButtonPushed():
	global entrybox
	txt=entrybox.get()
	print("the text is:",txt)
def create(parent):
	global entrybox
	entrybox=Entry(parent)
	entrybox.pack()
def main():
	global root
	root=Tk()
	x=Button(root,text="text",command=ButtonPushed)
	x.pack()
	create(root)
	root.mainloop()
main()

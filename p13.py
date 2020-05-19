from tkinter import *
def exit():
	root.destroy()
def disp():
	root.destroy()
def add_train():
	root.destroy()
def remove_train():
	root.destroy()	
root=Tk()
root.configure(bg='#40E0D0')

photo=PhotoImage(file='Railways.PGM')#declaration of photo
pic=PhotoImage(file='pic001.PGM')#declaration of photo

w=Label(root,text="---------------------------------------------------------")
w.pack()
w=Label(root,text="Railway Reservation Mangement System")
w.pack()
w=Label(root,text="---------------------------------------------------------")
w.pack()

#add a photo through canvas
myCanvas = Canvas(root, width=700, height=400)
myCanvas.pack()
myCanvas.create_image(0, 0,anchor=NW, image=photo)

w=Label(root,text="---------------------------------------------------------")
w.pack()
w=Label(root,text="click on the following options to proceed : ")
w.pack()
w=Label(root,text="---------------------------------------------------------")
w.pack()

p=Button(root,text="1.To view trains and timings",command=disp)
p.pack(side=TOP)
q=Button(root,text="2.To Add train",command=add_train)
q.pack(side=TOP)
s=Button(root,text="3.To remove train",command=remove_train)
s.pack(side=TOP)
r=Button(root,text="4.exit",command=exit)
r.pack(side=TOP)
x=Label(root,text="Comment Session :")
x.pack()
tBox=Entry(root)
tBox.pack()

#to add photo to label
#u=Label(root,image=pic)
#u.image=photo
#u.pack()

root.mainloop()

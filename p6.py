from tkinter import * 
root=None
text=None
count=0

def buttonPushed():
 global text
 global count
 count += 1
 print("Stop your clicking, it's already been %d times!" %(count)) #prints on terminal
 text.set("Stop your clicking, it's already been %d times!" %(count)) #prints on label


def addTextLabel(root):
 global text
 text = StringVar()
 text.set("")
 myLabel = Label(root, textvariable=text)
 myLabel.pack() 

def main():
 global root
 root = Tk()
 myButton = Button(root, text="Show Text",command=buttonPushed)
 myButton.pack()
 addTextLabel(root) 
 root.mainloop() 
main()

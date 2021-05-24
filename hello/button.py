import tkinter
import tkinter.messagebox as tkMessageBox
from playsound import playsound
top = tkinter.Tk()

def helloCallBack():
   tkMessageBox.showinfo( "Hello Python", "Hello World")


B = tkinter.Button(top, text ="Hello", command = helloCallBack)

B.pack()
top.mainloop()
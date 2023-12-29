from tkinter import *
import sys
L=[1]
def change(x,root):
    L.append(x)
    root.destroy()
def Play():
    root =Tk()
    root.title("main windows")
    root.geometry("500x500")
    
    GoToFirst=Button(root,text="play",command=lambda:[change(2,root)])
    CLS=Button(root,command=root.destroy,text="exit")
    GoToFirst.pack()
    CLS.pack()
    root.mainloop()
 
 
def ChooseLevel():
    root =Tk()
    root.geometry("500x500")
    root.title("level")
    Button(root,text="easy").pack()
    Button(root,text="midium").pack()
    Button(root,text="hard").pack()
    GoToSecond=Button(root,text="go Back",command=lambda:[change(1,root)])
    CLS=Button(root,command=root.destroy,text="exit")
    GoToSecond.pack()
    CLS.pack()
    root.mainloop()
 
 
while len(L):
    N=L.pop()
    if N==1:
        Play()
    else:
        ChooseLevel()
 
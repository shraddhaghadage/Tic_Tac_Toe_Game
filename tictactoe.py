import tkinter.messagebox
from tkinter import *

root =Tk()
root.geometry("1350*750+0+0")
root.tittle("TIC TAC TOE")
root.configure(background='Cadet Blue')

Tops = Frame(root, bg='Cadet Blue', pady=2, width=1350, height=100, relief=RIDGE)
Tops.grid(row=0, column=0)


lbTittle =Label(Tops, font=('arial',50,'bold'), text="Advance Tic Tac Toe Game", bd=21,bg='Cadet Blue',fg='Cronslik',justify=CENTER)
lbTittle.grid(row=0, column=0)

MainFrame = Frame(root, bg='Powder Blue', pady=2, width =1350, height=100, relief=RIDGE)
MainFrame.grid(row=1, column=0)

LeftFrame = Frame(MainFrame, bd=10, width=750, height=500, pady=2, padx=10, bg="Cadet Blue", relief=RIDGE)
LeftFrame.pack(side=LEFT)

RightFrame = Frame(MainFrame, bd=10, width=560, height=500, pady=10, padx=2, bg="Cadet Blue", relief=RIDGE)
RightFrame.grid(side=RIGHT)

RightFrame1 = Frame(MainFrame, bd=10, width=560, height=200, pady=10, padx=2, bg="Cadet Blue", relief=RIDGE)
RightFrame1.grid(row=0, column=0)

RightFrame2 = Frame(MainFrame, bd=10, width=560, height=200, pady=10, padx=2, bg="Cadet Blue", relief=RIDGE)
RightFrame2.grid(row=1, column=0)

root.mainloop()


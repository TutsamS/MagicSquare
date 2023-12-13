from tkinter import *
import magicSquareUI as msq
from tkinter import messagebox


#This is the main starting window that gets the size of the magic square

# This function gets the size from the test box and pass it to
# the createWindow method of magicSquareUI
def createMagicSquare():
   size = int(txtSize.get(1.0, 'end'))
   if size%2 == 1 and size >= 3:
       msq.createWindow(size)
   else:
       messagebox.showerror('Error', 'Size has to be a positive odd number greater than or equal to 3.')

# The main code
root = Tk()
root.title('Magic Square')
root.geometry('300x100')
lblSize = Label(root, text = "Enter a size.")
txtSize = Text(root,width=5, height=1)
txtSize.insert('end', str(3))
btnCreate = Button(root,
                     text="Create",
                     command=createMagicSquare)

lblSize.pack()
txtSize.pack()
btnCreate.pack()
root.mainloop()

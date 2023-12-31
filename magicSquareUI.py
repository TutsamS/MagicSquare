from tkinter import *
import tkinter.font as font
import magicSquareBackend as be


# The  UI that shows the magic square, the instructions and the buttons

# This function is called when the "Show Solution" button is clicked. It reads the correct
# values from the "matrix" (generated by  magicSquareBackend) and puts them in the UI grid
def showSolution(size, entrymatrix, matrix):
   for r in range(size):
       for c in range(size):
           e = entrymatrix[r][c]
           e.delete(0, END)
           e.insert(0, str(matrix[r][c]))


# This function is called when the "Check" button is clicked. Using the "matrix" (generated by  magicsquarebackend)
# and the values in the UI grid, it compares the value, if it is same highlights the cell with green, else with red
def check(size, entrymatrix, matrix):
   for r in range(size):
       for c in range(size):
           e = entrymatrix[r][c]
           v = e.get()
           if len(v) != 0:
               valueEntered = int(v)
               realValue = int(matrix[r][c])
               if valueEntered == realValue:
                   e.config(fg="green")
               else:
                   e.config(fg="red")
           else:
               e.config(fg="black")


# This function is called when the "Clear" button is clicked, it simples removes values
# from each cell and resets the highlights to white
def clear(size, entrymatrix, matrix):
   for r in range(size):
       for c in range(size):
           e = entrymatrix[r][c]
           e.delete(0, END)
           e.config(fg="black")


# This function is the core to create the magic square window based on the size
# of the magic square. It adds instructions at the top, then the grid of text boxes and
# finally  the buttons at the bottom
def createWindow(size=3):
   ms = Tk()
   ms.title('Magic Square')
   ms.config(bg='#add8e6')

   f = font.Font(family='Arial', size=20, weight='bold')
   g = font.Font(family='Arial', size=10, weight='bold')
   h = font.Font(family='Arial', size=12, weight='bold')

   myLabel = Label(ms, bg='#add8e6', wraplength=500,
       text="Welcome to the Magic Square game! The aim of this game is to "
            "think of numbers that will add up to the same number when "
            "adding a row, column, or diagonally. You must start with 1 and "
            "continue in chronological order, all numbers must be different. "
            "After filling in all of the boxes, press the 'Check' button to "
            "check your answer. If you're stuck, press the 'Show Solution' "
            "button and the values will appear. Try it yourself down below!")
   myLabel['font'] = g
   myLabel.grid(row=0, column=0)

   if size == 3:
       ms.geometry('500x400')
   elif size == 5:
       ms.geometry('645x550')
   else:
       ms.geometry('900x700')

   mainframe = Frame(ms, bg='#add8e6')

   entrymatrix = []

   # From the magicsquarebackend solve the square and store it into matrix
   matrix = be.solveSq(size)

   for r in range(size):
       row = []
       for c in range(size):
           e = Entry(mainframe, width=5, justify='center', font='Arial 20')
           e.grid(row=r, column=c, sticky='ew', ipadx=25, ipady=15)
           row.append(e)
       entrymatrix.append(row)

   mainframe.grid(row=1, column=0)

   buttonFrame = Frame(ms)
   button1 = Button(buttonFrame, text='Check', foreground='black', width=10,
                    command=lambda: check(size, entrymatrix, matrix))
   button1['font'] = f
   button1.grid(row=0, column=0)
   button2 = Button(buttonFrame, text='Clear', foreground='black', width=10,
                    command=lambda: clear(size, entrymatrix, matrix))
   button2['font'] = f
   button2.grid(row=0, column=1)
   buttonFrame.grid(row=2, column=0)

   button2 = Button(ms, text='Show Solution', bg='yellow',
                    foreground='black', width=15, command=lambda: showSolution(size, entrymatrix, matrix))
   button2['font'] = h
   button2.grid(row=3, column=0)

   ms.mainloop()


if __name__ == "__main__":
   createWindow(5)

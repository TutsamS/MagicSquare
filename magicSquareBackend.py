def nextCell(cell, size, movedown=2, moveright=1):
   row = cell[0]
   col = cell[1]
   newrow = (row + movedown) % size
   newcol = (col + moveright) % size
   return newrow, newcol


def initMgcsq(size):
   matrix = []
   for row in range(size):
       row = []
       for col in range(size):
           row.append(0)
       matrix.append(row)
   return matrix


def solveSq(size):
   if size % 2 != 1:
       print("Size must be an odd number.")
       return []
   matrix = initMgcsq(size)
   currentcell = (0, int(size/2))
   for n in range(1, (size**2)+1, 1):
       matrix[currentcell[0]][currentcell[1]] = n
       ncell = nextCell(currentcell, size)
       if matrix[ncell[0]][ncell[1]] != 0:
           currentcell = nextCell(currentcell, size, 1, 0)
       else:
           currentcell = ncell
   return matrix

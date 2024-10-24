def creategrid(row,column):
    grid = []
    for i in range(row):
      gridcolumn = []
      gridcolumn = ["" for i in range(column)]
      grid.append(gridcolumn)
    return grid
def checksize(name):
    rows = [len(row) for row in name]
    columns = rows[0]
    rows = len(name)
    print(f"There are {rows} rows and {columns} columns")
def printgrid(name):
    rows = [len(row) for row in name]
    rows = len(name)
    for i in range(0,rows):
        currentrow = "".join(str(name[i]))
        print(currentrow)
def getsize(name):
    rows = [len(row) for row in name]
    columns = rows[0]
    rows = len(name)
    return rows,columns

n = creategrid(9,9)
printgrid(n)

    
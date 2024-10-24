from gridfunctions import *
import random

grid = creategrid(9, 9)

def checkrow(row, num):
    for i in range(9):
        if grid[row][i] == num:
            return False
    return True

def checkcolumn(column, num):
    for i in range(9):
        if grid[i][column] == num:
            return False
    return True

def checkbox(row, column, num):
    rowstart = (row // 3) * 3
    colstart = (column // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[rowstart + i][colstart + j] == num:
                return False
    return True

rows = {f"rows{i}": ["1", "2", "3", "4", "5", "6", "7", "8", "9"] for i in range(9)}
columns = {f"columns{i}": ["1", "2", "3", "4", "5", "6", "7", "8", "9"] for i in range(9)}
boxes = {f"boxes{i}": ["1", "2", "3", "4", "5", "6", "7", "8", "9"] for i in range(9)}

for i in range(9):
    rownums = []
    for j in range(9):
        box = (i // 3) * 3 + (j // 3)
        numbers = list(set(rows[f"rows{i}"]) & set(columns[f"columns{j}"]) & set(boxes[f"boxes{box}"]))
        if not numbers:
            grid[i][j] = " "
            continue
        number = random.choice(numbers)
        try:
            rows[f"rows{i}"].remove(number)
            columns[f"columns{j}"].remove(number)
            boxes[f"boxes{box}"].remove(number)
            grid[i][j] = number
            rownums.append(number)
        except ValueError:
            grid[i][j] = " "
for x in range(65):
    while True:
        row = random.randint(0,8)
        column = random.randint(0,8)
        if grid[row][column] != " ":
            break
    grid[row][column] = " "
with open("suduko.txt", "w") as file:
    file.write("\n------------------------------------------------------\n")
    for row in grid:
        file.write("|  " + "  |  ".join(row) + "  |" + "\n------------------------------------------------------\n")

printgrid(grid)

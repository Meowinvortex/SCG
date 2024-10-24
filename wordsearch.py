global grid
import random
from gridfunctions import *


rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
grid = creategrid(rows, columns)

print("Start typing words\nType 'break' to stop\nSome words may be removed if they don't fit in the grid.")
words = []
allowed = "qwertyuioplkjhgfdsazxcvbnm"


while True:
    word = input()
    if word != "break":
        if any(i not in allowed for i in word):
            print("Invalid character found in word, please only use lowercase letters.")
        elif len(word) > rows or len(word) > columns:
            print("Word is too long for your grid")
        else:
            words.append(word)
    else:
        break


for i in range(1, len(words) + 1):
  loop = True
  while loop == True:
    pos = []
    word = list(words[i - 1])
    length = len(word)

    direction = random.randint(1, 8)
    
    if direction == 1:  # Upwards
        while True:
            startingrow = random.randint(length - 1, rows - 1)
            randomcolumn = random.randint(0, columns - 1)
            for j in range(length):
                if grid[startingrow - j][randomcolumn] == "":
                    pos.append([f"{startingrow - j} {randomcolumn}"])
                else:
                    pos = []
                    break
            if pos != []:
                break
                
    elif direction == 2:  # Downwards
        while True:
            startingrow = random.randint(0, rows - length)
            randomcolumn = random.randint(0, columns - 1)
            for j in range(length):
                if grid[startingrow + j][randomcolumn] == "":
                    pos.append([f"{startingrow + j} {randomcolumn}"])
                else:
                    pos = []
                    break
            if pos != []:
                break
                
    elif direction == 3:  # Leftwards
        while True:
            startingrow = random.randint(0, rows - 1)
            startingcolumn = random.randint(length - 1, columns - 1)
            for j in range(length):
                if grid[startingrow][startingcolumn - j] == "":
                    pos.append([f"{startingrow} {startingcolumn - j}"])
                else:
                    pos = []
                    break
            if pos != []:
                break
                
    elif direction == 4:  # Rightwards
        while True:
            startingrow = random.randint(0, rows - 1)
            startingcolumn = random.randint(0, columns - length)
            for j in range(length):
                if grid[startingrow][startingcolumn + j] == "":
                    pos.append([f"{startingrow} {startingcolumn + j}"])
                else:
                    pos = []
                    break
            if pos != []:
                break
                
    elif direction == 5:  # Diagonal up-left
        while True:
            startingrow = random.randint(length - 1, rows - 1)
            startingcolumn = random.randint(length - 1, columns - 1)
            for j in range(length):
                if grid[startingrow - j][startingcolumn - j] == "":
                    pos.append([f"{startingrow - j} {startingcolumn - j}"])
                else:
                    pos = []
                    break
            if pos != []:
                break
                
    elif direction == 6:  # Diagonal down-right
        while True:
            startingrow = random.randint(0, rows - length)
            startingcolumn = random.randint(0, columns - length)
            for j in range(length):
                if grid[startingrow + j][startingcolumn + j] == "":
                    pos.append([f"{startingrow + j} {startingcolumn + j}"])
                else:
                    pos = []
                    break
            if pos != []:
                break
                
    elif direction == 7:  # Diagonal up-right
        while True:
            startingrow = random.randint(length - 1, rows - 1)
            startingcolumn = random.randint(0, columns - length)
            for j in range(length):
                if grid[startingrow - j][startingcolumn + j] == "":
                    pos.append([f"{startingrow - j} {startingcolumn + j}"])
                else:
                    pos = []
                    break
            if pos != []:
                break
                
    elif direction == 8:  # Diagonal down-left
        while True:
            startingrow = random.randint(0, rows - length)
            startingcolumn = random.randint(length - 1, columns - 1)
            for j in range(length):
                if grid[startingrow + j][startingcolumn - j] == "":
                    pos.append([f"{startingrow + j} {startingcolumn - j}"])
                else:
                    pos = []
                    break
            if pos != []:
                break
    nooverlaps = True
    for check in range(len(pos)):
        position = ("".join(pos[check])).split()
        if grid[int(position[0])][int(position[1])] != "" and grid[int(position[0])][int(position[1])] != word[check]:
            nooverlaps = False
            break

        
        


    if nooverlaps == True:
       loop = False
       for x in range(len(word)):
          position = ("".join(pos[x])).split()
          grid[int(position[0])][int(position[1])] = word[x]

letters = ("".join(allowed))
for i in range(rows):
    for j in range(columns):
        if grid[i][j] == "":
            grid[i][j] = letters[random.randint(0,25)]
filename = input("Enter a name for your file: ")
file = open(f"{filename}.txt","w")
for i in range(rows):
    file.write(" ".join(grid[i]) + "\n")
file.write("\n\n\n\n")
for i in range(len(words)):
    file.write(words[i] + "\n")


        


    


    


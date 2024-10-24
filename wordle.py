white = "\033[0;37m" 
red = "\033[0;91m"
green = "\033[0;92m"
yellow = "\033[0;93m"
bold = "\033[1m"
import random
import os
import time
def clear():
    os.system("cls")
def format(x):
    string = bold
    for char in x:
        letter = char.split()
        if letter[0] == "red":
            string+=red + letter[1]
        elif letter[0] == "green":
            string+=green + letter[1]
        elif letter[0] == "yellow":
            string+=yellow + letter[1]
    print(string)
words = []
with open("words.txt", "r") as file:
    for lines in file:
        words.append(lines.strip())

word = list(random.choice(words))
userwords = []
print(word)
for i in range(5):
    correct = 0
    while True:
        print(white + "Type a 5-letter word:")
        user = list(input())
        if len(user) == 5 and ("".join(user)) in words:
            clear()
            for j in range(5):
                if user[j] == word[j]:
                    user[j] = "green " + user[j]
                    correct += 1
                elif user[j] in word:
                    user[j] = "yellow " + user[j]
                else:
                    user[j] = "red " + user[j]
            userwords.append(user)
            for sublists in userwords:
                format(sublists)
            break
        else:
            clear()
            print(red + "Invalid word")
            time.sleep(2)
            clear()
    if correct ==5:
        print(green + "Correct, well done!")
        break 
if correct != 5:
    print(red + "Out of guesses!")
    print("The word was " + "".join(word))
            
    


#  IMPORTS
from tkinter import *
import tkinter as tk
import time
import winsound
#  CONSTANTS
SCREEN_WIDTH  = 510
SCREEN_HEIGHT = 550
PLAYER = 2
EMPTY = 0
WALL = 1
coins=3
winsound.PlaySound("gamesound.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)

#  VARIABLES
grid =[
    
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 2, 1, 1, 0, 3, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 1, 0, 3, 1, 0, 1, 0, 1, 1, 0],
    [0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0],
    [0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
    [0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 3, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0],
    [0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 1, 1, 0, 3, 0, 0, 0, 1, 1, 0, 1, 1, 0],
    [0, 3, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0],
    [0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0],
    [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
    [0, 1, 0, 3, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 3, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    
]
#  FUNCTION
def arrayToDrawing():
    canvas.create_image(110,300, image=mybackground)
    for Y in range (len(grid)):
        for X in range  (len(grid[0])):
            x1 = (X * 30)
            x2 = 30 + x1
            y1 = (Y * 30)+40
            y2 = 30 + y1
            value = grid[Y][X]
            
            if value == WALL:
                color = ""
            if value == PLAYER:
                canvas.create_rectangle(x1,y1,x1+30,y1+30, fill="", outline="")
                canvas.create_image(x1+15,y1+15,image=Pacman)
            if value == EMPTY:
                color = ""
                canvas.create_image(x1+15,y1+15, image=walls)
            if value==3:
                
                canvas.create_rectangle(x1,y1,x1+30,y1+30,fill="",outline="")
                canvas.create_image(x1+15,y1+15,image=Images)
            canvas.create_rectangle(x1,y1,x2,y2,fill =color,outline="")
    countdown()
    return None
sum=0   
timeleft=30 
def timer():
    global timeleft
    timeleft -= 1
    canvas.after(1000, lambda:timer())
    canvas.after(1000, lambda:countdown())
def countdown(): 
    global sum
    canvas.delete("timer")
    canvas.create_text(40,20,fill="black",font="Times 16 italic bold",text="Score: "+str(sum))
    canvas.create_text(200,20,fill="black",font="Times 16 italic bold",text="Time Left: "+str(timeleft), tag ="timer")
def findPlayerPosition(grid) :
    canvas.delete("all") 
    for i in range(len(grid)):
        for n in range(len(grid[i])):
            if grid[i][n]== 2:
                position=[i,n]
    return position
def canGoRight(event):
    global sum
    position = findPlayerPosition(grid)
    p_column = position[1]
    p_row = position[0]
    old_value=0
    if grid[p_row][p_column+1]!=0:
        if grid[p_row][p_column+1]==coins:
            sum+=100
            # winsound.PlaySound("good_game.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
        grid[p_row][p_column]=1
        grid[p_row][p_column+1]=2
    if old_value==timeleft:
        winsound .PlaySound('slain.wav', winsound.SND_FILENAME)
        canvas.create_image(300,300,image=myLoser)
        messagebox.showinfo("Lost","You Lost!")
    arrayToDrawing()
    arrayToDrawing()
def canGoLeft(event):
    global sum
    position = findPlayerPosition(grid)
    p_column = position[1]
    p_row = position[0]
    old_value=0
    if grid[p_row][p_column-1]!=0:
        if grid[p_row][p_column-1]==coins:
            sum+=100
            # winsound .PlaySound('good_game.wav', winsound.SND_FILENAME)
        grid[p_row][p_column]=1
        grid[p_row][p_column-1]=2
    if old_value==timeleft:
        winsound .PlaySound('slain.wav', winsound.SND_FILENAME)
        canvas.create_image(300,300,image=myLoser)
        messagebox.showinfo("Lost","You Lost!")    
    arrayToDrawing()

def canGoUp(event):
    global sum, old_value
    position = findPlayerPosition(grid)
    p_column = position[1]
    p_row = position[0]
    old_value=0
    if grid[p_row-1][p_column]!=0:
        if grid[p_row-1][p_column]==coins:
            sum+=100
            # winsound .PlaySound('good_game.wav', winsound.SND_FILENAME)
        grid[p_row][p_column]=1
        grid[p_row-1][p_column]=2
 
    if old_value==timeleft:
        winsound .PlaySound('slain.wav', winsound.SND_FILENAME)
        canvas.create_image(300,300,image=myLoser)
    arrayToDrawing()


def canGoDown(event):
    canvas.delete("all")
    global sum
    position = findPlayerPosition(grid)
    p_column = position[1]
    p_row = position[0]
    old_value=0
    if grid[p_row+1][p_column]!=0:
        if grid[p_row+1][p_column]==coins:
            sum+=100
            # winsound .PlaySound('good_game.wav', winsound.SND_FILENAME)
        grid[p_row][p_column]=1
        grid[p_row+1][p_column]=2
    if old_value==timeleft:
        winsound .PlaySound('slain.wav', winsound.SND_FILENAME)
        canvas.create_image(300,300,image=myLoser)

    arrayToDrawing()


root = tk.Tk()
root.geometry(str(SCREEN_WIDTH)+"x"+str(SCREEN_HEIGHT))
canvas = tk.Canvas(root)
walls=tk.PhotoImage(file="myWall.png")
Images=tk.PhotoImage(file="gold1.png")
Pacman=tk.PhotoImage(file="image1.png")
mybackground=tk.PhotoImage(file='backg.png')
myLoser=tk.PhotoImage(file='over2.png')

root.bind("<Left>", canGoLeft) #LEFT CLICK
root.bind("<Right>", canGoRight)  #RIGHT CLICK
root.bind("<Up>", canGoUp) #Up CLICK
root.bind("<Down>", canGoDown)  #Down CLICK
# countdown()
canvas.pack(expand=True, fill="both")
timer()
arrayToDrawing()

root.mainloop()


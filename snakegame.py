#import dependencies
import turtle
import random

#create other turtles
grid = turtle.Turtle()
snake = turtle.Turtle()
apple = turtle.Turtle()
text = turtle.Turtle()

#variables
isdark = True

#coordinate map to place snake/apples
coordinateMap = {
  "x": {1: -215, 2: -190, 3: -165, 4: -140, 5: -115, 6: -90, 7: -65, 8: -40, 9: -15, 10: 10, 11: 35, 12: 60, 13: 85, 14: 110, 15: 135, 16: 160, 17: 185},
  "y": {1: 215, 2: 190, 3: 165, 4: 140, 5: 115, 6: 90, 7: 65, 8: 40, 9: 15, 10: -10, 11: -35, 12: -60, 13: -85, 14: -110, 15: -135}
}

snakePositionsX = [2, 3, 4]
snakePositionsY = [8, 8, 8]

global snakeLength
snakeLength = 3
global snakeDirection
snakeDirection = "right"

global appleX
global appleY
appleX = random.randint(1, 17)
appleY = random.randint(1, 15)

global hasStarted
hasStarted = False

global gameOver
gameOver = False

#functions
def up_move():
  global gameOver
  if snakePositionsY[-1] == 1:
    print("Border crash detected")
    gameOver = True
    return #
  snakePositionsX.append(snakePositionsX[-1])
  snakePositionsY.append(snakePositionsY[-1]-1)

def down_move():
  global gameOver
  if snakePositionsY[-1] == 15:
    print("Border crash detected")
    gameOver = True
    return #
  snakePositionsX.append(snakePositionsX[-1])
  snakePositionsY.append(snakePositionsY[-1]+1)

def right_move():
  global gameOver
  if snakePositionsX[-1] == 17:
    print("border crash detected")
    gameOver = True
    return #
  snakePositionsX.append(snakePositionsX[-1]+1)
  snakePositionsY.append(snakePositionsY[-1])

def left_move():
  global gameOver
  if snakePositionsX[-1] == 1:
    print("border crash detected")
    gameOver = True
    return #
  snakePositionsX.append(snakePositionsX[-1]-1)
  snakePositionsY.append(snakePositionsY[-1])

def direction_up():
  global snakeDirection
  if snakeDirection != "down":
    snakeDirection = "up"

def direction_down():
  global snakeDirection
  if snakeDirection != "up":
    snakeDirection = "down"

def direction_left():
  global snakeDirection
  if snakeDirection != "right":
    snakeDirection = "left"

def direction_right():
  global snakeDirection
  if snakeDirection != "left":
    snakeDirection = "right"

def start():
  global hasStarted
  if not hasStarted:
    hasStarted = True
    text.clear()
    text.goto(0, 222)
    text.write("Use arrow keys to move!", move=False, align="center", font=("Arial", 10, 'normal'))
    update()

def draw_snake():
  #draw new snake
  snake.clear()

  for pos in range(snakeLength):
    snake.penup()
    snake.setpos(coordinateMap["x"][snakePositionsX[pos]], coordinateMap["y"][snakePositionsY[pos]])
    snake.begin_fill()
    snake.pendown()

    for i in range(4):
      snake.forward(15)
      snake.right(90)

    snake.penup()
    snake.end_fill()

def draw_apple():
  #print new apple
  apple.clear()
  apple.penup()
  apple.goto(coordinateMap["x"][appleX], coordinateMap["y"][appleY])
  apple.pendown()
  apple.begin_fill()
  for i in range(4):
    apple.forward(15)
    apple.right(90)
  apple.end_fill()

#directions for calling move functions
directions = {
  "right": right_move,
  "left": left_move,
  "up": up_move,
  "down": down_move
}

#set colors
turtle.bgcolor("#90EE90")
grid.color("black")
grid.fillcolor("green")
snake.color("blue")
snake.fillcolor("blue")
apple.color("red")
apple.fillcolor("red")
text.color("white")

#hide turtles
snake.hideturtle()
grid.hideturtle()
turtle.hideturtle()
apple.hideturtle()
text.hideturtle()

#set some random things
grid.penup()
turtle.tracer(0,0)
grid.speed(0)
turtle.screensize(canvwidth=510, canvheight=510)

#draw grid
grid.setpos(-220,220)
for i in range(15):
  for i in range(17):
    
    if isdark:
      isdark = False
    else:
      isdark = True
      grid.begin_fill()
      
    for i in range(4):
      grid.pendown()
      grid.forward(25)
      grid.right(90)
    grid.end_fill()
    grid.penup()
    grid.forward(25)
  grid.right(90)
  grid.forward(25)
  grid.right(90)
  grid.forward(425)
  grid.right(180)

#check for key presses
turtle.onkeypress(direction_up, "Up")
turtle.onkeypress(direction_down, "Down")
turtle.onkeypress(direction_left, "Left")
turtle.onkeypress(direction_right, "Right")
turtle.onkeypress(start, "space")
turtle.listen()

#update every .5 seconds
def update():
  global appleX
  global appleY
  global snakeLength
  global gameOver
  
  #move snake in proper direction
  directions[snakeDirection]()
  
  #check for apple hit
  if snakePositionsX[-1] == appleX and snakePositionsY[-1] == appleY:
    snakeLength += 1
    appleX = random.randint(1, 17)
    appleY = random.randint(1, 15)
    
  #check for self-hit
  for i in range(len(snakePositionsX) - 1):
    if snakePositionsX[i] == snakePositionsX[-1] and snakePositionsY[i] == snakePositionsY[-1]:
      print("self-hit detected")
      print(snakePositionsX)
      print(snakePositionsY)
      gameOver = True
    
  #cut off end of snake
  if len(snakePositionsX) > snakeLength:
    snakePositionsX.pop(0)
    snakePositionsY.pop(0)
    
  draw_snake()

  draw_apple()
  
  if not gameOver:
    turtle.ontimer(update, 175)
  else:
    gameOverText = "Game over! Score: " + str(snakeLength - 3)
    text.goto(0, 0)
    text.write(gameOverText, move=False, align="center", font=("Arial", 25, 'normal'))

draw_snake()
draw_apple()
text.write("Press space to start", move=False, align="center", font=("Arial", 30, 'normal'))
turtle.mainloop()

#Import turtle package
import turtle

#Create, penup, and hide turtles
text = turtle.Turtle()
text.hideturtle()
text.penup()
text.goto(0, 230)

text2 = turtle.Turtle()
text2.hideturtle()
text2.penup()
text2.goto(0, 200)

text3 = turtle.Turtle()
text3.hideturtle()
text3.penup()
text3.goto(0, 170)

text4 = turtle.Turtle()
text4.hideturtle()
text4.penup()
text4.goto(0, 140)

towers = turtle.Turtle()
towers.hideturtle()
towers.penup()

disks = turtle.Turtle()
disks.penup()
disks.hideturtle()

#Set some random stuff
turtle.screensize(400, 400)
turtle.tracer(0,0)

#Set colors
turtle.bgcolor("lightblue")
towers.color("black")
towers.fillcolor("#ff8c00")
disks.color("black")
disks.fillcolor("#E97451")

#Create variables
global toMoveForward
toMoveForward = 0
global towerdisks
towerdisks = [[5, 4, 3, 2, 1], [], []]
global toChangeTower
toChangeTower = 0
global selected
selected = -1
global gameOver
gameOver = False
global gameStarted
gameStarted = False
global onDiskNumMenu
onDiskNumMenu = False

#Functions
def keyPress_1():
  global selected
  if not gameOver and gameStarted:

    if selected == -1:
      if len(towerdisks[0]) > 0:
        selected = 0
        text.clear()
        text2.clear()
        text3.clear()
        text.write("Select another tower to move disk!", move=False, align="center", font=("Arial", 8, "normal"))
        text2.write("Press 1 again to cancel.", move=False, align="center", font=("Arial", 8, "normal"))
      else:
        print("Nothing in tower to select!")
        text3.clear()
        text3.write("There is nothing in tower 1 to select!", move=False, align="center", font=("Arial", 8, "normal"))
  
    elif selected == 0:
      selected = -1
      text.clear()
      text2.clear()
      text3.clear()
      text.write("Use number keys 1-3 to select a tower!", move=False, align="center", font=("Arial", 8, "normal"))
    else:
    
      if len(towerdisks[selected]) > 0 and len(towerdisks[0]) > 0:
        if towerdisks[selected][-1] > towerdisks[0][-1]:
          print("Illegal move! Disk in tower selected is too big for this tower's top disk!")
          text3.clear()
          text3.write("You cannot place a disk on a smaller disk!", move=False, align="center", font=("Arial", 8, "normal"))
          return #
      text3.clear()
      towerdisks[0].append(towerdisks[selected][-1])
      del towerdisks[selected][-1]
      selected = -1
      text.clear()
      text2.clear()
      text3.clear()
      text.write("Use number keys 1-3 to select a tower!", move=False, align="center", font=("Arial", 8, "normal"))
      print("Successfully moved disk!")
      update()

def keyPress_2():
  global selected
  if not gameOver and gameStarted:

    if selected == -1:
      if len(towerdisks[1]) > 0:
        selected = 1
        text.clear()
        text2.clear()
        text3.clear()
        text.write("Select another tower to move disk!", move=False, align="center", font=("Arial", 8, "normal"))
        text2.write("Press 2 again to cancel.", move=False, align="center", font=("Arial", 8, "normal"))
      else:
        print("Nothing in tower to select!")
        text3.clear()
        text3.write("There is nothing in tower 2 to select!", move=False, align="center", font=("Arial", 8, "normal"))

    elif selected == 1:
      selected = -1
      text.clear()
      text2.clear()
      text3.clear()
      text.write("Use number keys 1-3 to select a tower!", move=False, align="center", font=("Arial", 8, "normal"))
    else:

      if len(towerdisks[selected]) > 0 and len(towerdisks[1]) > 0:
        if towerdisks[selected][-1] > towerdisks[1][-1]:
          print("Illegal move! Disk in tower selected is too big for this tower's top disk!")
          text3.clear()
          text3.write("You cannot place a disk on a smaller disk!", move=False, align="center", font=("Arial", 8, "normal"))
          return #

      text3.clear()
      towerdisks[1].append(towerdisks[selected][-1])
      del towerdisks[selected][-1]
      selected = -1
      text.clear()
      text2.clear()
      text3.clear()
      text.write("Use number keys 1-3 to select a tower!", move=False, align="center", font=("Arial", 8, "normal"))
      print("Successfully moved disk!")
      update()

def keyPress_3():
  global selected
  if not gameOver and gameStarted:

    if selected == -1:
      if len(towerdisks[2]) > 0:
        selected = 2
        text.clear()
        text2.clear()
        text3.clear()
        text.write("Select another tower to move disk!", move=False, align="center", font=("Arial", 8, "normal"))
        text2.write("Press 3 again to cancel.", move=False, align="center", font=("Arial", 8, "normal"))
      else:
        print("Nothing in tower to select!")
        text3.clear()
        text3.write("There is nothing in tower 3 to select!", move=False, align="center", font=("Arial", 8, "normal"))
    
    elif selected == 2:
      selected = -1
      text.clear()
      text2.clear()
      text3.clear()
      text.write("Use number keys 1-3 to select a tower!", move=False, align="center", font=("Arial", 8, "normal"))
    else:

      if len(towerdisks[selected]) > 0 and len(towerdisks[2]) > 0:
        if towerdisks[selected][-1] > towerdisks[2][-1]:
          print("Illegal move! Disk in tower selected is too big for this tower's top disk!")
          text3.clear()
          text3.write("You cannot place a disk on a smaller disk!", move=False, align="center", font=("Arial", 8, "normal"))
          return #

      text3.clear()
      towerdisks[2].append(towerdisks[selected][-1])
      del towerdisks[selected][-1]
      selected = -1
      text.clear()
      text2.clear()
      text3.clear()
      text.write("Use number keys 1-3 to select a tower!", move=False, align="center", font=("Arial", 8, "normal"))
      print("Successfully moved disk!")
      update()

def instructions():
  if not gameStarted:
    text.clear()
    text2.clear()
    text3.clear()
    text4.clear()
    text.write("Your goal is to move all disks to the 3rd tower.", move=False, align="center", font=("Arial", 8, "normal"))
    text2.write("You may only move the top disk from a tower. A disk cannot be placed on a smaller disk.", move=False, align="center", font=("Arial", 8, "normal"))
    text3.write("Use number keys 1-3 to select/move disks.", move=False, align="center", font=("Arial", 8, "normal"))
    text4.write("Press B to return to main menu.", move=False, align="center", font=("Arial", 8, "normal"))

def diskNumChange():
  global onDiskNumMenu
  if not gameStarted:
    onDiskNumMenu = True
    text.clear()
    text2.clear()
    text3.clear()
    text4.clear()
    insertText = str(len(towerdisks[0])) + " disks"
    text.write("Use up and down arrow keys to change disk number.", move=False, align="center", font=("Arial", 8, "normal"))
    text2.write("The maximum number of disks is 10.", move=False, align="center", font=("Arial", 8, "normal"))
    text3.write(insertText, move=False, align="center", font=("Arial", 8, "normal"))
    text4.write("Press B to return to main menu.", move=False, align="center", font=("Arial", 8, "normal"))

def solver():
  if not gameStarted:
    text.clear()
    text2.clear()
    text3.clear()
    text4.clear()
    text.write("Solver is not currently available!", move=False, align="center", font=("Arial", 8, "normal"))
    text2.write("Press B to return to main menu.", move=False, align="center", font=("Arial", 8, "normal"))

def begin():
  global gameStarted
  if not gameStarted:
    text.clear()
    text2.clear()
    text3.clear()
    text4.clear()
    gameStarted = True
    text.write("Use number keys 1-3 to select a tower!", move=False, align="center", font=("Arial", 8, "normal"))
    turtle.onkeypress(keyPress_1, "1")
    turtle.onkeypress(keyPress_2, "2")
    turtle.onkeypress(keyPress_3, "3")
    update()

def diskNumUp():
  if not gameStarted and onDiskNumMenu and len(towerdisks[0]) < 10:
    text3.clear()
    towerdisks[0].insert(0, towerdisks[0][0] + 1)
    insertText = str(len(towerdisks[0])) + " disks"
    text3.write(insertText, move=False, align="center", font=("Arial", 8, "normal"))

def diskNumDown():
  if not gameStarted and onDiskNumMenu and len(towerdisks[0]) > 1:
    text3.clear()
    del towerdisks[0][0]
    insertText = str(len(towerdisks[0])) + " disks"
    text3.write(insertText, move=False, align="center", font=("Arial", 8, "normal"))

def mainMenu():
  global onDiskNumMenu
  if not gameStarted:
    onDiskNumMenu = False
    text.clear()
    text2.clear()
    text3.clear()
    text4.clear()
    text.write("Press I to see instructions and rules.", move=False, align="center", font=("Arial", 8, "normal"))
    text2.write("Press C to change number of disks.", move=False, align="center", font=("Arial", 8, "normal"))
    text3.write("Press S to use the solver.", move=False, align="center", font=("Arial", 8, "normal"))
    text4.write("Press space to begin.", move=False, align="center", font=("Arial", 8, "normal"))
    #Runs update in case user was on disk number change menu
    update()

#Key press checks
turtle.onkeypress(instructions, "i")
turtle.onkeypress(diskNumChange, "c")
turtle.onkeypress(solver, "s")
turtle.onkeypress(begin, "space")
turtle.onkeypress(diskNumUp, "Up")
turtle.onkeypress(diskNumDown, "Down")
turtle.onkeypress(mainMenu, "b")
turtle.listen()

#Draw towers
towers.goto(-230, -230)
for i in range(3):
  towers.pendown()
  towers.begin_fill()
  towers.forward(120)
  towers.left(90)
  towers.forward(20)
  towers.left(90)
  towers.forward(50)
  towers.right(90)
  towers.forward(200)
  towers.left(90)
  towers.forward(20)
  towers.left(90)
  towers.forward(200)
  towers.right(90)
  towers.forward(50)
  towers.left(90)
  towers.forward(20)
  towers.penup()
  towers.end_fill()
  towers.left(90)
  towers.forward(170)

#Update disks on request
def update():
  global gameOver
  global toMoveForward
  global toChangeTower
  disks.clear()
  #Create disks on tower 1
  disks.goto(-230, -210)
  for h in range(3):
    toChangeTower = 170 * h
    toChangeTower = -230 + toChangeTower
    for q in range(len(towerdisks[h])):
      toMoveForward = 50 - (towerdisks[h][q] * 5)
      disks.forward(toMoveForward)
      disks.pendown()
      disks.begin_fill()
      for p in range(2):
        disks.forward(towerdisks[h][q] * 10 + 20)
        disks.left(90)
        disks.forward(20)
        disks.left(90)
      disks.penup()
      disks.end_fill()
      disks.left(90)
      disks.forward(20)
      disks.right(90)
      disks.goto(toChangeTower, disks.ycor())
    toChangeTower += 170
    disks.goto(toChangeTower, -210)

  #Check for win
  if len(towerdisks[0]) == 0 and len(towerdisks[1]) == 0:
    print("You win!")
    gameOver = True
    text.clear()
    text2.clear()
    text3.clear()
    text3.write("Congratulations! You win!", move=False, align="center", font=("Arial", 25, "normal"))

#Draws disks to start, creates text
text.write("Press I to see instructions and rules.", move=False, align="center", font=("Arial", 8, "normal"))
text2.write("Press C to change number of disks.", move=False, align="center", font=("Arial", 8, "normal"))
text3.write("Press S to use the solver.", move=False, align="center", font=("Arial", 8, "normal"))
text4.write("Press space to begin.", move=False, align="center", font=("Arial", 8, "normal"))
update()
#Keeps tab open
turtle.done()
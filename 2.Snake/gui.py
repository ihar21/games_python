from tkinter import *
from random import randint

class MaintInterface:
    def __init__(self):
        self.width=1000
        self.height=500
        self.win=Tk();
        self.win.geometry("{0}x{1}+0+0".format(self.width,self.height-17))
        self.field=Canvas(self.win,bg="gray",height=self.height,width=self.width)
        self.field.pack(side=BOTTOM)
        self.cellSize=40
        self.cells=[[self.field.create_rectangle(j*self.cellSize+0.5,\
        i*self.cellSize+0.5,(j+1)*self.cellSize-1,(i+1)*self.cellSize-1,fill="black")\
        for j in range((self.width//self.cellSize)+1)]for i in range((self.height//self.cellSize)+1)]
        self.win.bind('<Key>',self.dirChange)
        self.player=Snake()
        self.point = Point(self.width // self.cellSize, self.height // self.cellSize, self.player)
        self.draw()
        self.direction=0
        self.score=0
        self.death = False
        self.textScore = self.field.create_text(900, 20, fill="white", font="Fixedsys 20", text="Score:" + str(self.score))
        self.run()

    def run(self):
        self.clean()
        self.player.headMove(self.direction)
        if self.point.cheackTake():
            self.point.creatCoords()
            self.player.addSeg()
            self.score+=1
            self.updScore()
        self.player.move()
        self.draw()
        if not self.player.cheakDie(self.width // self.cellSize, self.height // self.cellSize):
            self.win.after(200,self.run)
        else:
            self.dead()

    def updScore(self):
        self.field.delete(self.textScore)
        self.textScore = self.field.create_text(900, 20, fill="white", font="Fixedsys 20",text="Score:" + str(self.score))

    def draw(self):
        for seg in self.player.segments:
            self.field.itemconfig(self.cells[seg.y][seg.x],fill="red")
        self.field.itemconfig(self.cells[self.point.y][self.point.x], fill="yellow")

    def clean(self):
        for i in self.cells:
            for j in i:
                if self.field.itemcget(j,'fill')=="red":
                    self.field.itemconfig(j,fill="black")

    def dead(self):
        self.death = True
        self.clean()
        self.textDie = self.field.create_text(500, 260, fill="white", font="Fixedsys 20", text="Press R to restart")
        del self.point

    def restart(self):
        for i in self.cells:
            for j in i:
                if self.field.itemcget(j,'fill')=="yellow":
                    self.field.itemconfig(j,fill="black")
        self.field.delete(self.textDie)
        self.direction = 0
        self.death = False
        self.player = Snake()
        self.point=Point(self.width // self.cellSize, self.height // self.cellSize, self.player)
        self.score = 0
        self.updScore()
        self.run()

    def dirChange(self, event):
        if event.keysym == "W" or event.keysym == "w" and self.direction != 3:
            self.direction = 2
        elif event.keysym == "S" or event.keysym == "s" and self.direction != 2:
            self.direction = 3
        elif event.keysym == "D" or event.keysym == "d" and self.direction != 0:
            self.direction = 1
        elif event.keysym == "A" or event.keysym == "a" and self.direction != 1:
            self.direction = 0
        if event.keysym == "R" or event.keysym == "r" and self.death:
            self.restart()

class Snake:
    def __init__(self,x=14,y=7):
        self.x=x
        self.y=y
        self.segments=[self.Segment(self.x,self.y),self.Segment(self.x+1,self.y),]
        self.ox = self.segments[0].x;self.oy = self.segments[0].y

    def headMove(self,direction):
        self.segments[0].ox=self.segments[0].x
        self.segments[0].oy = self.segments[0].y
        if direction == 0:
            self.segments[0].x -= 1
        elif direction == 1:
            self.segments[0].x += 1
        elif direction == 2:
            self.segments[0].y -= 1
        elif direction == 3:
            self.segments[0].y += 1

    def move(self):
        for i in range(1,len(self.segments)):
            self.segments[i].ox=self.segments[i].x
            self.segments[i].oy = self.segments[i].y
            self.segments[i].x=self.segments[i-1].ox
            self.segments[i].y = self.segments[i - 1].oy

    def cheakDie(self,width,height):
        if self.segments[0].x<0 or self.segments[0].x>=width:
            return True
        if self.segments[0].y<0 or self.segments[0].y>=height:
            return True
        for seg in range(1,len(self.segments)):
            if self.segments[0].x==self.segments[seg].x and self.segments[0].y==self.segments[seg].y:
                return True

    def addSeg(self):
        self.segments.append(self.Segment(self.x,self.y))

    class Segment:
        def __init__(self,x,y):
            self.x=x
            self.y=y
            self.ox=x
            self.oy=y

class Point:
    def __init__(self,fiw,fih,snake):
        self.xEnd=fiw
        self.yEnd=fih
        print(self.xEnd,self.yEnd)
        self.x = randint(0, self.xEnd-1)
        self.y = randint(0, self.yEnd-1)
        self.snakeLink=snake


    def creatCoords(self):
        self.x=randint(0,self.xEnd-1)
        self.y=randint(0,self.yEnd-1)
        for seg in self.snakeLink.segments:
            if self.x==seg.x and self.y==seg.y:
                self.creatCoords()
        print(self.x,self.y)

    def cheackTake(self):
        if self.snakeLink.segments[0].x==self.x and self.snakeLink.segments[0].y==self.y:
            return True

Interface=MaintInterface()
Interface.win.mainloop()
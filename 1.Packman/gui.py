from tkinter import *

class SomeObject:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __draw(self):
        global fileld
        if self.have:
            fileld.delete(self.body)
        self.body=fileld.create_oval(self.x,self.y,self.x+self.size,self.y+self.size,fill=self.color,outline=self.color)

class Packman(SomeObject):
    def __init__(self,x,y,speed,size=30,color="yellow"):
        super().__init__(x,y)
        self.speed=speed
        self.color=color
        self.size=size
        self.have = False
        super()._SomeObject__draw()
        self.have = True

    def move(self,x,y):
        self.x+=x*self.speed
        self.y+=y*self.speed
        super()._SomeObject__draw()

class Point(SomeObject):
    def __init__(self,x,y,size,cost,color="orange"):
        super().__init__(x, y)
        self.size=size
        self.cost=cost
        self.color=color
        self.have=False
        self.body=None
        super()._SomeObject__draw()
        self.have=True

    def cheakDie(self,other):
        global score
        if self.have:
            if type(other)==Packman:
                if (self.x>other.x and self.x+self.size<other.x+other.size) and (self.y>other.y and self.y+self.size<other.y+other.size):
                    return True
    def __del__(self):
        global fileld
        print("d")
        fileld.delete(self.body)
        #self.__dict__.clear()

class Wall(SomeObject):
    def __init__(self,x,y,x1,y1):
        super().__init__()


def moving(event):
    global player,testPoint,score
    if (event.keysym=="W" or event.keysym=="w") and player.y>0:
        player.move(0,-5)
    elif (event.keysym=="S" or event.keysym=="s") and player.y<h-player.size:
        player.move(0,5)
    elif (event.keysym == "D" or event.keysym == "d") and player.x<w-player.size:
        player.move(5,0)
    elif (event.keysym == "A" or event.keysym == "a") and player.x>0:
        player.move(-5,0)
    # one item eror
    if testPoint.have and testPoint.cheakDie(player):
        score+=1
        del testPoint
    text_upd()


def text_upd():
    global fileld,textScore
    fileld.delete(textScore)
    textScore = fileld.create_text(1570, 20, fill="white", font="Fixedsys 20", text="Score:" + str(score))

w=1680;h=1020;score=0
win=Tk()
win.attributes('-fullscreen', True)
fileld=Canvas(win,width=w,height=h,bg="black")
exbut=Button(win,text="x",height=0,width=1,bg="red",command=win.destroy)
fileld.pack(side=BOTTOM)
exbut.place(x=1663)
win.bind('<Key>',moving)
player=Packman(300,300,2,50)
testPoint=Point(400,400,10,10)
textScore=fileld.create_text(1570,20,fill="white",font="Fixedsys 20",text="Score:"+str(score))
win.mainloop()

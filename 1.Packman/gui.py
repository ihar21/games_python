from tkinter import *
class Packman:
    have=False
    def __init__(self,x,y,speed,size=30,color="yellow"):
        self.x=x
        self.y=y
        self.speed=speed
        self.color=color
        self.size=size
        Packman.__draw(self)
        Packman.have = True

    def __draw(self):
        global fileld
        if Packman.have:
            fileld.delete(self.body)
        self.body=fileld.create_oval(self.x,self.y,self.x+self.size,self.y+self.size,fill=self.color,outline=self.color)

    def move(self,x,y):
        self.x+=x*self.speed
        self.y+=y*self.speed
        Packman.__draw(self)

class Point:
    def __init__(self,x,y,size,cost,color="orange"):
        self.x=x
        self.y=y
        self.size=size
        self.cost=cost
        self.color=color
        self.have=False
        Point.__draw(self)
        self.have=True

    def __draw(self):
        global fileld
        if self.have:
            fileld.delete(self.body)
        self.body=fileld.create_oval(self.x,self.y,self.x+self.size,self.y+self.size,fill=self.color,outline=self.color)

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

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

def moving(event):
    global player
    if (event.keysym=="W" or event.keysym=="w") and player.y>0:
        player.move(0,-5)
    elif (event.keysym=="S" or event.keysym=="s") and player.y<h-player.size:
        player.move(0,5)
    elif (event.keysym == "D" or event.keysym == "d") and player.x<w-player.size:
        player.move(5,0)
    elif (event.keysym == "A" or event.keysym == "a") and player.x>0:
        player.move(-5,0)

w=1680;h=1020
win=Tk()
win.attributes('-fullscreen', True)
fileld=Canvas(win,width=w,height=h,bg="black")
exbut=Button(win,text="x",height=0,width=1,bg="red",command=win.destroy)
fileld.pack(side=BOTTOM)
exbut.place(x=1663)
win.bind('<Key>',moving)
player=Packman(300,300,2,50)
win.mainloop()

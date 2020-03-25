from tkinter import *

class MaintInterface:
    def __init__(self):
        self.width=1000
        self.height=600
        self.win=Tk();
        self.win.geometry("{0}x{1}+0+0".format(self.width,self.height))
        self.field=Canvas(self.win,bg="black",height=self.height,width=self.width)
        self.field.pack(side=BOTTOM)
        self.win.bind("<Key>",self.dirChange)
        self.size=30
        self.player=Snake()
        self.body=[]
        self.direction = 0
        for i in range(len(self.player.segments)):
            self.body.append(self.field.create_rectangle(self.player.segments[i]["x"],self.player.segments[i]["y"],\
            self.player.segments[i]["x"]+self.size,self.player.segments[i]["y"]+self.size,fill=self.player.color))
        self.sc=0
        self.draw()

    def draw(self):
        self.player.firstmove(self.direction)
        for i in range(len(self.body)):
            self.player.move(self.sc,self.direction)
            self.field.coords(self.body[i],self.player.segments[i]["x"],self.player.segments[i]["y"],\
            self.player.segments[i]["x"]+self.size,self.player.segments[i]["y"]+self.size)
            #self.field.create_rectangle(self.player.segments[i]["x"],self.player.segments[i]["y"],\
            #self.player.segments[i]["x"]+self.size,self.player.segments[i]["y"]+self.size,fill=self.player.color)
        self.sc+=1
        if self.sc>len(self.player.segments)-1:self.sc=0
        self.win.after(100,self.draw)



    def dirChange(self, event):
        if event.keysym == "W" or event.keysym == "w" and self.direction!=3:
            self.direction = 2
        elif event.keysym == "S" or event.keysym == "s" and self.direction!=2:
            self.direction = 3
        elif event.keysym == "D" or event.keysym == "d" and self.direction!=0:
            self.direction = 1
        elif event.keysym == "A" or event.keysym == "a" and self.direction!=1:
            self.direction = 0
        self.sc=0



class Snake:
    def __init__(self):
        self.x=300
        self.y=500
        self.color="red"
        #0-left1-right2-up3-down
        #self.direction=0
        self.segments=[{"x":self.x+i*10,"y":self.y} for i in range(3)]

    def firstmove(self,direction):
        mod = 20
        if direction==0:
            self.segments[0]["x"]-=mod
        elif direction==1:
            self.segments[0]["x"]+=mod
        elif direction==2:
            self.segments[0]["y"] -= mod
        elif direction==3:
            self.segments[0]["y"] += mod

    def move(self,segment,direction):
        if segment!=0:
            self.segments[segment]["x"]=self.segments[segment-1]["x"]
            self.segments[segment]["y"]=self.segments[segment-1]["y"]
            if direction == 0:
                self.segments[segment]["x"] += 20
            elif direction == 1:
                self.segments[segment]["x"] -= 20
            elif direction == 2:
                self.segments[segment]["y"] += 20
            elif direction == 3:
                self.segments[segment]["y"] -= 20






Interface=MaintInterface()
Interface.win.mainloop()
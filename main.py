from tkinter import *

class Window(Tk):
    def __init__(self):
        super().__init__()
        self.player = "X"
        self.score = {"X":0,"0":0}
        self.resizable(False,False)
        self.title("Tick-Tack-Toe")
        self.create()

    def create(self):
        #creating gaming field
        self.reset_btt = Button(self,text="RESET", command=self.reset, width=15,height=3)
        self.player_label = Label(self,text="It`s your turn, "+self.player,height="2",font="San-Serif, 20")
        self.score_label = Label(self,font="San-Serif, 18",text="Score:\nX: {}\n0: {}".format(str(self.score["X"]),str(self.score["0"])))
        self.score_label.grid(row=1,column=1)
        self.player_label.grid(row=1,column=2)
        self.A1 = Butt(self,"A1")
        self.A2 = Butt(self,"A2")
        self.A3 = Butt(self,"A3")
        self.B1 = Butt(self,"B1")
        self.B2 = Butt(self,"B2")
        self.B3 = Butt(self,"B3")
        self.C1 = Butt(self,"C1")
        self.C2 = Butt(self,"C2")
        self.C3 = Butt(self,"C3")
        self.A1.grid(row=2,column=1)
        self.A2.grid(row=2,column=2)
        self.A3.grid(row=2,column=3)
        self.B1.grid(row=3,column=1)
        self.B2.grid(row=3,column=2)
        self.B3.grid(row=3,column=3)
        self.C1.grid(row=4,column=1)
        self.C2.grid(row=4,column=2)
        self.C3.grid(row=4,column=3)
        self.reset_btt.grid(row=1, column=3)

    def reset(self):
        #when the game is over, reset the field
        self.A1.reset()
        self.A2.reset()
        self.A3.reset()
        self.B1.reset()
        self.B2.reset()
        self.B3.reset()
        self.C1.reset()
        self.C2.reset()
        self.C3.reset()
        self.player = "X"
        self.player_label['text'] = "It`s your turn, "+self.player
        self.score_label['text'] = "Score:\nX: {}\n0: {}".format(str(self.score["X"]), str(self.score["0"]))

    def press(self, btt):
        btt.button_pressed(self.player)
        self.is_winner()

    def winner(self,win):
        self.score[win]+=1
        self.reset()

    def crossed(self,dominator):
        if dominator:
            if self.A1.value==self.B2.value==self.C3.value==dominator: self.winner(dominator)
            elif self.A3.value==self.B2.value==self.C1.value==dominator: self.winner(dominator)

    def is_winner(self):
        #This func scans three rows, three columns and two roods to find a winner
        f = ["A","B","C"] # A,B,C are the names of rows
        for i in f:
            dominator = eval("self."+i+"1.value")
            if not dominator: continue
            for k in range(2,4):
                if eval("self."+i+str(k)+".value") != dominator:
                    break
                if k == 3:
                    self.winner(dominator)
        for i in range(1,4):
            for k in f:
                dominator = eval("self." +"A" + str(i) + ".value")
                if not dominator: continue
                if eval("self."+k+str(i)+".value") != dominator:
                    break
                if k == "C":
                    self.winner(dominator)
        dominator = self.A1.value
        self.crossed(dominator)
        dominator = self.A3.value
        self.crossed(dominator)


class Butt(Button): # yep, i know what butt is
    def __init__(self,root,name):
        self.name=name
        self.root = root
        super().__init__(self.root,text="",command = self.press)
        self.value = None
        self["width"] = 13
        self["height"] = 8
        self["font"] = "San-Serif, 14"

    def button_pressed(self, player):
        if not self.value:
            self.value = player
            self['text'] = self.value
            self.change_player()
        else:
            pass

    def change_player(self):
        if self.root.player == "X": self.root.player = "0"
        else: self.root.player = "X"
        self.root.player_label['text'] = "It`s your turn, "+self.root.player

    def reset(self):
        self.value = None
        self['text'] = ""

    def press(self):
        self.root.press(self)

root = Window()
root.mainloop()

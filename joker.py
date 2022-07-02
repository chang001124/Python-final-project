import random
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter import messagebox
class joker:

    class Card:
        def __init__(self, color, number):
            self.color = color      
            self.number = number    
        def __repr__(self):
            return self.color+self.number   
        
    pokers = []
    new_card=[]
    card=[]
    player1=[]
    player2 =[]
    player3=[]

    def __init__(self,master):
        frame=Frame(master)
        frame.place()
        frame.grid()
        numberList = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        # For simpler design, we only use RED and BLACK to seperate the card.
        for c in ["S", "H", "D", "F"]: 
            for n in numberList:
                self.pokers.append(self.Card(c, n))
        number=["Joker"]
        for c in ["B", "R"]: 
            for n in number:
                self.pokers.append(self.Card(c, n))
        # The list discards will be a list of 26 red Cards and 26 black Cards
        self.shuffle()
        self.draw(18) 
        self.throw1(self.player1)
        self.throw2(self.player2)
        self.throw3(self.player3)
        self.start()
        
    
    def throw1(self,player1):
        numberList = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        j=0
        color=["B", "R"]
        while(j!=len(numberList)):
            for i in range(len(self.player1)):
                if(self.player1[i].number==numberList[j]):
                    self.new_card.append(self.player1[i])
            while(True):
                if(len(self.new_card)>=2):
                    self.new_card.pop(0)
                    self.new_card.pop(0)
                else:
                    for k in range(len(self.new_card)):
                        self.card.append(self.new_card[k])
                    self.new_card.clear()
                    break
            j+=1
        j=0
        while(j!=len(color)):
            for i in range(len(self.player1)):
                if(self.player1[i].color==color[j]):
                    self.card.append(self.player1[i])
            j+=1
        self.player1.clear()
        for i in range(len(self.card)):
            self.player1.append(self.card[i])
 
        random.shuffle(self.player1)
        self.card.clear()
        self.new_card.clear()
    
    
    def throw2(self,player2):
        numberList = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        j=0
        color=["B", "R"]
        while(j!=len(numberList)):
            for i in range(len(self.player2)):
                if(self.player2[i].number==numberList[j]):
                    self.new_card.append(self.player2[i])
            while(True):
                if(len(self.new_card)>=2):
                    self.new_card.pop(0)
                    self.new_card.pop(0)
                else:
                    for k in range(len(self.new_card)):
                        self.card.append(self.new_card[k])
                    self.new_card.clear()
                    break
            j+=1
        j=0
        while(j!=len(color)):
            for i in range(len(self.player2)):
                if(self.player2[i].color==color[j]):
                    self.card.append(self.player2[i])
            j+=1
        self.player2.clear()
        for i in range(len(self.card)):
            self.player2.append(self.card[i])

        random.shuffle(self.player2)
        self.card.clear()
        self.new_card.clear()


    def throw3(self,player3):
        numberList = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        j=0
        color=["B", "R"]
        while(j!=len(numberList)):
            for i in range(len(self.player3)):
                if(self.player3[i].number==numberList[j]):
                    self.new_card.append(self.player3[i])
            while(True):
                if(len(self.new_card)>=2):
                    self.new_card.pop(0)
                    self.new_card.pop(0)
                else:
                    for k in range(len(self.new_card)):
                        self.card.append(self.new_card[k])
                    self.new_card.clear()
                    break
            j+=1
        j=0
        while(j!=len(color)):
            for i in range(len(self.player3)):
                if(self.player3[i].color==color[j]):
                    self.card.append(self.player3[i])
            j+=1
        self.player3.clear()
        for i in range(len(self.card)):
            self.player3.append(self.card[i])
        random.shuffle(self.player3)
        self.card.clear()
        self.new_card.clear()
        
        
    def shuffle(self):
        random.shuffle(self.pokers)


    def draw(self, count):
        for i in range(count):
            self.player1.append(self.pokers.pop(0))
            self.player2.append(self.pokers.pop(0))
            self.player3.append(self.pokers.pop(0))
    

    def start(self):
        list2 = []
        list=['tittle','card','takeplayer','take','choose','get']
        global turn
        turn=random.randint(1,3)
        
        def reduce():
            list2[0].destroy()
            list2[1].destroy()
            list2[2].destroy()
            setst()
            go()
        def pop_up():
            messagebox.showinfo("Rule", "1.每個玩家手上會已經會有整理過後的牌子\n2.3個玩家輪流抽排\n3.抽到一樣時候，電腦會自動幫你打出去\n4.最先打完手上的牌，即可獲勝")
            
        tittle=tk.Label(root,text="Welcome  to  joker  game!",font=("Ariel",20,"bold"))
        tittle.place(relx = 0.5, rely = 0.3, anchor = CENTER)
        list2.append(tittle)
        startbutton=Button(root,text="start",height=1,width=5,fg = "red",font=("Ariel",20,"bold"),command=reduce)
        startbutton.place(relx = 0.5, rely = 0.5, anchor = CENTER)
        list2.append(startbutton)
        
        jump=Button(root, text="Rule",height=1,width=5,font=("Ariel",15,"bold"),command= pop_up)
        jump.place(relx = 0.5, rely = 0.7, anchor = CENTER)
        list2.append(jump)
        def turnto():
            global turn   
            turn+=1
            if(turn>3):
                turn=1
            list[0]["text"]=""
            list[1]["text"]=""    
            go()
        
        def setst():
             list[0]=tk.Label(root,text="",font=("Ariel",15,"bold"))
             list[0].place(relx = 0.5, rely = 0.1, anchor = CENTER)
             tk.Label(root,text="My card",font=("Ariel",16,"bold"),fg = "blue").place(relx = 0.5, rely = 0.75, anchor = CENTER)
             list[1]=tk.Label(root,text="",font=("Ariel",12,"bold"),fg = "blue")
             list[1].place(relx = 0.5, rely = 0.85, anchor = CENTER)
             list[2]=tk.Label(root,text="",font=("Ariel",12,"bold"),fg = "green")
             list[2].place(relx = 0.5, rely = 0.30, anchor = CENTER)
             list[3]=tk.Label(root,text="",font=("Ariel",12,"bold"),fg = "green")
             list[3].place(relx = 0.5, rely = 0.45, anchor = CENTER)
             list[4]=ttk.Combobox(root,values=["1"],font=("Ariel",12,"bold"))
             list[4].place(relx = 0.5, rely = 0.62, anchor = CENTER)
             list[4].current(0)
             list[5]=tk.Label(root,text="",font=("Ariel",12,"bold"),fg = "red")
             list[5].place(relx = 0.5, rely = 0.53, anchor = CENTER)
        
        def check1():
            idx=int(list[4].get())
            list[5]["text"]="You get  {}".format(self.player2[idx-1])
            self.player1.append(self.player2.pop(idx-1))
            self.throw1(self.player1)
            Button(root,text="OK",height=1,width=5,fg = "red",font=("Ariel",15,"bold"),command=win).place(relx = 0.80, rely = 0.55)
            
        def check2():
            idx=int(list[4].get())
            list[5]["text"]="You get  {}".format(self.player3[idx-1])
            self.player2.append(self.player3.pop(idx-1))
            self.throw2(self.player2)
            Button(root,text="OK",height=1,width=5,fg = "red",font=("Ariel",15,"bold"),command=win).place(relx = 0.80, rely = 0.55)
       
        def check3():
            idx=int(list[4].get())
            list[5]["text"]="You get  {}".format(self.player1[idx-1])
            self.player3.append(self.player1.pop(idx-1))
            self.throw3(self.player3)
            Button(root,text="OK",height=1,width=5,fg = "red",font=("Ariel",15,"bold"),command=win).place(relx = 0.80, rely = 0.55)
        
        def win():
            if(len(self.player1)==0):
                list[0]["text"]="player 1 win!!!"
                list[0]["font"]=("Ariel",25,"bold")
                list[0]["fg"]="red"
                Button(root,text="LEAVE",height=1,width=5,fg = "red",font=("Ariel",15,"bold"),command=root.quit).place(relx = 0.80, rely = 0.55)
            elif(len(self.player2)==0):
                list[0]["text"]="player 2 win!!!"
                list[0]["font"]=("Ariel",25,"bold")
                list[0]["fg"]="red"
                Button(root,text="lEAVE",height=1,width=5,fg = "red",font=("Ariel",15,"bold"),command=root.quit).place(relx = 0.80, rely = 0.55)
            elif(len(self.player3)==0):
                list[0]["text"]="player 3 win!!!"
                list[0]["font"]=("Ariel",25,"bold")
                list[0]["fg"]="red"
                Button(root,text="lEAVE",height=1,width=5,fg = "red",font=("Ariel",15,"bold"),command=root.quit).place(relx = 0.80, rely = 0.55)
            else:
                turnto()
        
            
        def go():
            list[5]["text"]=""
            temp=""
            val=[]
            val.clear()
            if turn==1:
                print("player 2 card:",self.player2)
                list[0]["text"]="Player 1's Round"
                list[1]["text"]=self.player1
                Button(root,text="OK",height=1,width=5,fg = "red",font=("Ariel",15,"bold"),command=check1).place(relx = 0.80, rely = 0.55)
                for i in range(len(self.player2)):
                    temp+=str(i+1)+"　"
                    val.append(i+1)
                list[2]["text"]="player  2  card:\n(please choose one)"
                list[3]["text"]=temp
                list[4]["values"]=val
                list[4].current(0)
            elif turn==2:
                print("player 3 card:",self.player3)
                list[0]["text"]="Player 2's Round"
                list[1]["text"]=self.player2
                Button(root,text="OK",height=1,width=5,fg = "red",font=("Ariel",15,"bold"),command=check2).place(relx = 0.80, rely = 0.55)
                for i in range(len(self.player3)):
                    temp+=str(i+1)+"　"
                    val.append(i+1)
                list[2]["text"]="player  3  card:\n(please choose one)"
                list[3]["text"]=temp
                list[4]["values"]=val
                list[4].current(0)
            else:
                print("player 1 card:",self.player1)
                list[0]["text"]="Player 3's Round"
                list[1]["text"]=self.player3
                Button(root,text="OK",height=1,width=5,fg = "red",font=("Ariel",15,"bold"),command=check3).place(relx = 0.80, rely = 0.55)
                for i in range(len(self.player1)):
                    temp+=str(i+1)+"　"
                    val.append(i+1)
                list[2]["text"]="player  1  card:\n(please choose one)"
                list[3]["text"]=temp
                list[4]["values"]=val
                list[4].current(0)
        

root=tk.Tk()
root.title("Joker")
root.geometry("400x300")
B=joker(root)
root.mainloop()
# to do: make size of the mall map dependent on NameMall.Mall() characteristics
#add stores
from Mall import *
from Stores import *
import tkinter as tk
window =tk.Tk()





frm=tk.Frame(window, relief = tk.RIDGE, borderwidth=5)
frm.pack(side=tk.TOP)
greeting = tk.Label(frm, text="Bootleg Mall Game",
           fg = "pink",
           bg = "white" )
greeting.pack()

def Robo():
    RoboWindow=tk.Tk()
    robo_lbl=tk.Label(RoboWindow,text=OnlineRobot.getPhrase(0),fg='green')
    robo_lbl.pack()
    
    def opentxt(x):
        window=tk.Tk()
        if x==3:
            lbl=tk.Label(window,text="These are our stores. Click for additional information.")
            lbl.pack()
        else:
            lbl=tk.Label(window,text=OnlineRobot.getPhrase(x))
            lbl.pack()
        window.mainloop()

    robo_frm=tk.Frame(RoboWindow,width=200,height=300)
    robo_frm.pack()
    coord=0
    userQuestions=["How many floors are there?", 
                    "What city are you located in?",
                    "What stores do you have?",
                    "How many stores are there?",
                    "Is the parking lot busy?"]
    for i in range(len(userQuestions)):

        robo_btn=tk.Button(robo_frm,text=userQuestions[i],command=lambda i=i:opentxt(i+1))
        robo_btn.place(x=0,y=coord)
        coord+=50

    
    

    RoboWindow.mainloop()


def OpenInventory():
    inventory_window=tk.Tk()
    inventory=tk.Label(inventory_window,text='This is your inventory')
    inventory.pack()

    inventory_window.mainloop()

def OpenMall():
    window2=tk.Tk()
    window2.rowconfigure([0,1,2],weight=1)
    window2.columnconfigure([0,1,2],weight=1)
    centerMain_frm=tk.Frame(window2)
    centerMain_txt=tk.Label(centerMain_frm,
                            text='You are in the mall.' ,
                            fg="pink",
                            bg="white")
    centerMain_txt.pack()
    leave_btn=tk.Button(centerMain_frm,text="Leave?",
                        fg="pink",
                        bg="white",
                        command = window2.destroy)
    leave_btn.pack()
    btn_store=[]

    for store in TSt:
        btn_store.append(tk.Button(window2, 
                                    text = store.getStoreName(),
                                    width= 15,
                                    height= 5,
                                    fg="pink",
                                    bg="white"))
    
    j=0
    for c in range(3):
        for r in range(3):
            if c ==1 and r == 1:
                centerMain_frm.grid(row=r, column=c)
            else:
                btn_store[j].grid(row=r,column=c,sticky="nsew")
                j+=1

  
    
    window2.mainloop()

def MyHouse():
    windowHouse=tk.Tk()
    windowHouse.rowconfigure([0,1],weight=1)
    windowHouse.columnconfigure([0,1,2],weight=1)
    home_btns=["The Internet", 'Go to the mall','Inventory']
    internet_frm=tk.Frame(windowHouse,relief=tk.GROOVE,borderwidth=5)
    internet_frm.grid(row=0,column=0)

    mall_frm=tk.Frame(windowHouse,relief=tk.GROOVE,borderwidth=5)
    mall_frm.grid(row = 0,column=2)

    inventory_frm=tk.Frame(windowHouse,relief=tk.GROOVE,borderwidth=5)
    inventory_frm.grid(row=1,column=1)

    internet_btn=tk.Button(internet_frm,text=home_btns[0],fg='pink',bg='white',command=Robo)
    internet_btn.pack()

    inventory_btn=tk.Button(inventory_frm,text=home_btns[2],fg='pink',bg='white',command=OpenInventory)
    inventory_btn.pack()

    mall_btn=tk.Button(mall_frm,text=home_btns[1],fg='pink',bg='white',command=OpenMall)
    mall_btn.pack()



    windowHouse.mainloop()

startBtnFrm=tk.Frame(window, relief=tk.RAISED,borderwidth=5)
startBtnFrm.pack()
startBtn = tk.Button(startBtnFrm, text = 'Click to start',
                        width = 15,
                        height = 5,
                        fg = "pink",
                        bg = "white",
                        command=MyHouse)
startBtn.bind("<Button-1>",MyHouse)
startBtn.pack()


window.mainloop()



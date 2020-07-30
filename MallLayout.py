# to do: make size of the mall map dependent on NameMall.Mall() characteristics
#add stores
from Stores import *
import tkinter as tk
window =tk.Tk()

frm=tk.Frame(master=window, relief = tk.RIDGE, borderwidth=5)
frm.pack(side=tk.TOP)
greeting = tk.Label(master =frm, text="Bootleg Mall Game",
           fg = "pink",
           bg = "white" )
greeting.pack()

def OpenMall():
    window2=tk.Tk()
    window2.rowconfigure([0,1,2],minsize=50,weight=1)
    window2.columnconfigure([0,1,2],minsize=50,weight=1)
    centerMain=tk.Label(master=window2,text='You are in the mall. Leave?',fg="pink",bg="white")
    btn_store=[]

    for store in TSt:
        btn_store.append(tk.Button(master=window2, text = store.getStoreName(),width= 15,height= 5,fg="pink",bg="white"))
    
    j=0
    for c in range(3):
        for r in range(3):
            if c ==1 and r == 1:
                centerMain.grid(row=r, column=c)
            else:
                btn_store[j].grid(row=r,column=c,sticky="nsew")
                j+=1
        # if i =! 4:
        #     btn_store[i].grid(row = 0, column= i , text= btn_store[i].getStoreName())
        # else:
        #     btn_store[i].grid(row = 1)
  
    
    window2.mainloop()



startBtnFrm=tk.Frame(master= window, relief=tk.RAISED,borderwidth=5)
startBtnFrm.pack()
startBtn = tk.Button(master = startBtnFrm, text = 'Click to start',
                        width = 15,
                        height = 5,
                        fg = "pink",
                        bg = "white",
                        command=OpenMall)
startBtn.bind("<Button-1>",OpenMall)
startBtn.pack()


window.mainloop()



# root2=tk.Tk()

# greeting2 = tk.Label(text="Generic Bootleg Mall Game",
#            fg = "pink",
#            bg = "white" )
# greeting2.pack()

# root2.mainloop()
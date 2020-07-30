# to do: make size of the mall map dependent on NameMall.Mall() characteristics
#add stores

import tkinter as tk
root =tk.Tk()

frame=tk.Frame(master=root,"sunken")
greeting = tk.Label(master =frame, text="Generic Bootleg Mall Game",
           fg = "green",
           bg = "pink" )
greeting.pack(fill = tk.BOTH)
frame.pack(fill=tk.BOTH)

startButton = tk.Button(text = 'Click to start',
                        width = 15,
                        height = 5,
                        fg = "green",
                        bg = "white")
startButton.pack()



root.mainloop()

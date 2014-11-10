from tkinter import Tk, Label

tk = Tk()
#First thing you pass to TK objects is its parent
#Lots of options for TK objects, usually easier to use keyword arguements
w = Label(tk, text = 'Hello, world!')
w.grid() #Geometry/packing manager. very simple method (and recommended by Bobl)
tk.mainloop()

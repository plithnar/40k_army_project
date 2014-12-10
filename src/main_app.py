import army
import squad
import unit
import weapon
import csv
from tkinter import *

class App(Frame):
    def __init(self, parent):
        super.__init__()
#        self.grid()
#        armyMenu = Menubutton(self, text="Armies")
#        armyMenu.grid()
#        armyMenu.menu = Menu(armyMenu)
#        armyMenu.menu.choices = Menu(armyMenu.menu)
        

#        print("init app")
#        #for army in army.Armies:
#        #    print("In loop")
#        for name in army.ValidArmies:
                
#        mainloop()

root = Tk()
root.title('My App')

def textUpdate(s, label=""):
    s.set(label)
if 0:
    root.option_readfile('lecture_options.txt')
menubarFrame = Frame(root, relief=RAISED, borderwidth=2, height = 800, width = 1080)
menubarFrame.grid(row=0, column=0)
armyFram = Frame(root, height = 600, width = 800)
armyFram.grid(row=1, column=1)
s = StringVar()
mess = Label(armyFram, textvariable = s, text="Hey, I'm in here!", command=textUpdate(s))
mess.grid(row=0, column=1)

    

def changeText(b, label):
    if b == True:
        s.set(label)
        print(label)
        textUpdate(s, label)

def new_file():
    print("Open new file")


def open_file():
    print("Open existing file")


def stub_action():
    print("Menu select")


def makeCommandMenubutton():
    menubutton = Menubutton(menubarFrame, text='Button Commands', underline=0)
    menubutton.menu = Menu(menubutton)

    menubutton.menu.add_command(label="Undo")
    menubutton.menu.entryconfig(0, state=DISABLED)

    menubutton.menu.add_command(label='New...', underline=0, command=new_file)
    menubutton.menu.add_command(label='Open...', underline=0, command=open_file)
    menubutton.menu.add_command(label='Wild Font', underline=0,
            font=('Zapfino', 14), command=stub_action)
    menubutton.menu.add('separator')
    menubutton.menu.add_command(label='Quit', underline=0, 
            background='red', activebackground='green', 
            command=menubutton.quit)

    menubutton['menu'] = menubutton.menu
    return menubutton


def makeCascadeMenubutton():
    menubutton = Menubutton(menubarFrame, text='Cascading Menus', underline=0)
    menubutton.menu = Menu(menubutton)
    menubutton.menu.choices = Menu(menubutton.menu)

    # create and populate the "weirdOnes" submenu
    menubutton.menu.choices.weirdOnes = Menu(menubutton.menu.choices)
    menubutton.menu.choices.weirdOnes.add_command(label='Stockbroker')
    menubutton.menu.choices.weirdOnes.add_command(label='Quantity Surveyor')
    menubutton.menu.choices.weirdOnes.add_command(label='Church Warden')
    menubutton.menu.choices.weirdOnes.add_command(label='BRM')    

    menubutton.menu.choices.add_command(label='Wooden Leg')
    menubutton.menu.choices.add_command(label='Hire Purchase')
    menubutton.menu.choices.add_command(label='Dead Crab')
    menubutton.menu.choices.add_command(label='Tree Surgeon')
    menubutton.menu.choices.add_command(label='Filing Cabinet')
    menubutton.menu.choices.add_command(label='Goldfish')
    # note the "add_cascade()" rather than the "add_command()"
    menubutton.menu.choices.add_cascade(label='Is it a...', 
            menu=menubutton.menu.choices.weirdOnes)

    menubutton.menu.add_cascade(label='Scripts',
                                   menu=menubutton.menu.choices)
    menubutton['menu'] = menubutton.menu
    return menubutton


def makeCheckbuttonMenubutton():
    menubutton = Menubutton(menubarFrame, text='Checkbutton Menus', underline=0)
    menubutton.menu = Menu(menubutton)

    menubutton.menu.add_checkbutton(label='Doug')
    menubutton.menu.add_checkbutton(label='Dinsdale')
    menubutton.menu.add_checkbutton(label="Stig O'Tracy")
    menubutton.menu.add_checkbutton(label='Vince')
    menubutton.menu.add_checkbutton(label='Gloria Pules')    
    menubutton.menu.invoke(menubutton.menu.index('Dinsdale'))

    menubutton['menu'] = menubutton.menu
    return menubutton

def makeRadiobuttonMenubutton():
    b = BooleanVar()
    b.set(False)
    menubutton = Menubutton(menubarFrame, text='Armies', underline=0)
    menubutton.menu = Menu(menubutton)
    for validArmy in army.validArmies:
        menubutton.menu.add_radiobutton(label=validArmy, variable=b, value=validArmy, command=changeText(b, validArmy))
        
    menubutton['menu'] = menubutton.menu
    return menubutton


def makeDisabledMenubutton(): 
    menubutton = Menubutton(menubarFrame, text='Disabled Menu', underline=0)
    menubutton["state"] = DISABLED
    return menubutton





commandMenubutton = makeCommandMenubutton()
commandMenubutton.grid(row=0, column=0)
cascadeMenubutton = makeCascadeMenubutton()
cascadeMenubutton.grid(row=0, column=1)
checkbuttonMenubutton = makeCheckbuttonMenubutton()
checkbuttonMenubutton.grid(row=0, column=2)
radiobuttonMenubutton = makeRadiobuttonMenubutton()
radiobuttonMenubutton.grid(row=0, column=3)
disabledMenubutton = makeDisabledMenubutton()
disabledMenubutton.grid(row=0, column=4)



mess = Label(armyFram, textvariable = s, text="Hey, I'm in here too!")
mess.grid(row=2, column=0)

#menubarFrame.tk_menuBar(#commandMenubutton,
                #cascadeMenubutton,
                #checkbuttonMenubutton,
#                radiobuttonMenubutton)#,
                #disabledMenubutton)
root.mainloop()

import army
import squad
import unit
import weapon
import vehicle
import csv
from tkinter import *
import copy

__title_format__="Helvetica 14 bold"
__column_format__="Helvetica 12 bold"
__item_format__="Helvetica 12"

class MyGui:
    def __init__(self):
        self.__mainWindow = Tk()
        self.__mainWindow.title("Warhammer 40k Army Simulator")
        self.__mainWindow.geometry('{}x{}'.format(800, 600))
        self.labelText = 'Enter amount to deposit'
        self.depositLabel = Label(self.__mainWindow, text = self.labelText)
        self.menuBarFrame = Frame(self.__mainWindow, relief=RAISED, borderwidth=2)
        self.menuBarFrame.grid(row=0, column=0)
        self.commandMenubutton = self.makeCommandMenubutton(self.menuBarFrame)
        self.commandMenubutton.grid(row=0, column=0)
        self.armySpin = Spinbox(self.menuBarFrame, values=army.validArmies)
        self.armySpin.grid(row=1, column=0)
        self.armyButton = Button(self.menuBarFrame, text="Create army", command=self.submit).grid(row=1, column=1)
        self.simulateButton = Button(self.menuBarFrame, text="Simulate combat", command=self.simulate).grid(row=1, column=2)
        self.armyFrame = Frame(self.__mainWindow)
        self.armyFrame.grid(row=2, column=0, sticky='w')
        mainloop()

    def submit(self):
        label = self.armySpin.get()
        self.depositLabel['text'] = label
        self._army = army.Army(label)
        for key in squad.Squads:
            if key != "" and squad.Squads[key].army_name == label:
                sq = SquadDisplayBar(self.__mainWindow, self, squad.Squads[key])
                sq.frame.grid()
        for key in vehicle.Vehicles:
            if key != "" and vehicle.Vehicles[key].army_name == label:
                sq = SquadDisplayBar(self.__mainWindow, self, vehicle.Vehicles[key])
                sq.frame.grid()

    def simulate(self):
        sim = SimulateWindow()

    def squadSimulate(self, squad):
        sim = SimulateWindow(attackingSquad=squad)

    def new_file(self):
        print("Open new file")
    
    
    def open_file(self):
        print("Open existing file")


    def stub_action(self):
        print("Menu select")
    
    
    def makeCommandMenubutton(self, menubarFrame):
        menubutton = Menubutton(menubarFrame, text='Button Commands', underline=0)
        menubutton.menu = Menu(menubutton)
    
        menubutton.menu.add_command(label="Undo")
        menubutton.menu.entryconfig(0, state=DISABLED)
    
        menubutton.menu.add_command(label='New...', underline=0, command=self.new_file)
        menubutton.menu.add_command(label='Open...', underline=0, command=self.open_file)
        menubutton.menu.add_command(label='Wild Font', underline=0,
                font=('Zapfino', 14), command=self.stub_action)
        menubutton.menu.add('separator')
        menubutton.menu.add_command(label='Quit', underline=0, 
                background='red', activebackground='green', 
                command=self.__mainWindow.quit)
    
        menubutton['menu'] = menubutton.menu
        return menubutton

    def removeCommand(self, remSquad):
        if(squad.Squads[remSquad.squad_name].squad_type) == "HQ":
            container = self._army.hq
        if(squad.Squads[remSquad.squad_name].squad_type) == "Troop":
            container = self._army.troop        
        index = container.index(remSquad)
        container.pop(index)
        print(container)
        self.updateArmy()

    def updateArmy(self):
        print("updating army")
        self.armyFrame.grid_remove()
        self.armyFrame = Frame(self.__mainWindow)
        self.armyFrame.grid(row=2, column=0, sticky='w')
        self.armyFrame['borderwidth']=2
        r = 0
        Label(self.armyFrame, text="HQ Units", font=__column_format__).grid(row=r)
        r +=1

        for squad in self._army.hq:
            sqF = SquadFrameBar(self.armyFrame, self, squad)
            sqF.frame.grid(row=r)
            r += 1

        Label(self.armyFrame, text="Troop Units", font=__column_format__).grid(row=r)
        r += 1

        for squad in self._army.troop:
            sqF = SquadFrameBar(self.armyFrame, self, squad)
            sqF.frame.grid(row=r)
            r += 1

        Label(self.armyFrame, text="Elite Units", font=__column_format__).grid(row=r)
        r += 1

        for squad in self._army.elite:
            sqF = SquadFrameBar(self.armyFrame, self, squad)
            sqF.frame.grid(row=r)
            r += 1

        Label(self.armyFrame, text="Fast Attack Units", font=__column_format__).grid(row=r)
        r += 1

        for squad in self._army.fast:
            sqF = SquadFrameBar(self.armyFrame, self, squad)
            sqF.frame.grid(row=r)
            r += 1

        Label(self.armyFrame, text="Heavy Support Units", font=__column_format__).grid(row=r)
        r += 1

        for squad in self._army.heavy:
            sqF = SquadFrameBar(self.armyFrame, self, squad)
            sqF.frame.grid(row=r)
            r += 1

class SquadFrameBar:
    def __init__(self, parent, guiClass, squad):
        self.guiClass = guiClass
        self.name = squad.squad_name
        self.cost = squad.point_cost
        self.size = squad.current_size
        self.frame = Frame(parent, borderwidth=2)
        name = Label(self.frame, text = self.name, font=__item_format__)
        cost = Label(self.frame, text = self.cost, font=__item_format__)
        size = Label(self.frame, text = self.size, font=__item_format__)
        simbutton = Button(self.frame, text="Simulate Combat", command=lambda:self.guiClass.squadSimulate(squad))
        rembutton = Button(self.frame, text="Remove Squad", command=lambda:self.guiClass.removeCommand(squad))
        name.grid(row=0, column=0)
        cost.grid(row=0, column=1)
        size.grid(row=0, column=2)
        simbutton.grid(row=0, column=3)
        rembutton.grid(row=0, column=4)

class SquadDisplayBar:
    def __init__(self, parent, guiClass, squad):
        self.guiClass = guiClass
        self.name = squad.squad_name
        self.type = squad.squad_type
        self.cost = squad.point_cost
        self.size = squad.current_size
        self.frame = Frame(parent, borderwidth=2)
        name = Label(self.frame, width=30, justify=LEFT, text = self.name, relief=RAISED, bd=1)
        sq_type = Label(self.frame, width=10, text = self.type, relief=RAISED, bd=1)
        cost = Label(self.frame, width=6, text = self.cost, relief=RAISED, bd=1)
        size = Label(self.frame, width=4, text = self.size, relief=RAISED, bd=1)
        button = Button(self.frame, text="Create Squad", command=self.LoadSquad)
        name.grid(row=0, column=0)
        sq_type.grid(row=0, column=1)
        cost.grid(row=0, column=2)
        size.grid(row=0, column=3)
        button.grid(row=0, column=4)


    def LoadSquad(self):
        squad = SquadWindow(self.guiClass, self.name)

class SimulateWindow:
    def __init__(self, attackingSquad="none"):
        self.__mainWindow = Tk()
        self.__mainWindow.title("Simulation Window")
        squads = []
        for key in squad.DefSquads:
            if key != "":
                squads.append(squad.DefSquads[key].squad_name)
        self.squadChooseFrame = Frame(self.__mainWindow, padx=15, pady=15)
        self.squadChooseFrame.grid(row=0, column=0, sticky="new")
        self.attackingSpin = Spinbox(self.squadChooseFrame, values=squads)
        self.attackingSquad=attackingSquad
        self.fromArmy = False
        if attackingSquad == "none":
            Label(self.squadChooseFrame, text="Attacking Squad").grid(row=0, column=0, sticky="nsw")
            self.attackingSpin.grid(row = 1, column = 0, sticky="nsw")
        else:
            Label(self.squadChooseFrame, text="Attacking Squad from Army").grid(row=0, column=0, sticky="nsw")
            Label(self.squadChooseFrame, text=attackingSquad.squad_name, font=__item_format__).grid(row=1, column=0, sticky="nsw")
            self.fromArmy=True

        Label(self.squadChooseFrame, text="Defending Squad").grid(row=0, column=2, sticky="nse")
        self.defendingSpin = Spinbox(self.squadChooseFrame, values=squads)
        self.defendingSpin.grid(row = 1, column = 2, sticky="nse")

        self.spinBarFrame = Frame(self.__mainWindow, padx=15, pady=15)
        self.spinBarFrame.grid(row=1, column=0, sticky="nwe")
        Label(self.spinBarFrame, text="Choose number of simulations").grid(row=0, column=0, sticky="new")
        simNums=list(range(200, 20001, 100))
        self.simulationSpin = Spinbox(self.spinBarFrame, values=list(range(200, 20001, 100)))
        self.simulationSpin.grid(row=1, column=0, sticky="sew")
        self.runSimButton = Button(self.spinBarFrame, text="Run Simulation", command=self.runSim)
        self.runSimButton.grid(row=0, rowspan=2, column=1, sticky="nsew")
        self.simKillResults = {}
        self.simHitResults = {}
        mainloop()

    def runSim(self):
        self.simKillResults = {}
        self.simHitResults = {}
        if self.fromArmy == False:
            self.attackingSquad = copy.deepcopy(squad.Squads[self.attackingSpin.get()])
        for num in range(eval(self.simulationSpin.get())):
            defSquad = copy.deepcopy(squad.DefSquads[self.defendingSpin.get()])
            result = self.attackingSquad.squadFire(defSquad)
            if result[0] not in self.simHitResults:
                self.simHitResults[result[0]] = 0
            self.simHitResults[result[0]] += 1
            if result[1] not in self.simKillResults:
                self.simKillResults[result[1]] = 0
            self.simKillResults[result[1]] += 1
        self.simResultsFrame = Frame(self.__mainWindow, padx=15, pady=15)
        self.simResultsFrame.grid(row=2,column=0,sticky="nsew")
        self.hitResultsFrame = Frame(self.simResultsFrame, padx=10, pady=15)
        self.hitResultsFrame.grid(row=0, column=0,sticky="nsew")
        self.killResultsFrame = Frame(self.simResultsFrame, padx=10, pady=15)
        self.killResultsFrame.grid(row=0, column=1,sticky="nsew")
        self.maxPosFrame = Frame(self.simResultsFrame, padx=10, pady=15)
        self.maxPosFrame.grid(row=1, sticky="nsew")
        numHitPoss = 0
        numWoundsPoss = 0
        if isinstance(self.attackingSquad, squad.Squad):
            for unit in self.attackingSquad.units:
                numHitPoss += eval(unit.ranged_weapon.attacks)
        else:
            for i in range(self.attackingSquad.current_size):
                for weapon in self.attackingSquad.ranged_weapons:
                    numHitPoss += eval(weapon.attacks)
        for unit in squad.DefSquads[self.defendingSpin.get()].units:
            numWoundsPoss += unit.wounds
        rf = 1
        Label(self.hitResultsFrame, text="{} hits possible".format(min(numWoundsPoss,numHitPoss)), font=__item_format__).grid(row=0)
        for hit in self.simHitResults:
            percent = self.simHitResults[hit]/eval(self.simulationSpin.get())*100
            t = "{} hits: {:6.2f}%".format(hit, percent)
            Label(self.hitResultsFrame, text=t, font=__item_format__).grid(row=rf)
            rf+=1
        Label(self.killResultsFrame, text="{} kills possible".format(defSquad.current_size), font=__item_format__).grid(row=0)
        for kill in self.simKillResults:
            percent = self.simKillResults[kill]/eval(self.simulationSpin.get())*100
            t = "{} kills: {:6.2f}%".format(kill, percent)
            Label(self.killResultsFrame, text=t, font=__item_format__).grid(row=rf)
            rf+=1
        
class SquadWindow:
    def __init__(self, parent, squadName):
        self.parent = parent
        if squadName in squad.Squads:
            self.squad = copy.deepcopy(squad.Squads[squadName])
        else:
            self.squad = copy.deepcopy(vehicle.Vehicles[squadName])
        self.__mainWindow = Tk()
        self.__mainWindow.title("{} to create".format(self.squad.squad_name))
        self.__mainWindow.geometry('{}x{}'.format(1080,800))
        Label(self.__mainWindow, text="Squad information", font=__title_format__).grid(row=0)

        Label(self.__mainWindow, text="Squad Name", font=__column_format__).grid(row=1, column=0)
        Label(self.__mainWindow, text="Squad Type", font=__column_format__).grid(row=1, column=1)
        Label(self.__mainWindow, text="Current Cost", font=__column_format__).grid(row=1, column=2)
        Label(self.__mainWindow, text="Current Size", font=__column_format__).grid(row=1, column=3)
        Label(self.__mainWindow, text="Max Size", font=__column_format__).grid(row=1, column=4)

        Label(self.__mainWindow, text=self.squad.squad_name, font=__item_format__).grid(row=2, column=0)
        Label(self.__mainWindow, text=self.squad.squad_type, font=__item_format__).grid(row=2, column=1)
        self.pointLabel = Label(self.__mainWindow, text=self.squad.point_cost, font=__item_format__)
        self.pointLabel.grid(row=2, column=2)
        self.sizeLabel = Label(self.__mainWindow, text=self.squad.current_size, font=__item_format__)
        self.sizeLabel.grid(row=2, column=3)
        Label(self.__mainWindow, text=self.squad.max_size, font=__item_format__).grid(row=2, column=4)

        #Spacer
        Label(self.__mainWindow,).grid(row=3)

        Label(self.__mainWindow, text="Unit information", font=__title_format__).grid(row=4)
        if isinstance(self.squad, squad.Squad):
            Label(self.__mainWindow, text="Unit Name", font=__column_format__).grid(row=5, column=0)
            Label(self.__mainWindow, text="Weapon Skill", font=__column_format__).grid(row=5, column=1)
            Label(self.__mainWindow, text="Ballistics Skill", font=__column_format__).grid(row=5, column=2)
            Label(self.__mainWindow, text="Str.", font=__column_format__).grid(row=5, column=3)
            Label(self.__mainWindow, text="Tough.", font=__column_format__).grid(row=5, column=4)
            Label(self.__mainWindow, text="Wounds", font=__column_format__).grid(row=5, column=5)
            Label(self.__mainWindow, text="Init.", font=__column_format__).grid(row=5, column=6)
            Label(self.__mainWindow, text="Melee Att.", font=__column_format__).grid(row=5, column=7)
            Label(self.__mainWindow, text="Lead.", font=__column_format__).grid(row=5, column=8)
            Label(self.__mainWindow, text="Armor", font=__column_format__).grid(row=5, column=9)
            Label(self.__mainWindow, text="Invuln", font=__column_format__).grid(row=5, column=10)
        
        else:
            Label(self.__mainWindow, text="Unit Name", font=__column_format__).grid(row=5, column=0)
            Label(self.__mainWindow, text="Ballistics Skill", font=__column_format__).grid(row=5, column=1)
            Label(self.__mainWindow, text="Front Armor", font=__column_format__).grid(row=5, column=2)
            Label(self.__mainWindow, text="Side Armor", font=__column_format__).grid(row=5, column=3)
            Label(self.__mainWindow, text="Rear Armor", font=__column_format__).grid(row=5, column=4)
            Label(self.__mainWindow, text="Hull Points", font=__column_format__).grid(row=5, column=5)
        r=6
        if isinstance(self.squad, squad.Squad):
            for u in self.squad.units:
                Label(self.__mainWindow, text=u.name, font=__item_format__).grid(row=r, column=0)
                Label(self.__mainWindow, text=u.weapon_skill.__str__(), font=__item_format__).grid(row=r, column=1)
                Label(self.__mainWindow, text=u.ballistics_skill.__str__(), font=__item_format__).grid(row=r, column=2)
                Label(self.__mainWindow, text=u.strength.__str__(), font=__item_format__).grid(row=r, column=3)
                Label(self.__mainWindow, text=u.toughness.__str__(), font=__item_format__).grid(row=r, column=4)
                Label(self.__mainWindow, text=u.wounds.__str__(), font=__item_format__).grid(row=r, column=5)
                Label(self.__mainWindow, text=u.initiative, font=__item_format__).grid(row=r, column=6)
                Label(self.__mainWindow, text=u.melee_attacks.__str__(), font=__item_format__).grid(row=r, column=7)
                Label(self.__mainWindow, text=u.leadership.__str__(), font=__item_format__).grid(row=r, column=8)
                Label(self.__mainWindow, text=u.armor_save.__str__(), font=__item_format__).grid(row=r, column=9)
                Label(self.__mainWindow, text=u.invuln_save.__str__(), font=__item_format__).grid(row=r, column=10)
                r += 1

            weps = []
            self.unitToWeap = {}

            for weapon in self.squad.ranged_weapons:
                for i in range(3,len(weapon)):
                    label = "{} - {} {}, {} points".format(weapon[i][0],weapon[2],weapon[0],weapon[i][1]) 
                    weps.append(label)
                    self.unitToWeap[label] = [weapon[i][0], weapon[2], weapon[i][1], weapon[0]]
            # enable "change weapon" button

        
            self.wepSpin = Spinbox(self.__mainWindow, values=weps)
            self.wepSpin.grid(row=r, column=3)
            self.weaponAdd = Button(self.__mainWindow, text="Upgrade Weapon", command=self.UpgradeWeapon)
            self.weaponAdd.grid(row=r, column=4)

            r += 1

        else:
            for i in range(self.squad.current_size):
                Label(self.__mainWindow, text=self.squad.squad_name, font=__item_format__).grid(row=r, column=0)
                Label(self.__mainWindow, text=self.squad.ballistics_skill.__str__(), font=__item_format__).grid(row=r, column=1)
                Label(self.__mainWindow, text=self.squad.front_armor.__str__(), font=__item_format__).grid(row=r, column=2)
                Label(self.__mainWindow, text=self.squad.side_armor.__str__(), font=__item_format__).grid(row=r, column=3)
                Label(self.__mainWindow, text=self.squad.rear_armor.__str__(), font=__item_format__).grid(row=r, column=4)
                Label(self.__mainWindow, text=self.squad.hull_points, font=__item_format__).grid(row=r, column=5)

                r += 1

        self.exportButton = Button(self.__mainWindow, text="Add to Army", command=self.AddSquad)
        self.exportButton.grid(row=r, column=3)
        self.addButton = Button(self.__mainWindow, text="Add Unit to Squad", command=self.AddUnit)
        self.addButton.grid(row=r, column=4)
        self.fillButton = Button(self.__mainWindow, text="Fill Squad with units", command=self.FillSquad)
        self.fillButton.grid(row=r, column=5)
        
        mainloop()

    def AddSquad(self):
        if self.squad.squad_type == "Troop":
            self.parent._army.AddTroop(self.squad)

        if self.squad.squad_type == "HQ":
            self.parent._army.AddHq(self.squad)

        if self.squad.squad_type == "Elite":
            self.parent._army.AddElite(self.squad)

        if self.squad.squad_type == "Heavy Support":
            self.parent._army.AddHeavy(self.squad)

        if self.squad.squad_type == "Fast Attack":
            self.parent._army.AddFast(self.squad)

        self.parent.updateArmy()
            
        self.__mainWindow.destroy()

    def FillSquad(self):
        unitName = ""
        if isinstance(self.squad, squad.Squad):
            unitName = list(self.squad.additional_units.keys())[0]
        while self.squad.current_size < self.squad.max_size:
            self.squad.addUnit(unitName)
        self.addButton
        self.exportButton
        self.pointLabel['text'] = self.squad.point_cost
        self.sizeLabel['text'] = self.squad.current_size
        r=6

        if isinstance(self.squad, squad.Squad):
            for u in self.squad.units:
                Label(self.__mainWindow, text=u.name, font=__item_format__).grid(row=r, column=0)
                Label(self.__mainWindow, text=u.weapon_skill.__str__(), font=__item_format__).grid(row=r, column=1)
                Label(self.__mainWindow, text=u.ballistics_skill.__str__(), font=__item_format__).grid(row=r, column=2)
                Label(self.__mainWindow, text=u.strength.__str__(), font=__item_format__).grid(row=r, column=3)
                Label(self.__mainWindow, text=u.toughness.__str__(), font=__item_format__).grid(row=r, column=4)
                Label(self.__mainWindow, text=u.wounds.__str__(), font=__item_format__).grid(row=r, column=5)
                Label(self.__mainWindow, text=u.initiative, font=__item_format__).grid(row=r, column=6)
                Label(self.__mainWindow, text=u.melee_attacks.__str__(), font=__item_format__).grid(row=r, column=7)
                Label(self.__mainWindow, text=u.leadership.__str__(), font=__item_format__).grid(row=r, column=8)
                Label(self.__mainWindow, text=u.armor_save.__str__(), font=__item_format__).grid(row=r, column=9)
                Label(self.__mainWindow, text=u.invuln_save.__str__(), font=__item_format__).grid(row=r, column=10)
                r += 1

        else:
            for i in range(self.squad.current_size):
                Label(self.__mainWindow, text=self.squad.squad_name, font=__item_format__).grid(row=r, column=0)
                Label(self.__mainWindow, text=self.squad.ballistics_skill.__str__(), font=__item_format__).grid(row=r, column=1)
                Label(self.__mainWindow, text=self.squad.front_armor.__str__(), font=__item_format__).grid(row=r, column=2)
                Label(self.__mainWindow, text=self.squad.side_armor.__str__(), font=__item_format__).grid(row=r, column=3)
                Label(self.__mainWindow, text=self.squad.rear_armor.__str__(), font=__item_format__).grid(row=r, column=4)
                Label(self.__mainWindow, text=self.squad.hull_points, font=__item_format__).grid(row=r, column=5)
                r += 1
        
        self.addButton['state']='normal'
        if self.squad.current_size == self.squad.max_size:
            self.addButton['state']='disabled'
        if isinstance(self.squad, squad.Squad):
            self.wepSpin.grid(row=r, column=3)
            self.weaponAdd.grid(row=r, column=4)
            r += 1
        self.exportButton.grid(row=r, column=3)
        self.addButton.grid(row=r, column=4)
        self.fillButton.grid(row=r, column=5)

    def AddUnit(self):
        unitName = ""
        if isinstance(self.squad, squad.Squad):
            unitName = list(self.squad.additional_units.keys())[0]
        self.squad.addUnit(unitName)
        self.addButton
        self.exportButton
        self.pointLabel['text'] = self.squad.point_cost
        self.sizeLabel['text'] = self.squad.current_size
        r=6
        if isinstance(self.squad, squad.Squad):
            for u in self.squad.units:
                Label(self.__mainWindow, text=u.name, font=__item_format__).grid(row=r, column=0)
                Label(self.__mainWindow, text=u.weapon_skill.__str__(), font=__item_format__).grid(row=r, column=1)
                Label(self.__mainWindow, text=u.ballistics_skill.__str__(), font=__item_format__).grid(row=r, column=2)
                Label(self.__mainWindow, text=u.strength.__str__(), font=__item_format__).grid(row=r, column=3)
                Label(self.__mainWindow, text=u.toughness.__str__(), font=__item_format__).grid(row=r, column=4)
                Label(self.__mainWindow, text=u.wounds.__str__(), font=__item_format__).grid(row=r, column=5)
                Label(self.__mainWindow, text=u.initiative, font=__item_format__).grid(row=r, column=6)
                Label(self.__mainWindow, text=u.melee_attacks.__str__(), font=__item_format__).grid(row=r, column=7)
                Label(self.__mainWindow, text=u.leadership.__str__(), font=__item_format__).grid(row=r, column=8)
                Label(self.__mainWindow, text=u.armor_save.__str__(), font=__item_format__).grid(row=r, column=9)
                Label(self.__mainWindow, text=u.invuln_save.__str__(), font=__item_format__).grid(row=r, column=10)
                r += 1

        else:
            for i in range(self.squad.current_size):
                Label(self.__mainWindow, text=self.squad.squad_name, font=__item_format__).grid(row=r, column=0)
                Label(self.__mainWindow, text=self.squad.ballistics_skill.__str__(), font=__item_format__).grid(row=r, column=1)
                Label(self.__mainWindow, text=self.squad.front_armor.__str__(), font=__item_format__).grid(row=r, column=2)
                Label(self.__mainWindow, text=self.squad.side_armor.__str__(), font=__item_format__).grid(row=r, column=3)
                Label(self.__mainWindow, text=self.squad.rear_armor.__str__(), font=__item_format__).grid(row=r, column=4)
                Label(self.__mainWindow, text=self.squad.hull_points, font=__item_format__).grid(row=r, column=5)
                r += 1
        
        self.addButton['state']='normal'
        if self.squad.current_size == self.squad.max_size:
            self.addButton['state']='disabled'
        if isinstance(self.squad, squad.Squad):
            self.wepSpin.grid(row=r, column=3)
            self.weaponAdd.grid(row=r, column=4)
            r += 1
        self.exportButton.grid(row=r, column=3)
        self.addButton.grid(row=r, column=4)
        self.fillButton.grid(row=r, column=5)

    def UpgradeWeapon(self):
        label = self.wepSpin.get()
        for index in range(min(self.squad.current_size, self.unitToWeap[label][1])):
            upgradedUnit = next(x for x in self.squad.units if x.name == self.unitToWeap[label][3])
            upgradedUnit.armRangedWeapon(weapon.ranged_weapons[self.unitToWeap[label][0]])
            self.squad.point_cost += self.unitToWeap[label][2]        
            self.pointLabel['text'] = self.squad.point_cost

myGUI = MyGui()

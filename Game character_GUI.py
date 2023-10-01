
## ANGEL CYRHEN P. RECAÑA | ACTIVITY 5 | BSIS-2AB


from tkinter import *
from tkinter import messagebox
import tkinter as tk

Library = [ ["WIZARD", "KNIGHT", "ARCHER", "ASSASSIN"],["WIZARD STAFF", "SWORD", "BOW & ARROW", "KATAR"],]

class gc_gui(Frame):  
    def __init__(self):
       
        Frame.__init__(self)
        self.Class = ""  
        self.Weapon= ""
        self.Ability = []
    
        self.master.title("Game Characters")
        self.pack()
        self.configure(bg='burlywood2')

        self.header= Label(self,text = " === CUSTOMIZE YOUR GAME CHARACTER  === ", font = ("Courier New (Courier)", 10,), fg = "saddle brown", background = "burlywood2")
        self.header.pack(pady = 10)

        #Class
        self.class_label= Label(self,text = "SET CLASS", font = ("Helvitica", 10,'bold'), fg = "saddle brown", background = "burlywood2")
        self.class_label.pack(pady = 10)
        self.class_choices = Label(self,text = "[1] WIZARD\n[2] KNIGHT\n [3] ARCHER\n    [4] ASSASSIN", font = ("Helvitica", 10,), fg = "saddle brown", background = "burlywood2")
        self.class_choices.pack(pady = 10)

        self.classVar= IntVar()
        self.classVarEntry = Entry(self, font = ("Helvitica", 10), textvariable = self.classVar, fg= "saddle brown", background = "wheat2" )
        self.classVarEntry.pack(pady = 10)

        self.class_Btn = Button(self, text = " SUBMIT | CLASS ", font = ("Helvitica", 10), command = self.Set_Class, fg= "antique white", background = "saddle brown" ) #Button widget
        self.class_Btn.pack(pady = 10)

        #Weapon

        self.weapon_label= Label(self,text = "SET WEAPON", font = ("Helvitica", 10,'bold'), fg = "saddle brown", background = "burlywood2")
        self.weapon_label.pack(pady = 10)
        self.weapon_choices = Label(self,text ="[1] WIZARD STAFF\n [2] SWORD            \n [3] BOW & ARROW\n [4] KATA                ", font = ("Helvitica", 10,), fg = "saddle brown", background = "burlywood2")
        self.weapon_choices.pack(pady = 10)

        self.weaponVar= IntVar()
        self.weaponEntry = Entry(self, font = ("Helvitica", 10), textvariable = self.weaponVar, fg= "saddle brown", background = "wheat2" )
        self.weaponEntry.pack(pady = 10)

        self.weapon_Btn = Button(self, text = "SUBMIT | WEAPON", font = ("Helvitica", 10), command = self.Set_Weapon, fg= "antique white", background = "saddle brown" ) #Button widget
        self.weapon_Btn.pack(pady = 10)

         #Ability

        self.abilitiesOption_label= Label(self,text = "SET ABILITIES", font = ("Helvitica", 10,'bold'), fg = "saddle brown", background = "burlywood2")
        self.abilitiesOption_label.pack(pady = 10)

       
     
        self.ab1 = StringVar()
        self.ab1.set('SELECT | ABILITY 1')
        self.ab1_dropdown = tk.OptionMenu(self, self.ab1, '', '', '')
        self.ab1_dropdown.pack(pady =5)

        self.ab2 = StringVar()
        self.ab2.set('SELECT | ABILITY 2')
        self.ab2_dropdown = tk.OptionMenu(self, self.ab2, '', '', '',)
        self.ab2_dropdown.pack(pady =5)

        self.ab3 = StringVar()
        self.ab3.set('SELECT | ABILITY 3')
        self.ab3_dropdown = tk.OptionMenu(self, self.ab3, '', '', '')
        self.ab3_dropdown.pack(pady =5)

        self.weapon_Btn = Button(self, text = " VIEW RESULT", font = ("Helvitica", 10), command = self.See_Result, fg= "antique white", background = "saddle brown" ) #Button widget
        self.weapon_Btn.pack(pady = 10)

        # Refresh
        self.classVar.trace('w', self.refresh_selectionAB)

       
    def Set_Class(self): 
         
        ch_class = int(self.classVarEntry.get())
        self.lib_class = Library[0][ch_class - 1]
        self.Class = self.lib_class
        messagebox.showinfo("SELECTED CLASS", f" YOU CHOSE:\n {self.lib_class}") 

    def Set_Weapon(self):
        ch_weapon = int(self.weaponEntry.get())
        lib_weapon = Library[1][ch_weapon - 1]
        self.Weapon = lib_weapon 
        messagebox.showinfo("SELECTED WEAPON", f" YOU CHOSE:\n {lib_weapon}")


    def refresh_selectionAB(self, *args):
    
        Class = self.classVar.get()
        if Class == 1:
            self.ab1.set('SELECT | ABILITY 1')
            self.ab1_dropdown['menu'].delete(0, 'end')
            self.ab1_dropdown['menu'].add_command(label='Energy Ball', command=tk._setit(self.ab1, 'Energy Ball'))
            self.ab1_dropdown['menu'].add_command(label='Dragons Breath', command=tk._setit(self.ab1, 'Dragons Breath'))
            self.ab1_dropdown['menu'].add_command(label='Crown of Flame', command=tk._setit(self.ab1, 'Crown of Flame'))
            self.ab1_dropdown['menu'].add_command(label='Hail Storm', command=tk._setit(self.ab1, 'Hail Storm'))

            self.ab2.set('SELECT | ABILITY 2')
            self.ab2_dropdown['menu'].delete(0, 'end')
            self.ab2_dropdown['menu'].add_command(label='Energy Ball', command=tk._setit(self.ab2, 'Energy Ball'))
            self.ab2_dropdown['menu'].add_command(label='Dragons Breath', command=tk._setit(self.ab2, 'Dragons Breath'))
            self.ab2_dropdown['menu'].add_command(label='Crown of Flame', command=tk._setit(self.ab2, 'Crown of Flame'))
            self.ab2_dropdown['menu'].add_command(label='Hail Storm', command=tk._setit(self.ab2, 'Hail Storm'))

            self.ab3.set('SELECT | ABILITY 3')
            self.ab3_dropdown['menu'].delete(0, 'end')
            self.ab3_dropdown['menu'].add_command(label='Energy Ball', command=tk._setit(self.ab3, 'Energy Ball'))
            self.ab3_dropdown['menu'].add_command(label='Dragons Breath', command=tk._setit(self.ab3, 'Dragons Breath'))
            self.ab3_dropdown['menu'].add_command(label='Crown of Flame', command=tk._setit(self.ab3, 'Crown of Flame'))
            self.ab3_dropdown['menu'].add_command(label='Hail Storm', command=tk._setit(self.ab3, 'Hail Storm'))

        elif Class == 2:
            self.ab1.set('SELECT | ABILITY 1')
            self.ab1_dropdown['menu'].delete(0, 'end')
            self.ab1_dropdown['menu'].add_command(label='Fire Slash', command=tk._setit(self.ab1, 'Fire Slash'))
            self.ab1_dropdown['menu'].add_command(label='Power Slash', command=tk._setit(self.ab1, 'Power Slash'))
            self.ab1_dropdown['menu'].add_command(label='Gigantic Storm', command=tk._setit(self.ab1, 'Gigantic Storm'))
            self.ab1_dropdown['menu'].add_command(label='Chaotic Disaster', command=tk._setit(self.ab1, 'Chaotic Disaster'))

            self.ab2.set('SELECT | ABILITY 2')
            self.ab2_dropdown['menu'].delete(0, 'end')
            self.ab2_dropdown['menu'].add_command(label='Fire Slash', command=tk._setit(self.ab2, 'Fire Slash'))
            self.ab2_dropdown['menu'].add_command(label='Power Slash', command=tk._setit(self.ab2, 'Power Slash'))
            self.ab2_dropdown['menu'].add_command(label='Gigantic Storm', command=tk._setit(self.ab2, 'Gigantic Storm'))
            self.ab2_dropdown['menu'].add_command(label='Chaotic Disaster', command=tk._setit(self.ab2, 'Chaotic Disaster'))

            self.ab3.set('SELECT | ABILITY 3')
            self.ab3_dropdown['menu'].delete(0, 'end')
            self.ab3_dropdown['menu'].add_command(label='Fire Slash', command=tk._setit(self.ab3, 'Fire Slash'))
            self.ab3_dropdown['menu'].add_command(label='Power Slash', command=tk._setit(self.ab3, 'Power Slash'))
            self.ab3_dropdown['menu'].add_command(label='Gigantic Storm', command=tk._setit(self.ab3, 'Gigantic Storm'))
            self.ab3_dropdown['menu'].add_command(label='Chaotic Disaster', command=tk._setit(self.ab3, 'Chaotic Disaster'))
        
        elif Class == 3:
            self.ab1.set('SELECT | ABILITY 1')
            self.ab1_dropdown['menu'].delete(0, 'end')
            self.ab1_dropdown['menu'].add_command(label='Take Aim', command=tk._setit(self.ab1, 'Take Aim'))
            self.ab1_dropdown['menu'].add_command(label='Quick Shot', command=tk._setit(self.ab1, 'Quick Shot'))
            self.ab1_dropdown['menu'].add_command(label='Blazing Arrow', command=tk._setit(self.ab1, 'Blazing Arrow'))
            self.ab1_dropdown['menu'].add_command(label='Frost Arrow', command=tk._setit(self.ab1, 'Frost Arrow'))

            self.ab2.set('SELECT | ABILITY 2')
            self.ab2_dropdown['menu'].delete(0, 'end')
            self.ab2_dropdown['menu'].add_command(label='Take Aim', command=tk._setit(self.ab2, 'Take Aim'))
            self.ab2_dropdown['menu'].add_command(label='Quick Shot', command=tk._setit(self.ab2, 'Quick Shot'))
            self.ab2_dropdown['menu'].add_command(label='Blazing Arrow', command=tk._setit(self.ab2, 'Blazing Arrow'))
            self.ab2_dropdown['menu'].add_command(label='Frost Arrow', command=tk._setit(self.ab2, 'Frost Arrow'))

            self.ab3.set('SELECT | ABILITY 3')
            self.ab3_dropdown['menu'].delete(0, 'end')
            self.ab3_dropdown['menu'].add_command(label='Take Aim', command=tk._setit(self.ab3, 'Take Aim'))
            self.ab3_dropdown['menu'].add_command(label='Quick Shot', command=tk._setit(self.ab3, 'Quick Shot'))
            self.ab3_dropdown['menu'].add_command(label='Blazing Arrow', command=tk._setit(self.ab3, 'Blazing Arrow'))
            self.ab3_dropdown['menu'].add_command(label='Frost Arrow', command=tk._setit(self.ab3, 'Frost Arrow'))

        elif Class == 4:
            self.ab1.set('SELECT | ABILITY 1')
            self.ab1_dropdown['menu'].delete(0, 'end')
            self.ab1_dropdown['menu'].add_command(label='Cloaking', command=tk._setit(self.ab1, 'Cloaking'))
            self.ab1_dropdown['menu'].add_command(label='Enchant Poison', command=tk._setit(self.ab1, 'Enchant Poison'))
            self.ab1_dropdown['menu'].add_command(label='Sonic Acceleration', command=tk._setit(self.ab1, 'Sonic Acceleration'))
            self.ab1_dropdown['menu'].add_command(label='Meteor Assault', command=tk._setit(self.ab1, 'Meteor Assault'))

            self.ab2.set('SELECT | ABILITY 2')
            self.ab2_dropdown['menu'].delete(0, 'end')
            self.ab2_dropdown['menu'].add_command(label='Cloaking', command=tk._setit(self.ab2, 'Cloaking'))
            self.ab2_dropdown['menu'].add_command(label='Enchant Poison', command=tk._setit(self.ab2, 'Enchant Poison'))
            self.ab2_dropdown['menu'].add_command(label='Sonic Acceleration', command=tk._setit(self.ab2, 'Sonic Acceleration'))
            self.ab2_dropdown['menu'].add_command(label='Meteor Assault', command=tk._setit(self.ab2, 'Meteor Assault'))

            self.ab3.set('SELECT | ABILITY 3')
            self.ab3_dropdown['menu'].delete(0, 'end')
            self.ab3_dropdown['menu'].add_command(label='Cloaking', command=tk._setit(self.ab3, 'Cloaking'))
            self.ab3_dropdown['menu'].add_command(label='Enchant Poison', command=tk._setit(self.ab3, 'Enchant Poison'))
            self.ab3_dropdown['menu'].add_command(label='Sonic Acceleration', command=tk._setit(self.ab3, 'Sonic Acceleration'))
            self.ab3_dropdown['menu'].add_command(label='Meteor Assault', command=tk._setit(self.ab3, 'Meteor Assault'))



   
    def See_Result(self):
        messagebox.showinfo("RESULT", f" CUSTOMIZED GAME CHARACTER  \n\n CLASS: {self.Class} \n WEAPON: {self.Weapon}\n\n ABILITY 1: {self.ab1.get()} \n ABILITY 2: {self.ab2.get()} \n ABILITY 3: {self.ab3.get()}")
       
    
def main():

    gc_gui().mainloop()
main()



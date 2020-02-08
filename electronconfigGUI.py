import tkinter
from tkinter import messagebox
import periodictable as pt

class ElectronConfiguration:

    

    # The __init__ method for the object 
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.geometry("600x400")
        
        # Initialising the frames in this program
        self.top_frame = tkinter.Frame()
        self.radio_button_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()
        self.button_frame = tkinter.Frame()

        self.element_prompt = tkinter.Label(self.top_frame, text="Please enter the element you are looking to find the electron configuration of: ")
        self.element_entry = tkinter.Entry(self.top_frame, width=20)
        
        self.element_prompt.pack(side="left")
        self.element_entry.pack(side="left")

        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        self.long_hand_rb = tkinter.Radiobutton(self.radio_button_frame, text="Longhand Configuration", variable = self.radio_var, value=1)
        self.short_hand_rb = tkinter.Radiobutton(self.radio_button_frame, text="Shorthand Configuration", variable = self.radio_var, value=2)

        self.long_hand_rb.pack(side="left")
        self.short_hand_rb.pack(side="left")

        
        self.configuration_message = tkinter.Label(self.bottom_frame, text="Configuration: ")
        self.configuration_value = tkinter.StringVar()
        self.configuration_label = tkinter.Label(self.bottom_frame, textvariable=self.configuration_value)
        
        self.configuration_message.pack(side="left")
        self.configuration_label.pack(side="left")

        self.configuration_button = tkinter.Button(self.button_frame, text="Generate", command=self.configurate)
        self.quit_button = tkinter.Button(self.button_frame, text="Quit", command=self.main_window.quit)
        
        self.configuration_button.pack(side="left")
        self.quit_button.pack(side="left")
        
        self.top_frame.pack()
        self.radio_button_frame.pack()
        self.bottom_frame.pack()
        self.button_frame.pack()
        
        tkinter.mainloop()

    # This method finds the nearest noble gas for a given element. This will be called every time, but the values will only be used if the user wants the shorthand electron configuration
    # of their chosen element
    def nearest_noble(self, atomic_number):
        noble_gases = [2, 10, 18, 36, 54, 86, 118]

        for x in noble_gases:
            if atomic_number - x < 0:
                return noble_gases[noble_gases.index(x) - 1]

            elif atomic_number - x == 0:
                return atomic_number


    def shorten_config(self, configuration1, configuration2, noble_name):
        self.conf1list = configuration1.split(" ")
        self.conf2list = configuration2.split(" ")

        final_config = "[" + noble_name + "]"

        for x in self.conf1list:
            if x not in self.conf2list:
                final_config += " " + x

        return final_config

    
    def configuration(self, atomic_number):
        self.orbitals = {"1s": 2, "2s": 2, "2p": 6, "3s": 2, "3p": 6, "4s": 2, "3d": 10, "4p": 6, "5s": 2, "4d": 10, "5p": 6, "6s": 2, "4f": 14, "5d": 10, "6f": 6, "7s": 2, "5f": 14,
                    "6d": 10, "7p": 6}

        self.total_electrons = 0
        self.energy_level = ""
        self.final_electron = False

        for keys in self.orbitals.keys():
            for potential in range(0, self.orbitals[keys]):
                atomic_number -= 1

                if atomic_number == 0:
                    self.energy_level += " " + keys + "" + str(potential + 1)
                    self.final_electron = True
                    break

            if self.final_electron:
                return self.energy_level
            else:
                self.energy_level += " " + keys + "" + str(self.orbitals[keys])
        
    def display(self, atomic_number, noble_name, noble_number):
        self.configuration_atom = self.configuration(atomic_number)
        self.configuration_noble = self.configuration(noble_number)

        if self.radio_var.get() == 1 or atomic_number <= 2 or atomic_number == noble_number:
            return self.configuration_atom
        else:
            return self.shorten_config(self.configuration_atom, self.configuration_noble, noble_name)

        
    def configurate(self):
        # This is where the methods from the other program will go

        # This will make sure that the element in question exists
        self.exists = False
        # This will keep track of the atomic number of the element in question
        self.atomic_number = 0
        # This will keep track of the nearest 
        self.noble_number = 0
        # This will keep track of the symbol of the nearest noble gas
        self.noble_name = ""

        self.element_name = self.element_entry.get().lower()

        for element in pt.elements:
            if element.name == self.element_name:
                self.exists = True
                self.atomic_number = element.number

        
        if self.exists:
            self.noble_gas = self.nearest_noble(self.atomic_number)

            for el in pt.elements:
                if el.number == self.noble_gas:
                    self.noble_name = el.symbol
                    self.noble_number = el.number


            complete_config = self.display(self.atomic_number, self.noble_name, self.noble_number)

            self.configuration_value.set(complete_config)
            
config = ElectronConfiguration()

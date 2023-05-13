import random
import threading

import mouse
import time
import tkinter
import kivy_venv

# from pyGUI import pyGUI
# gui = pyGUI()

#TODO
# Tkinter GUI
# More anti-ban measures?
# If misclicks, detect and go back to magic spellbook and restart (screen detection/recognition)
# Mouse movement macro, add variation to coordinates

class Autoclicker:
    def __init__(self):
        self._clickMinTime = 0.3
        self._clickMaxTime = 0.6
        self._doubleClickSleep = 0.3

    @property
    def clickMinTime(self):
        return self._clickMinTime

    @clickMinTime.setter
    def clickMinTime(self, value):
        self._clickMinTime = value

    def doubleClick(self):
        mouse.click("left")
        time.sleep(random.uniform(0.05, self._doubleClickSleep))
        mouse.click("left")

        # Random wait 5% of time for 3-8 seconds
        if(random.randint(0,100) <= 5):
            x = random.uniform(3, 8)
            print(f'Waiting {x} seconds')
            time.sleep(x)

        # Random wait 1% of time for 20-45 seconds
        if(random.randint(0,100) <= 1):
            x = random.uniform(20, 45)
            print(f'Waiting {x} seconds')
            time.sleep(x)

        # Random wait 0.1% of time for 70-300 seconds
        if(random.randint(0,1000) <= 1):
            x = random.uniform(70, 300)
            print(f'Waiting {x} seconds')
            time.sleep(x)

    def autoclick(self, minTime, maxTime):
        self.clickMinTime = minTime
        self._clickMaxTime = maxTime

    def start(self):
        while True:
            print(threading.active_count())
            time.sleep(random.uniform(self.clickMinTime, self._clickMaxTime))
            self.doubleClick()

# ac = Autoclicker()
# ac.start()
    # while True:
    #     time.sleep(random.uniform(clickMinTime,self._clickMaxTime))
    #     doubleClick()








# from tkinter import *
# master = Tk()
#
# def change_text():
#     my_var.set("Second click")
#     print('click')
#
# my_var = StringVar()
# my_var.set("First click")
# label = Label(master, textvariable=my_var, fg="red")
# button = Button(master, text="Submit", command=change_text)
# button.pack()
# label.pack()
#
# master.mainloop()

# window = tkinter.Tk(screenName=None, baseName=None, className='Tk', useTk=1)
# window.title('AutoClicker')
# window.geometry(newGeometry='500x500+50+50')
# scale = tkinter.Scale(window, width=25)
# scale.pack()


# buttonValue = tkinter.StringVar()
# buttonValue.set(0.05)
# label = tkinter.Label(window, textvariable=buttonValue)
# def changeButtonValue(value=0):
#     global buttonValue
#     val = buttonValue.get()
#     buttonValue.set(val + value)
#     print(val)
# button1 = tkinter.Button(window, width=2,text='+', command=changeButtonValue)
# button2 = tkinter.Button(window, width=2,text='-', command=changeButtonValue)
# button1.pack()
# button2.pack()
# label.pack()
# window.mainloop()
import kivy
kivy.require('2.1.0')
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix import *
from kivy.uix.button import *
from kivy.uix.textinput import TextInput
from kivy.uix.slider import Slider

import autoclicker

class GUI(App):
    # class LoginScreen(GridLayout):
        # def __init__(self,**kwargs):
        #     super(LoginScreen, self).__init__(**kwargs)
    # self.cols = 2
    def build(self):
        grid = GridLayout(cols=2)


        self.username = TextInput(multiline = False)
        self.button = Button(text='fuckoff')
        grid.add_widget(self.button)

        #Slider
        self.slider = Slider(min=0, max=100, value=25)
        grid.add_widget(self.slider)
        self.label = Label(text='lrewjl')
        self.slider.add_widget(self.label)

        return grid
    # class Myapp(App, AutoClicker):
    #     def build(self):
            # l = Label(text = 'hello')
            # b = Button(text = 'heyyyy')
            # l.add_widget(b)
            # return LoginScreen()

        # checkbox = kivy.uix.checkbox
# Myapp = Myapp()
if __name__ == '__main__':
    GUI().run()
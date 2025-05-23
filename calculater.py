from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

class CalculatorApp(App):

    def build(self):
        layout = BoxLayout(orientation='vertical')
        display = Label(text='0')
        layout.add_widget(display)

        buttons = GridLayout(cols=4)
        for i in range(10):
            button = Button(text=str(i))
            buttons.add_widget(button)

        layout.add_widget(buttons)

        return layout

if __name__ == '__main__':
    CalculatorApp().run()
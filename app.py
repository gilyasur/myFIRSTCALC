from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.graphics import Color


class Calculator(App):
    def build(self):
        markup=True
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

      
        self.message_label = Label(text='[color=FFFFFF]Write numbers and Hit Sum to sum them up! [/color]', markup=True)
        self.text_input1 = TextInput(hint_text='Enter Number 1 ', background_color = "ff3333",hint_text_color=(255, 255, 255) )
        self.text_input2 = TextInput(hint_text="Enter Number 2",  background_color = "blue", hint_text_color=(255, 255, 255))

        button1 = Button(text="Sum!")
        button1.bind(on_press=self.on_button_click_sum)
        button2 = Button(text="Mutiply!")
        button2.bind(on_press=self.on_button_click_multi)
        

        main_layout.add_widget(self.message_label)
        main_layout.add_widget(self.text_input1)
        main_layout.add_widget(self.text_input2) 
        main_layout.add_widget(button1)
        main_layout.add_widget(button2)

        return main_layout


    def on_button_click_sum(self, instance):
        num1 = int(self.text_input1.text)
        num2 = int(self.text_input2.text)
        total_Sum = int(num1+num2)
        self.message_label.text = f'Sum {total_Sum}'
    
    def on_button_click_multi(self, instance):
        num1 = int(self.text_input1.text)
        num2 = int(self.text_input2.text)
        total_multi = int(num1*num2)
        self.message_label.text = f'Sum {total_multi}'


if __name__ == '__main__':
    Calculator().run()

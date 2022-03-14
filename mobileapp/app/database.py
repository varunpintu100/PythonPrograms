import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import pyttsx3


class TextToVoice_Grid(GridLayout):
    def __init__(self,**kwargs):
        super(TextToVoice_Grid, self).__init__() # this is to invoke the constructor it self 
        self.cols = 2 #creates the number of lines required
        self.add_widget(Label(text="Person Name: "))   # this line creates a new widget 
        self.person_name = TextInput(multiline=False)  # multiline is false so that can take only line as input 
        self.add_widget(self.person_name)   
        
        #amount field to capture amount on the given date
        
        self.add_widget(Label(text="Amount : "))
        self.person_amount=TextInput(multiline=False)
        self.add_widget(self.person_amount)
        
        #date on which the amount is given
        
        self.add_widget(Label(text="Enter date : "))
        self.amount_date=TextInput(multiline=False)
        self.add_widget(self.amount_date)
        
        #enter button
        self.Submit=Button(text="Submit")
        self.Submit.bind(on_press=self.Click)
        self.add_widget(self.Submit)
        
    def Click(self,instance):
        self.voicecall(self.person_name.text)
        print("You have entered your details sucessfully")
            
    
    def voicecall(self,text):
        converter = pyttsx3.init()  #initializes text to speech and stores in a object
        converter.setProperty('rate', 150)   # initializes text rate of speech
        converter.setProperty('volume', 1.0)  # controlls the volume of the speech
        converter.say(text) #this is used to spell out the text 
        converter.runAndWait() 

class TextToVoice(App):
    
    def build(self):
        
        return TextToVoice_Grid()
    
if __name__=="__main__":
    TextToVoice().run()
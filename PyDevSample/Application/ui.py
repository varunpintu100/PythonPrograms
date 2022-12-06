from tkinter import *
import pyttsx3
def voicecall(text,id):
    converter = pyttsx3.init()  #initializes text to speech and stores in a object
    converter.setProperty('rate', 150)   # initializes text rate of speech
    converter.setProperty('volume', 1.0)  # controlls the volume of the speech
    voice_id= id
    converter.setProperty('voice', voice_id) #setting the voice can be done or not based on the request
    converter.say(text) #this is used to spell out the text
    converter.runAndWait()
def download_voice(text,id):
    converter = pyttsx3.init()  #initializes text to speech and stores in a object
    converter.setProperty('rate', 150)   # initializes text rate of speech
    converter.setProperty('volume', 1.0)  # controlls the volume of the speech
    voice_id= id
    converter.setProperty('voice', voice_id) #setting the voice can be done or not based on the request
    converter.save_to_file(text, 'speech.mp3') #this is used to spell out the text
    converter.runAndWait()
if __name__=='__main__':
    window = Tk() #intializes the window using the tkinter initialization
    window.title("Voice Application")
    l1=Label(window, text="Text to voice converter",font=("Courier",22))
    l1.grid(column=0,row=0)
    txt=Entry(window,width=40)
    txt.grid(column=1,row=0)
    def clicked():
        id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
        res = txt.get()
        voicecall(res,id)
    bt1=Button(window,text="David_Voice",command=clicked,font=("Courier",10))
    bt1.grid(column=2,row=0)
    def clicked1():
        id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
        res = txt.get()
        voicecall(res,id)
    def clicked2():
        id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
        res = txt.get()
        download_voice(res, id)
    bt2=Button(window,text="Zira_Voice",command=clicked1,font=("Courier",10))
    bt2.grid(column=2,row=1)
    bt=Button(window,text="quit",command=window.destroy,font=("Courier",10))
    bt.grid(column=1,row=1)
    bt3 = Button(window, text="Download", command=clicked2, font=("Courier", 10))
    bt3.grid(column=2,row=2)
window.mainloop()

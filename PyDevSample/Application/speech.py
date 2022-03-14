import pyttsx3
def voice_call(text):
    converter = pyttsx3.init()
    converter.setProperty('rate', 140)
    converter.setProperty('volume', 1.0)
    # voice_id= "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
    # converter.setProperty('voice', voice_id)
    # converter.say(text)
    # converter.say("Hai shivangi")
    # converter.say("How are you doing?")
    # converter.runAndWait() 
    # converter.say("Happy diwali")
    # converter.say("All the best for your cat Exam!")
    converter.runAndWait()
    voices = converter.getProperty('voices')
    for voice in voices:
    # to get the info. about various voices in our PC
        print("Voice:")
        print("ID: %s" %voice.id)
        print("Name: %s" %voice.name)
        print("Age: %s" %voice.age)
        print("Gender: %s" %voice.gender)
        print("Languages Known: %s" %voice.languages)
txt="varun"
voice_call(txt)

from tkinter import *
from main.weatherapi import *
if __name__=='__main__':
    window = Tk() #intializes the window using the tkinter initialization
    window.title("Weather Application")
    window.geometry('900x600')
    window.config(bg='#0f4b6e')
    scrollbar = Scrollbar(window)
    scrollbar.pack(side=RIGHT, fill=Y)
    l1=Label(window, text="Enter the location to find the weather : ",font=("Courier",12),bg='#0f4b6e',fg='white')
    l1.pack()
    txt=Entry(window,width=45)
    txt.pack()
    def clicked():
        res = txt.get()
        api_data=current_City(res)
        if api_data['cod'] == '400':
            disp_text.config(text="Please enter a city name")
            return None
        if api_data['cod'] == "404":
            disp_text.config(text="Invalid City: {}, Please check you City name".format(res))
        else:
            temp_city= ((api_data['main']['temp'])-273.15)
            weather_desc = api_data['weather'][0]['description']
            hmdt = api_data['main']['humidity']
            wind_spd = api_data[ 'wind' ]['speed']
            date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
            disp_text.config(text='---------------------------------------------------------'+'\n'+"Weather Stats for - {}   ||   {}\n".format(res.upper(), date_time)+"--------------------------------------------------------------\n"+"Current temperature is: {0:.2f} deg C\n".format(temp_city)+"Current weather desc: {}\n".format(weather_desc)+"Current Humidity : {}%\n ".format(hmdt)+"Current windspeed : {}kmph\n".format(wind_spd))
    def clear():
        txt.delete(0, 'end')
    bt1=Button(window,text="Get Data",command=clicked,relief=SOLID,font=("Courier",10))
    bt1.config(height=1,width=15)
    bt1.place(x=305,y=55)
    bt2=Button(window,text="Clear",command=clear,font=("Courier",10),relief=SOLID)
    bt2.config(height=1,width=15)
    bt2.place(x=448,y=55)
    bt=Button(window,text="QUIT",command=window.destroy,font=("Courier",10),relief=SOLID)
    bt.place(x=376,y=100)
    bt.config(height=1,width=15)
    disp_text= Label(window,width=50,font=('Courier',10),borderwidth = 3,relief="sunken",bg='black',fg='white')
    disp_text.place(x=140,y=200,width=600,height=300)
    window.mainloop()
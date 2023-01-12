#importing required libraries
from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

#creating main window
root=Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)

# '*event' is a parameter given to this function in order to allow it to accept any number of arguments.
# This is needed to implement the use of the "enter" key upon search and giving back the weather details immediately.
def getWeather(*event): 
    try:
        #get city name from text field
        city=textfield.get()
        
        #get latitude and longitude for the given city
        geolocator=Nominatim(user_agent="geoapiExercises")
        location=geolocator.geocode(city)
        
        #get timezone for the given location
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
        
        #set timezone
        home=pytz.timezone(result)
        
        #get current time in the given timezone
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")
        
        #display current time on the clock label
        clock.config(text=current_time)
        
        #heading text label
        name.config(text="Time in City:")
        
        #api to get weather data for the given city
        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=646824f2b7b86caffec1d0b16ea77f79"
        
        #get json data from the api
        json_data = requests.get(api).json()
        
        #extract required data from the json data
        condition = json_data['weather'][0]['main']
        description=json_data['weather'][0]['description']
        temp=int(json_data['main']['temp']-273.15)
        pressure=json_data['main']['pressure']
        humidity=json_data['main']['humidity']
        wind=json_data['wind']['speed']
        
        #display data on respective labels
        t.config(text=(temp,"°", "C"))
        c.config(text=(condition,"|","Feels","like",temp,"°","Celsius"))
        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)
        
    except Exception as e:
        #display error message if invalid entry
        messagebox.showerror("Weather App","404:Invalid Entry.")

#initializing search image
Search_image=PhotoImage(file="textbox.png")
myimage=Label(image=Search_image)
myimage.place(x=20,y=20)

#initializing text field
textfield=tk.Entry(root,justify="center",width=17, font=("poppins",25,"bold"),bg="#1D3839", border=0,fg="white")
textfield.place(x=50,y=40)
textfield.focus()
textfield.bind("<Return>",getWeather)




#initializing search icon button
Search_icon=PhotoImage(file="searchButton.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#1D3839",command=getWeather)
myimage_icon.place(x=400,y=34)

#initializing logo image
Logo_image=PhotoImage(file="logo.png")
logo=Label(image=Logo_image)
logo.place(x=150,y=100)

#initializing frame image
Frame_image=PhotoImage(file="frame.png")
frame_myimage=Label(image=Frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

#initializing name label
name=Label(root,font=("Helvetica",15,"bold"))
name.place(x=30,y=100)

#initializing clock label
clock=Label(root,font=("Ubuntu Sans Mono",20))
clock.place(x=30,y=130)

#initializing labels for weather data
label1=Label(root,text="WIND",font=("Helvetica",15,'bold'),fg="white",bg="#383372")
label1.place(x=120,y=400)
label2=Label(root,text="HUMIDITY",font=("Helvetica",15,'bold'),fg="white",bg="#383372")
label2.place(x=250,y=400)
label3=Label(root,text="DESCRIPTION",font=("Helvetica",15,'bold'),fg="white",bg="#383372")
label3.place(x=430,y=400)
label4=Label(root,text="PRESSURE",font=("Helvetica",15,'bold'),fg="white",bg="#383372")
label4.place(x=650,y=400)

t=Label(font=("arial",70,"bold"),fg="#F88D2A")
t.place(x=400,y=150)
c=Label(font=("arial",15,'bold'))
c.place(x=400,y=250)

w=Label(text="...",font=("arial",20,"bold"),bg="#383372",fg="#D46FB4")
w.place(x=120,y=430)
h=Label(text="...",font=("arial",20,"bold"),bg="#383372",fg="#D46FB4")
h.place(x=280,y=430)
d=Label(text="...",font=("arial",20,"bold"),bg="#383372",fg="#D46FB4")
d.place(x=450,y=430)
p=Label(text="...",font=("arial",20,"bold"),bg="#383372",fg="#D46FB4")
p.place(x=670,y=430)

#starts the program
root.mainloop()


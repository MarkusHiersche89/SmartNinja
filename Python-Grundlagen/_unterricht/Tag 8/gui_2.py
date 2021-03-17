import tkinter
import json
from urllib.request import urlopen
from PIL import Image, ImageTk      # pip3 install pillow

api_key = "db42a172058b014d7e4feb069ab9a7aa"
city_name = "Vienna"
response = urlopen("https://api.openweathermap.org/data/2.5/weather?q=" + city_name + "&appid=" + api_key).read()
data = json.loads(response)
print(data)

def k_in_c(kelvin):
    return kelvin -273.15

main_window = tkinter.Tk()
main_window.geometry("500x500")
main_window.title("Wetterstation")

willkommenstext = tkinter.Label(main_window, text="Eigene Wetterstation")
willkommenstext.grid(row=0, column=0)

temperatur = tkinter.Label(main_window, text=k_in_c(data.get("main").get("temp")))
temperatur.grid(row=1, column=0)

load = Image.open("images.png")
render = ImageTk.PhotoImage(load)
img = tkinter.Label(image=render)
img.grid(row=1, column=2)

tkinter.mainloop()
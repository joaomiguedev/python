import requests
from tkinter import Tk, Entry, Label, Button, messagebox
import http.client


root = Tk()
root.geometry('300x300')
root.title('weather_api')
root.resizable(False, False)

api_url = "https://api.openweathermap.org/data/2.5/weather"
api_key = "" # your put api_key

api_data = "https://api.api-ninjas.com/v1/city"
api_ninja_key = "" # your put api_key

def get_weather(city):
    global data

    # --- WEATHER API ---
    params = {"q": city, "appid": api_key, "units": "metric"}
    response = requests.get(api_url, params=params)
    data = response.json()

    # --- CITY API ---
    responsetime = requests.get(
        api_data,
        params={"name": city},
        headers={"X-Api-Key": api_ninja_key}
    )

    data_time = responsetime.json()
    print("City API:", data_time)

    try:
        temp = data['main']['temp']
        temp_min = data['main']['temp_min']
        temp_max = data['main']['temp_max']
        weather = data['weather'][0]['main']
        return temp, temp_min, temp_max, weather
    except KeyError:
        messagebox.showerror("Error", "City not found")
        return None


def button_main():
    n1 = get_weather(Entry1.get())
    if n1 is None:
        return

    lb1.configure(text=f"temp: {n1[0]} Cº")
    lb2.configure(text=f"temp_min: {n1[1]} Cº")
    lb3.configure(text=f"temp_max: {n1[2]} Cº")
    lb4.configure(text=f"weather: {n1[3]}")


Entry1 = Entry(root)
Entry1.place(x=50, y=225, width=200)

bt1 = Button(root, text='ok', command=button_main)
bt1.place(x=100, y=250, width=100)

lb1 = Label(root, text='temp: ')
lb1.place(x=135, y=140)

lb2 = Label(root, text='temp_min: ')
lb2.place(x=10, y=170)

lb3 = Label(root, text='temp_max: ')
lb3.place(x=190, y=170)

lb4 = Label(root, text='weather: ')
lb4.place(x=135, y=50)

root.mainloop()

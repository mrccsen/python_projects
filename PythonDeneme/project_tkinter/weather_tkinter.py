from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import requests
from io import BytesIO

url = "https://api.openweathermap.org/data/2.5/weather"
apikey = "d1cd4c615d8aa73bad078698f20693b9"
iconURL = 'https://openweathermap.org/img/wn/{}@2x.png'

def get_weather(city):
    params = {'q': city,
              'appid': apikey,
              'lang': 'tr'
              }
    data = requests.get(url, params=params).json()
    if data:
        city = data['name'].capitalize()
        country = data['sys']['country']
        temp = int(data['main']['temp'] - 273.15)
        icon = data['weather'][0]['icon']
        condition = data['weather'][0]['description'].capitalize()
        return city, country, temp, icon, condition
        

def main():
    try:
        city = konum_giris.get("1.0", "end-1c").strip()
        weather = get_weather(city)
    except:
        messagebox.showwarning("Hata", "Şehir İsmi Geçersiz.")
    if weather:
        konum_goster['text'] = f'{weather[0]}, {weather[1]}'
        sicaklik['text'] = f'{weather[2]}°C'
        condi['text'] = f'Hava {weather[4]}'
        icon_response = requests.get(iconURL.format(weather[3]))
        icon_data = Image.open(BytesIO(icon_response.content))
        icon = ImageTk.PhotoImage(icon_data)
        iconLabel.configure(image=icon)
        iconLabel.image = icon

master = Tk()

canvas = Canvas(master, height=500, width=300)
canvas.pack()

frame_ust = Frame(master, bg="#aaffd4")
frame_ust.place(relx=0.1, rely=0.1, relheight=0.2, relwidth=0.8)

frame_alt = Frame(master, bg="#ffaa56")
frame_alt.place(relx=0.1, rely=0.31, relheight=0.5, relwidth=0.8)

# ÜST ALAN
konum = Label(frame_ust, bg="#aaffd4", text="Lütfen Konum Giriniz", font="Verdana 9 bold")
konum.pack(pady=2)

konum_giris = Text(frame_ust, height=1, width=20)
konum_giris.pack(pady=2)

gonder = Button(frame_ust, height=1, width=10, text="SORGULA", command=main)
gonder.pack(pady=10)

# ALT ALAN
hava_durumu = Label(frame_alt, bg="#ffaa56", text="Hava Durumu", font="Verdana 9 bold")
hava_durumu.pack()

konum_goster = Label(frame_alt, bg="#ffaa56", text="", font="Verdana 9 bold")
konum_goster.pack(pady=3)

iconLabel = Label(frame_alt,bg="#ffaa56")
iconLabel.pack()

sicaklik = Label(frame_alt, bg="#ffaa56", text="", font="Verdana 9 bold")
sicaklik.pack(pady=3)

condi = Label(frame_alt, bg="#ffaa56", text="", font="Verdana 9 bold")
condi.pack(pady=3)

master.mainloop()

from tkinter import *
import random

x = random.randint(0,100)

def tahmin():
    global x
    try:
        value = int(kullanici_tahmini.get())  # Kullanıcının girdiği değeri al ve bir tamsayıya dönüştür
        if value == x:
            text_2['text'] = 'Tebrikler, doğru tahmin ettiniz!'
            text['text'] += f'{value}'
        elif value > x:
            text_2['text'] = f'{value} - Yanlış tahmin ettiniz. Daha küçük bir sayı deneyin.'
            text['text'] += f'{value}'
        else:
            text_2['text'] = f'{value} - Yanlış tahmin ettiniz. Daha büyük bir sayı deneyin.'
            text['text'] += f'{value}'
    except ValueError:
        text_2['text'] = 'Lütfen bir sayı giriniz.'

master = Tk()

canvas = Canvas(master, height=500, width=500)
canvas.pack()

frame_ust = Frame(master, bg='black')
frame_ust.place(relx=0.1, rely=0.1, relheight=0.1, relwidth=0.8)

frame_alt = Frame(master, bg='blue')
frame_alt.place(relx=0.1, rely=0.25, relheight=0.6, relwidth=0.8)

kullanici_tahmini = Entry(frame_ust)
kullanici_tahmini.place(relx=0.1, rely=0.2, relheight=0.5, relwidth=0.5)

button = Button(frame_ust, height=1,width=10, text='Tahmin Et!',command=tahmin)
button.place(relx= 0.7, rely=0.2)

text = Label(frame_alt, text=f'Lütfen Tahmin Ettiğiniz Sayı:')
text.pack(pady=5)

text_2 = Label(frame_alt, text=f'Random Sayı: ')
text_2.pack(pady=100)


master.mainloop()
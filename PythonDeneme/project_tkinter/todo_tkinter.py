from tkinter import *

master = Tk()

canvas = Canvas(master, height=700, width=700)
canvas.pack()

frame = Frame(master, bg='#A4A4A4')
frame.place(relx=0.1, rely=0.1, relheight=0.1, relwidth=0.8)

frame_alt = Frame(master, bg='#00BFFF')
frame_alt.place(relx=0.1, rely=0.22, relheight=0.7, relwidth=0.8)

def ekleme():
    text_content = text.get()
    lines = text_content.split('\n')
    
    for x in lines:
        if x:
            new_frame = Frame(frame_alt, height=2, width=74, bg='#00BFFF')
            new_frame.pack(fill='x', pady=2)

            button_delete = Button(new_frame, bg='red', height=2, width=12, text='X', command=lambda: new_frame.destroy())
            button_delete.pack(side=LEFT, padx=5)

            label = Label(new_frame, bg='#4B088A', height=2, width=50, text=f'{x}', font='veranda 9 bold', fg='orange')
            label.pack(side=LEFT, padx=5, pady=5)

            button_success = Button(new_frame, bg='green', height=2, width=12, text='+', command=lambda: label.config(bg='green'))
            button_success.pack(side=RIGHT, padx=5)

    text.delete(0, END)

# Üst kısım
text = Entry(frame)
text.place(relx=0.05, rely=0.35, relheight=0.3, relwidth=0.7)
text.bind('<Return>', lambda event: None)  # Enter tuşuna basılmasını engelle

btn = Button(frame, height=2, width=10, bg='#6E6E6E', text='EKLE', fg='white', font='veranda 8 bold', command=ekleme)
btn.place(relx=0.8, rely=0.22)

# Alt Kısım
master.mainloop()

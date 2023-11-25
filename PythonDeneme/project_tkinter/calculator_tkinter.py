from tkinter import *

main_window = Tk()

drawing_area = Canvas(main_window, height=500, width=500)
drawing_area.pack()

top_frame = Frame(main_window, bg='blue')
top_frame.place(relx=0.1, rely=0.1, relheight=0.1, relwidth=0.8)

bottom_frame = Frame(main_window)
bottom_frame.place(relx=0.33, rely=0.45, relheight=0.7, relwidth=0.8)

middle_frame = Frame(main_window)
middle_frame.place(relx=0.15, rely=0.22, relheight=0.2, relwidth=0.8)

label = Label(top_frame, height=1, width=50)
label.pack(padx=5, pady=15)

value_1 = []
section = 0
value_2 = []
operation = ''
row_value = 1
column_value = 0
result = ''


def update_label():
    global value_1, value_2, operation
    label['text'] = ' '.join(map(str, value_1)) + ' ' + operation + ' ' + ' '.join(map(str, value_2))


def delete(value):
    global value_1, value_2, operation
    if value == 'C':
        value_1.clear()
        value_2.clear()
        operation = operation[:-1]
    elif value == '«':
        if value_2:
            value_2.pop()
        elif operation:
            operation = operation[:-1]
        elif value_1:
            value_1.pop()
    else:
        if value_1:
            value_1.pop()
    update_label()


def calculate_result(s):
    global result, operation
    if value_1 and value_2 and operation:
        if operation == '+':
            result = str(float(value_1[0]) + float(value_2[0]))
        elif operation == '-':
            result = str(float(value_1[0]) - float(value_2[0]))
        elif operation == '/':
            result = str(float(value_1[0]) / float(value_2[0]))
        elif operation == '*':
            result = str(float(value_1[0]) * float(value_2[0]))
        value_1.clear()
        value_2.clear()
        value_1.append(result)
        label['text'] = f'{result} '


def operations(i):
    global section, operation
    operation = i
    label['text'] += f'{operation} '
    section = 1


def values(d):
    if section == 0:
        value_1.append(d)
        label['text'] += f'{value_1[-1]} '
    elif section == 1:
        value_2.append(d)
        label['text'] += f'{value_2[-1]}'


operations_list = ['+', '-', '*', '/', 'C', '«', ]

for op in operations_list:
    if op != 'C' and op != '«':
        Button(middle_frame, text=op, padx=20, pady=20, border=2.5, font=('Arial', 9), bg='#6E6E6E',
               command=lambda i=op: operations(i)).grid(row=row_value, column=column_value)
        column_value += 1
    else:
        Button(middle_frame, text=op, padx=20, pady=20, border=2.5, font=('Arial', 9), bg='#6E6E6E',
               command=lambda i=op: delete(i)).grid(row=row_value, column=column_value)
        column_value += 1

column_value = 0
row_value += 1

buttons = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3',
    ',', '0', '='
]

for button in buttons:
    if button != ',' and button != '=':
        Button(bottom_frame, text=button, padx=20, pady=20, borderwidth=2.5, font=('Arial', 9), bg='#6E6E6E',
               command=lambda d=button: values(d)).grid(row=row_value, column=column_value)

        column_value += 1
        if column_value > 2:
            column_value = 0
            row_value += 1
    if button == ',':
        Button(bottom_frame, text=button, padx=20, pady=20, borderwidth=4.5, font=('Arial', 9), bg='#6E6E6E',
               command=lambda d=button: values(d)).grid(row=row_value, column=column_value)
        column_value += 1
        if column_value > 2:
            column_value = 0
            row_value += 1
    if button == '=':
        Button(bottom_frame, text=button, padx=20, pady=20, borderwidth=4.5, font=('Arial', 9), bg='#6E6E6E',
               command=lambda s=button: calculate_result(s)).grid(row=row_value, column=column_value)
        column_value += 1
        if column_value > 2:
            column_value = 0
            row_value += 1

main_window.mainloop()

import tkinter
import os
from tkinter import filedialog

def file_select():
    filename = filedialog.askopenfilename(initialdir="/", title = 'Выберите файл', filetypes=(('Текстовый файл', '.txt'),("Все файлы", '*')))
    text['text'] = text['text'] + '' + filename
    os.startfile(filename)

window = tkinter.Tk()
window.title("Проводник")
window.geometry('465x165')
window.configure(bg='gold')
window.resizable(False, False)
text = tkinter.Label(window, text = 'Файл', height = 5, width = 65, bg = 'green')
text.grid(column =1, row =1)
button_select = tkinter.Button(window, text ='Выбрать файл', height = 5, width = 65, bg = 'red', command = file_select)
button_select.grid(column = 1, row = 2)
window.mainloop()
from tkinter import *
import os
import pickledb
from tkinter import messagebox
from tkinter import ttk
from tkinter.messagebox import showerror
import time
from multiprocessing import Process

window = Tk()
window.title("LAN Chat v1.5")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)
window.geometry("800x300")

def close():
    window.destroy()

db = pickledb.load(os.getenv('APPDATA')+'/LAN Chat/user.log', True)
if not db.exists('install'):
    showerror(title="Ошибка", message="Вы не установили LAN Chat! Запустите setup.exe! Выключение через 10 сек.")
    time.sleep(10)
    close()

def send():
    sended_text = send_text.get(1.0, END)

    try:
        name = db.get('username')
    except:
        lock()
        return None
    if name == True or False:
        lock()
        return None
    to_log = name + ': ' + sended_text + '\n'
    f = open(r""+db.get('spath')+"/chat.log", 'a')
    f.write(to_log)
    f.close()
    send_text.delete("1.0","end")

send_text = Text(height=3)
send_button = Button(text='Отправить', command=send)
close_button = Button(text='Закрыть', command=close)

def lock():
    send_button['text'] = 'Установите приложение'
    send_button['state'] = DISABLED

send_text.pack(pady=20)
send_button.pack()
close_button.pack(pady=20)

window.mainloop()

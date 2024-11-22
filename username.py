from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os
import pickledb

db = pickledb.load(os.getenv('APPDATA')+'/LAN Chat/user.log', True)

def enable(children):
   for child in children:
      child.configure(state='enable')

def disable(children):
   for child in children:
      child.configure(state='disable')

def white_fr_func():
    white_fr['state'] = DISABLED
    black_fr['state'] = NORMAL
    db.rem('color_fr')
    db.set('color_fr', 7)

def black_fr_func():
    white_fr['state'] = NORMAL
    black_fr['state'] = DISABLED
    db.rem('color_fr')
    db.set('color_fr', 0)

def white_bg_func():
    white_bg['state'] = DISABLED
    black_bg['state'] = NORMAL
    red_bg['state'] = NORMAL
    green_bg['state'] = NORMAL
    blue_bg['state'] = NORMAL
    db.rem('color_bg')
    db.set('color_bg', 7)

def black_bg_func():
    white_bg['state'] = NORMAL
    black_bg['state'] = DISABLED
    red_bg['state'] = NORMAL
    green_bg['state'] = NORMAL
    blue_bg['state'] = NORMAL
    db.rem('color_bg')
    db.set('color_bg', 0)

def red_bg_func():
    white_bg['state'] = NORMAL
    black_bg['state'] = NORMAL
    red_bg['state'] = DISABLED
    green_bg['state'] = NORMAL
    blue_bg['state'] = NORMAL
    db.rem('color_bg')
    db.set('color_bg', 4)

def grn_bg_func():
    white_bg['state'] = NORMAL
    black_bg['state'] = NORMAL
    red_bg['state'] = NORMAL
    green_bg['state'] = DISABLED
    blue_bg['state'] = NORMAL
    db.rem('color_bg')
    db.set('color_bg', 2)

def blue_bg_func():
    white_bg['state'] = NORMAL
    black_bg['state'] = NORMAL
    red_bg['state'] = NORMAL
    green_bg['state'] = NORMAL
    blue_bg['state'] = DISABLED
    db.rem('color_bg')
    db.set('color_bg', 1)


window = Tk()
window.title("LAN Chat Setup")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)
window.geometry("250x300")
motebook = ttk.Notebook()
motebook.pack(expand=True, fill=BOTH)
setup = ttk.Frame(motebook)
colots = ttk.Frame(motebook)
setup.pack(fill=BOTH, expand=True)
colots.pack(fill=BOTH, expand=True)
motebook.add(setup, text="Установка и имя")
motebook.add(colots, text="Персонализация")
username = Text(setup,height=1, width=16)
spath = Text(setup,height=1, width=16)

def send():
    sended_text = username.get(1.0, END)
    sended_path = spath.get(1.0, END)
    if db.exists('spath'):
        db.rem('spath')
    if db.exists('username'):
        db.rem('username')
    db.set('spath', sended_path.rstrip('\n'))
    db.set('username', sended_text.rstrip('\n'))
    username.delete("1.0","end")
    spath.delete("1.0","end")

def install():
    os.chdir(os.getenv('APPDATA'))
    try:
        os.mkdir('LAN Chat')
    except:
        install_b['text'] = 'Установленно'
        install_b['state'] = DISABLED
    db.set('install', True)
    db.set('color_bg', 9)
    db.set('color_fr', 9)
    white_bg_func()
    black_fr_func()

send_button = Button(setup,text='Отправить', command=send)
header_fr = Label(colots, text='Цвет текста')
header_user = Label(setup, text='Имя')
header_path = Label(setup, text='Путь к серверу')
black_fr = Button(colots, text="Чёрный", command=black_fr_func)
white_fr = Button(colots, text='Белый', background="black",foreground="white", command=white_fr_func)
header_bg = Label(colots, text='Цвет фона')
white_bg = Button(colots, text='Белый', background="black",foreground="white", command=white_bg_func)
black_bg = Button(colots, text="Чёрный", command=black_bg_func)
red_bg = Button(colots, text="Красный",foreground="red",command=red_bg_func)
green_bg = Button(colots, text="Зелёный",foreground="green",command=grn_bg_func)
blue_bg = Button(colots, text="Синий",foreground="blue",command=blue_bg_func)
install_b = Button(setup,text='Установить LAN Chat', command=install)

if db.exists('install'):
    install_b['text'] = 'Установленно'
    install_b['state'] = DISABLED
    send_button['state'] = NORMAL
    lambda: enable(colots.winfo_children())
else:
    install_b['state'] = NORMAL
    send_button['state'] = DISABLED
    lambda: disable(colots.winfo_children())


header_user.pack(pady=10)
username.pack(pady=10)
header_path.pack()
spath.pack(pady=10)
send_button.pack(pady=10)
install_b.pack(pady=20)
header_fr.pack()
black_fr.pack(pady=20)
white_fr.pack()
header_bg.pack(pady=20)
white_bg.pack()
black_bg.pack(pady=20)
red_bg.pack()
green_bg.pack(pady=20)
blue_bg.pack()

window.mainloop()

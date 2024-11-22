from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
import shutil
import os
import pickledb

selection = ''

db = pickledb.load(os.getenv('APPDATA')+'/LAN Chat/user.log', True)

window = Tk()
window.title("LAN File Exchanger")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)
window.geometry("250x450")

newWindow = Toplevel(window)
newWindow.title("Комментарий к файлу")
newWindow.geometry("200x200")
comment = Label(newWindow)

download_files = os.listdir(r""+db.get('spath')+"/Files/")
files_var = Variable(value=download_files)


file_path = Text(height=1, width=16)
def open_file():
    filepath = filedialog.askopenfilename()
    if filepath != "":
        file_path.delete("1.0", END)
        file_path.insert("1.0", filepath)

file_button = Button(text='Обзор', command=open_file)

comm_label = Label(text='Комментарий:')
comm_text = Text(height=3, width=16)

def lock():
    send_button['text'] = 'Установите приложение'
    send_button['state'] = DISABLED

def send():
    path = file_path.get(1.0, END)
    path = path.strip()
    if path == '':
        send_button['text'] = 'Неизвестный файл'
        download_files = os.listdir(r""+db.get('spath')+"/Files/")
        files_var.set(download_files)
        return None
    try:
        shutil.copyfile(path, r""+db.get('spath')+"/Files/" + os.path.basename(path))
    except:
        send_button['text'] = 'Неизвестный файл'
        file_path.delete("1.0", END)
        download_files = os.listdir(r""+db.get('spath')+"/Files/")
        files_var.set(download_files)
        return None
    try:
        name = db.get('username')
    except:
        lock()
        download_files = os.listdir(r""+db.get('spath')+"/Files/")
        files_var.set(download_files)
        return None
    file_path.delete("1.0", END)
    send_button['text'] = 'Отправить'
    tempTuple = os.path.splitext(os.path.basename(path))
    jk = tempTuple[0]
    f = open(r""+db.get('spath')+"/Files Comments/" + jk + '.txt','w')
    f.write(comm_text.get(1.0, END))
    f.close
    f = open(r""+db.get('spath')+"/chat.log", 'a')
    m = f'{name} выложил файл:\n{os.path.basename(path)}\nКомментарий: \n{comm_text.get(1.0, END)}\n'
    f.write(m)
    f.close()
    download_files = os.listdir(r""+db.get('spath')+"/Files/")
    files_var.set(download_files)
    comm_text.delete("1.0", END)

def select(event):
    download_files = os.listdir(r""+db.get('spath')+"/Files/")
    files_var.set(download_files)
    file_sel = files_listbox.curselection()
    file_o = r""+db.get('spath')+"/Files/" + download_files[file_sel[0]]
    file_comm1 = r""+db.get('spath')+"/Files/" + download_files[file_sel[0]]
    tempTuple = os.path.splitext(os.path.basename(file_comm1))
    jk1 = tempTuple[0]
    file_comm = r""+db.get('spath')+"/Files Comments/" + jk1 + '.txt'
    f = open(file_comm, 'r')
    comment['text'] = f.read()
    f.close()
    selection = file_o

def install():
    download_files = os.listdir(r""+db.get('spath')+"/Files/")
    files_var.set(download_files)
    file_sel = files_listbox.curselection()
    file_o = r""+db.get('spath')+"/Files/" + download_files[file_sel[0]]
    if file_o == '':
        download_files = os.listdir(r""+db.get('spath')+"/Files/")
        files_var.set(download_files)
        return None
    shutil.copy(file_o, os.path.expanduser( '~' )+'\\Downloads\\' + os.path.basename(file_o))


files_listbox = Listbox(listvariable=files_var, selectmode=SINGLE)
install_button = Button(text='Установить', command=install)

send_button = Button(text='Отправить', command=send)
file_button.pack(pady=20)
file_path.pack()
comm_label.pack(pady=20)
comm_text.pack()
send_button.pack(pady=20)
ttk.Separator(orient=HORIZONTAL,style='TSeparator',class_= ttk.Separator,takefocus= 1,cursor='plus').pack(fill=X, padx=10, expand=True)
files_listbox.pack(side=LEFT, fill=BOTH, pady=20)
files_listbox.bind("<<ListboxSelect>>", select)
scrollbar = ttk.Scrollbar(orient="vertical", command=files_listbox.yview)
scrollbar.pack(side=RIGHT, fill=Y)
files_listbox["yscrollcommand"]=scrollbar.set
comment.pack(padx=10, side=LEFT, anchor=NW)
install_button.pack(pady=20)

while True:
    download_files = os.listdir(r""+db.get('spath')+"/Files")
    files_var.set(download_files) 
    window.update()

window.mainloop()
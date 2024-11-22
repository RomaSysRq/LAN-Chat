import os
import pickledb
import time

db = pickledb.load(os.getenv('APPDATA')+'/LAN Chat/user.log', True)
os.system(f'color {db.get("color_bg")}{db.get("color_fr")}')
while True:
    f = open(r""+db.get('spath')+"/chat.log", 'r')
    messages = f.read()
    f.close()
    os.system('cls')
    print(messages)
    time.sleep(0.5)
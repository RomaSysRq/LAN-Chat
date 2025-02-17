import os
import pickledb
import time
import base64

db = pickledb.load(os.getenv('APPDATA')+'/LAN Chat/user.log', True)
os.system(f'color {db.get("color_bg")}{db.get("color_fr")}')
while True:
    f = open(r""+db.get('spath')+"/Новый текстовый документ.txt", 'r')
    for line in f:    
        base64_string = line
        base64_bytes = base64_string.encode("utf-8")

        sample_string_bytes = base64.b64decode(base64_bytes)
        sample_string = sample_string_bytes.decode("utf-8")
        print(sample_string)
    f.close()
    time.sleep(0.5)
    os.system('cls')
time.sleep(1)

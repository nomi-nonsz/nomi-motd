import time
import sys
import os


def success():
  print("\033[0m[ \033[0;32mOK \033[0m] Mounted \033[0;37mKernel Debug File System")
  time.sleep(.05)
  print("\033[0m[ \033[0;32mOK \033[0m] Mounted \033[0;37mKernel Trace File System")
  time.sleep(.05)
  print("\033[0m[ \033[0;32mOK \033[0m] Finished \033[0;37mLoad Wired Module")
  time.sleep(.05)
  print("\033[0m[ \033[0;32mOK \033[0m] Finished \033[0;37mLoad Wired Connection Module")
  time.sleep(.05)
  print("\033[0m[ \033[0;32mOK \033[0m] Finished \033[0;37mSet Console Scheme")
  time.sleep(.05)
  print("\033[0m[ \033[0;32mOK \033[0m] Finished \033[0;37mRemount Root and Kernel File System")
  time.sleep(.2)
  print("\033[0m[ \033[0;32mOK \033[0m] Finished \033[0;37mLoad/Save Random Seed")
  time.sleep(.2)
  print("\033[0m[ \033[0;32mOK \033[0m] Finished \033[0;37mCreate User File System")
  time.sleep(.05)
  print("\033[0m[ \033[0;32mOK \033[0m] Finished \033[0;37mApply Kernel Variables")
  time.sleep(.05)
  print("\033[0m[ \033[0;32mOK \033[0m] Finished \033[0;37mApply Kernel Variables")
  time.sleep(.05)
  print("\033[0m[ \033[0;32mOK \033[0m] Unmounted \033[0;37mMount Unit for core18, revision 2811")
  time.sleep(.01)
  print("\033[0m[ \033[0;32mOK \033[0m] Unmounted \033[0;37mMount Unit for core18, revision 2137")
  time.sleep(.01)
  print("\033[0m[ \033[0;32mOK \033[0m] Unmounted \033[0;37mMount Unit for core18, revision 2912")
  time.sleep(.01)
  print("\033[0m[ \033[0;32mOK \033[0m] Unmounted \033[0;37mMount Unit for core18, revision 4209")
  time.sleep(.01)
  print("\033[0m[ \033[0;32mOK \033[0m] Unmounted \033[0;37mMount Unit for core20, revision 321")
  time.sleep(.01)
  print("\033[0m[ \033[0;32mOK \033[0m] Unmounted \033[0;37mMount Unit for core22, revision 323")
  time.sleep(.01)
  print("\033[0m[ \033[0;32mOK \033[0m] Unmounted \033[0;37mMount Unit for core22, revision 534")
  time.sleep(.01)
  print("\033[0m[ \033[0;32mOK \033[0m] Unmounted \033[0;37mMount Unit for core23, revision 234")
  time.sleep(.01)
  print("\033[0m[ \033[0;32mOK \033[0m] Unmounted \033[0;37mMount Unit for wired, revision 546")
  time.sleep(.01)
  print("\033[0m[ \033[0;32mOK \033[0m] Unmounted \033[0;37mMount Unit for wired, revision 765")
  time.sleep(.01)
  print("\033[0m[ \033[0;32mOK \033[0m] Unmounted \033[0;37mMount Unit for wired-socket-unit, revision 154")
  time.sleep(.01)
  print("\033[0m[ \033[0;32mOK \033[0m] Unmounted \033[0;37mMount Unit for wired-socket-unit, revision 211")
  time.sleep(.01)
  print("\033[0m[ \033[0;32mOK \033[0m] Unmounted \033[0;37mMount Unit for wired-connect, revision 485")
  time.sleep(.01)
  print("\033[0m[ \033[0;32mOK \033[0m] Unmounted \033[0;37mMount Unit for navi-core-util, revision 1643")
  time.sleep(.01)
  print("\033[0m[ \033[0;32mOK \033[0m] Unmounted \033[0;37mMount Unit for navi-core-util, revision 1242")
  time.sleep(.01)
  print("\033[0m[ \033[0;32mOK \033[0m] Unmounted \033[0;37mMount Unit for navi-core-util, revision 1864")
  time.sleep(.01)
  print("\033[0m[ \033[0;32mOK \033[0m] Unmounted \033[0;37mMount Unit for navi, revision 4220")
  time.sleep(.01)

print("\033[0m", end="")

print("Starting NaviOs terminal ...")
time.sleep(.2)
print("Integrating bash ...")
time.sleep(.15)
print("Profile ... ", end="")
time.sleep(.3)
print("autoconfigure.cf")
time.sleep(.1)
print("Running /opt/wired/connect.sh ...")
time.sleep(.2)
print("Connecting to 210.322.330.1 ...")
time.sleep(.6)
print("Connected!")

success()

os.system("clear")

print("Running motd ...")
time.sleep(.2)

motd = """Welcome!      
\033[0;36m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⣤⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣤⣾⣿⠀⣠⣾⣿⡿⠛⠛⠛⠛⠿⣿⣷⣤⠀⣿⣷⣤⡀⠀⠀⠀⠀
⠀⠀⢀⣴⣿⠿⠋⠀⣾⣿⠟⠁⠀⠀⠀⠀⠀⠀⠈⠻⣿⣷⠀⠙⠻⣿⣦⡀⠀⠀
⠀⣰⣿⡟⠁⠀⠀⣸⣿⡏⠀⠀⢠⣾⣿⣿⣷⣄⠀⠀⢹⣿⣧⠀⠀⠈⢻⣿⣦⠀
⠐⣿⣿⡀⠀⠀⠀⣿⣿⡇⠀⠀⢻⣿⣿⣿⣿⡿⠀⠀⢸⣿⣿⠀⠀⠀⢀⣿⣿⠇
⠀⠙⢿⣷⣄⡀⠀⠸⣿⣷⡀⠀⠈⠛⠿⠿⠛⠁⠀⢀⣾⣿⠇⠀⠀⣠⣾⡿⠋⠀
⠀⠀⢀⡙⢿⣿⣦⣄⠹⣿⣿⣦⡀⠀⠀⠀⠀⢀⣤⣾⣿⠏⣠⣴⣿⡿⢋⡀⠀⠀
⠀⠀⠿⠟⠀⠈⠛⠛⠀⠈⠛⠿⣿⣷⠀⠀⣾⣿⠿⠛⠁⠀⠛⠛⠁⠀⠻⠿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⣄⠀⠀⠀⠀⣽⣿⠀⠀⣿⣿⠀⠀⠀⠀⣠⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠙⢿⣷⣦⣤⣴⣿⠟⠀⠀⠻⣿⣦⣤⣴⣾⡿⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠁⠀⠀⠀⠀⠈⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀

NaviOs 1.0.5-savari\033[0m
Copyright 1991 (c) Copland OS Enterprise
Produced by Tachibana Lab
"""

for p in motd:
  print(p, end='')
  sys.stdout.flush()
  time.sleep(0.0005)

print("")

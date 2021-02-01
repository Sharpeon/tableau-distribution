import pyautogui as pya
import time

print("GOOOOOOOO")
time.sleep(2)

for line in open("valeurs.txt", "r"):
    pya.typewrite(line)


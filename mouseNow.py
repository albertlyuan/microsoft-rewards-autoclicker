"""
Created on 1/3/2021

@author: Albert
Needs 'Emulate terminal in output console' in Run Configuration
"""
import pyautogui
import keyboard
print('Press c to quit.')
while True:
    try:
        if keyboard.is_pressed('c'):
            break
        x,y = pyautogui.position()
        pos_str = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(pos_str, end='')
        print('\b' * len(pos_str), end='', flush=True)
    except KeyboardInterrupt:
        break
#print(pyautogui.size())
    #Size(width=1920, height=1080)

#pyautogui.moveTo(100, 100, duration=0.25)
#pyautogui.moveRel(100, 100, duration=0.25)

#left=135, top=210 + 300 + 30
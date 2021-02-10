"""
Created on 1/3/2021

@author: Albert
"""
import pyautogui
import time

pyautogui.FAILSAFE = True

#start edge
pyautogui.press('winleft')
time.sleep(1)
pyautogui.typewrite('edge')
pyautogui.press('enter')

confirmation = input('hit y to continue: ')
if confirmation == 'y':
    pass
else:
    quit()
try:
    windows_edge = pyautogui.locateOnScreen('orangeedge.png', confidence=0.9)
    pyautogui.click(windows_edge[0] + 10, windows_edge[1] + 10)
except TypeError:
    pyautogui.click(323, 92)

chars='abcdefghijklmnopqrstuvwxyz1234567890'
num = 0

pyautogui.click(323, 92)
pyautogui.typewrite(chars[num])
pyautogui.press('enter')

for i in range(len(chars)):
    time.sleep(1)
    pyautogui.click(323, 92)
    num += 1
    pyautogui.typewrite(chars[num])
    pyautogui.press('enter')
quit()




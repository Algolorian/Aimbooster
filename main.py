import pyautogui
import keyboard
import time

# Write a script for every vertical column to be scanned in aim booster 50 pixels apart and
# 52.5 pixels rounded for spacing
# top left of aim booster 660, 369
# bottom right of aim booster 1260, 790
# window dimensions 600W and 420H

'''
for i in range(int(600 / 50) - 1):
    i_num = (665 + (50 * i))
    for j in range(int(420 / 52.5) - 1):
        j_num = (375 + (52.5 * j))
        pyautogui.hotkey('win', 'r')
        pyautogui.write('notepad')
        pyautogui.press('enter')
        pyautogui.write('import pyautogui')
        pyautogui.write('import keyboard')
        pyautogui.press('enter', presses=2)

        if pyautogui.pixel(i_num, j_num)[0] == 1:
            pyautogui.click(i_num, j_num)
        if keyboard.is_pressed('q'):
            exit(00)
'''


time.sleep(5)

print('starting')
step = 120

while True:
    for i in range(1147, 2650, step):
        for j in range(861, 1920, step):
            print(i, j)
            # print(pyautogui.pixel(i, j))
            if pyautogui.pixel(i, j)[0] >= 252:
                pyautogui.click(i, j)
            if keyboard.is_pressed('q'):
                exit(0)

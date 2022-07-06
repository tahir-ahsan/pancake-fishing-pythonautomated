import pyautogui as pat
from time import sleep
import pyperclip as pc
import time 

def pancakes():
    sleep(5)
    position = pat.locateOnScreen('C:/Users/tahir/Desktop/Codes/Python Discord Pancake Farming Bot/python-discord plus ss.png', confidence=.999)
    pat.moveTo(position[0:2], duration=.5)
    pat.moveRel(55,-55, duration=.5)
    pat.click()
    pat.doubleClick(button='left')
    pat.click(button='right')
    pat.locateOnScreen('C:/Users/tahir/Desktop/Codes/Python Discord Pancake Farming Bot/python-discord copy ss.png', confidence=.999)
    pat.moveRel(80,-300, duration=.5)
    pat.click()
    text_identify = pc.paste()
    '''with open('C:/Users/tahir/Desktop/Codes/Python Discord Pancake Farming Bot/fish_data.txt', 'a', encoding='utf8') as fish_data:
        fish_data.write(text_identify)''' # To be worked on further
    i = text_identify.split()
    for j in i:
        if (j == 'Buy') or (j == 'broke!'):
            while True:
                wd_script = """p!wd 50"""
                pat.write(wd_script)
                pat.press('enter')
                sleep(2)
                buy_script = """p!buy rod"""
                pat.write(buy_script)
                pat.press('enter')
                sleep(2)
                position = pat.locateOnScreen('C:/Users/tahir/Desktop/Codes/Python Discord Pancake Farming Bot/python-discord buy prompt ss.png', confidence=.999)
                pat.moveTo(position[0:2], duration=.5)
                pat.click()
                script = """p!fish"""
                pat.write(script)
                pat.press('enter')
                sleep(60)
                break
    else:
            while True:
                script = """p!fish"""
                pat.write(script)
                pat.press('enter')
                sleep(60)
                break


timeout = 60*2   # [seconds]

timeout_start = time.time()

while time.time() < timeout_start + timeout:
    test = 0
    if test == 5:
        break
    pancakes()
    test -= 1
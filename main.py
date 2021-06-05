import pyautogui
from time import *
print(pyautogui.size())
print(pyautogui.position())
pyautogui.moveTo(38,762)
pyautogui.click()
sleep(1)
pyautogui.write("Google chrome")
pyautogui.press("enter")
sleep(1)
pyautogui.write("insagram.com")
pyautogui.press("enter")

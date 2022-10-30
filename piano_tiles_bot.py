import pyautogui
#"""
import time
import keyboard
import win32api, win32con
#using win32api bcs its much faster
def click(x,y):
    win32api.SetCursorPos((x,y))    #moving mouse to x y position
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)   #pressing and holding down left click
    time.sleep(0.01)                                            #holding down left click for 0.01 sec
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)     #releasing the left click

pyautogui.PAUSE = 0                     #faster clicks command

while not keyboard.is_pressed("q"):     #ak sa stlaci tato klavesa tak to prerusi program
    
    if pyautogui.pixel(950, 500)[0] == 0:   #ignore #if the cursor is on the 950 and 500 postion(x y) and the color there is black then click there
        click(950, 500)
    if pyautogui.pixel(1030, 500)[0] == 0:
        click(1030, 500)
    if pyautogui.pixel(1120, 500)[0] == 0:
        click(1120, 500)
    if pyautogui.pixel(1200, 500)[0] == 0:
        click(1200, 500)
"""
pyautogui.displayMousePosition()    #this command let you sho your mouse position


# 950  500 RGB: (0, 0, 0)
# 1030 500 RGB: (0, 0, 0)
# 1120 500 RGB: (0, 0, 0)
# 1200 500 RGB: (0, 0, 0)
#"""

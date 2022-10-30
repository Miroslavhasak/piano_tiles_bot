import pyautogui
#"""
import time
import keyboard
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

pyautogui.PAUSE = 0

while not keyboard.is_pressed("q"):
    
    if pyautogui.pixel(950, 500)[0] == 0:
        click(950, 500)
    if pyautogui.pixel(1030, 500)[0] == 0:
        click(1030, 500)
    if pyautogui.pixel(1120, 500)[0] == 0:
        click(1120, 500)
    if pyautogui.pixel(1200, 500)[0] == 0:
        click(1200, 500)
"""
pyautogui.displayMousePosition()


# 950  500 RGB: (0, 0, 0)
# 1030 500 RGB: (0, 0, 0)
# 1120 500 RGB: (0, 0, 0)
# 1200 500 RGB: (0, 0, 0)
#"""
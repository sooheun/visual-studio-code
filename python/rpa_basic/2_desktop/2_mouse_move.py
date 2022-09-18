import pyautogui

# pyautogui.moveTo(100, 100, duration=1)

# pyautogui.move(100, 100, duration=1)
# pyautogui.move(100, 100, duration=1)
# pyautogui.move(100, 100, duration=1)

print(pyautogui.position())

p = pyautogui.position()
print(p[0], p[1])
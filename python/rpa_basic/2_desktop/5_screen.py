import pyautogui

# img = pyautogui.screenshot()
# img.save("screenshot.png")

# pyautogui.mouseInfo()
# 996,204 0,122,204 #007ACC

pixel = pyautogui.pixel(996,204)
print(pixel)

print(pyautogui.pixelMatchesColor(996, 204, (0,122,204)))
print(pyautogui.pixelMatchesColor(996, 204, pixel))
print(pyautogui.pixelMatchesColor(996, 204, (0,122,205)))
import pyautogui
w = pyautogui.getWindowsWithTitle("제목 없음")[0]
w.activate()

# pyautogui.write("12345")
# pyautogui.write("lee soo heun", interval=0.025)

# pyautogui.write(["t", "e", "s", "t", "left", "left", "right", "l", "a", "enter"], interval = 0.25)

# 특수 문자
# shift 4-> $
# pyautogui.keyDown("shift") #쉬프트 누른 상태
# pyautogui.press("4") # 4를 누름
# pyautogui.keyUp("shift") #쉬프트를 뗀다.

# #조합 키
# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("a")
# pyautogui.keyUp("a")
# pyautogui.keyUp("ctrl")

# pyautogui.hotkey("ctrl", "alt", "shift", "a")

# pyautogui.hotkey("ctrl", "a")

import pyperclip
# pyperclip.copy("나도코딩")
# pyautogui.hotkey("ctrl", "v")

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")

my_write("이수흔")


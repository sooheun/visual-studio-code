import pyautogui
import sys
import pyperclip

pyautogui.keyDown("win")
pyautogui.keyDown("r")
pyautogui.keyUp("win")
pyautogui.keyUp("r")

pyautogui.write("mspaint")
pyautogui.keyDown("Enter")
pyautogui.keyUp("Enter")

pyautogui.sleep(2)

window = pyautogui.getWindowsWithTitle("제목 없음 - 그림판")[0]
if window.isMaximized == False:
    window.maximize()

text_icon = pyautogui.locateOnScreen("text_icon.png")

if text_icon:
    pyautogui.click(text_icon, duration=0.5)
else:
    print("찾기 실패")
    sys.exit()

pyautogui.click(200, 200, duration=0.5)

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")

my_write("참 잘했어요")

pyautogui.sleep(5)

window.close()
pyautogui.sleep(1)
pyautogui.press("n")
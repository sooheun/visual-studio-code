import pyautogui

# fw = pyautogui.getActiveWindow()

# print(fw.title) #창의 제목 정보
# print(fw.size) # 창의 크기 정보
# print(fw.left, fw.top, fw.right, fw.bottom)
# pyautogui.click(fw.left + 25, fw.top + 20)

# for w in pyautogui.getAllWindows():
#     print(w)

w = pyautogui.getWindowsWithTitle("설정")[0]
print(w)

if w.isActive == False:
    w.activate()

if w.isMaximized == False:
    w.maximze()

if w.isMinimized == False:
    w.minimize

w.restore()
w.close()
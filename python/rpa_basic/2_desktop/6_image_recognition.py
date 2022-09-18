import pyautogui
# file_menu = pyautogui.locateOnScreen("file_menu.png")
# print(file_menu)

# pyautogui.click(file_menu)

# plus_icon = pyautogui.locateOnScreen("plus_icon.png")
# pyautogui.moveTo(plus_icon)

# screen = pyautogui.locateOnScreen("screenshot.png")
# print(screen)


# for i in pyautogui.locateAllOnScreen("checkbox.png"):
#     print(i)
#     pyautogui.click(i, duration=0.5)

# checkbox = pyautogui.locateOnScreen("checkbox.png")
# pyautogui.click(checkbox)

# 속도 개선
# grayscale

# plus_icon = pyautogui.locateOnScreen("plus_icon.png", grayscale=True)
# pyautogui.moveTo(plus_icon)

# 범위 지정

# plus_icon = pyautogui.locateOnScreen("plus_icon.png", region=(1778, 728, 1887-1778, 829-728))
# pyautogui.moveTo(plus_icon)

# 정확도 조정
# run_btn = pyautogui.locateOnScreen("run_btn.png", confidence=0.9)
# pyautogui.moveTo(run_btn)

# 자동화 대상이 바로 보여지지 않는 경우
# 1. 계속 기다리기
# file_txt = pyautogui.locateOnScreen("file_txt.png")
# if file_txt:
#     pyautogui.click(file_txt)
# else:
#     print("발견 실패")

# while file_txt is None:
#     file_txt = pyautogui.locateOnScreen("file_txt.png")
#     print("발견 실패")
# pyautogui.click(file_txt)

# 2.일정 시간 기다리기 (TimeOut)

import time
import sys

timeout = 10
# start = time.time()
# file_txt = None

# while file_txt is None:
#     file_txt = pyautogui.locateOnScreen("file_txt.png")
#     end = time.time()
#     if end - start > timeout:
#         print("시간 종료")
#         sys.exit()

# pyautogui.click(file_txt)

def find_target(img_file, timeout = 30):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout:
            break
    return target

def my_click(img_file, timeout = 30):
    target = find_target(img_file, timeout)
    
    if target:
        pyautogui.click(target)
    else:
        print(f"[Timeout {timeout}s] Target not found ({img_file}). Terminate program.")
        sys.exit()

my_click("file_txt.png", 1)





















# pyautogui.mouseInfo()

# 1778,728
# 1887,829
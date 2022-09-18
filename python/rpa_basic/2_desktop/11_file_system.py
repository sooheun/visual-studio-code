import os
import time
import datetime

# print(os.getcwd()) # 현재 작업 공간
# os.chdir("rpa_basic")
# print(os.getcwd())
# os.chdir("..") # 상위 폴더
# print(os.getcwd())
# os.chdir("../..") # 상위 폴더 X 2
# print(os.getcwd())
# os.chdir("c:/") # 주어진 경로로 이동
# print(os.getcwd())

# 파일 경로 만들기
# file_path = os.path.join(os.getcwd(), "my_file.txt") # 절대 경로 생성
# print(os.path.join(os.getcwd(), "my_file.txt"))

# 파일 경로에서 폴더 정보 가져오기
# print(os.path.dirname(r"D:\비주얼 스튜디오 코드\my_file.txt"))

# 파일 정보 가져오기

# 파일의 생성 날짜
# file_path = "rpa_basic/2_desktop/11_file_system.py"
# ctime = os.path.getctime(file_path)
# print(ctime)
# # 날짜 정보를 strftime 을 통해서 연월일 시분초 형태로 출력
# print(datetime.datetime.fromtimestamp(ctime).strftime("%Y %m %d %H:%M:%S"))

# # 파일의 수정 날짜
# mtime = os.path.getmtime(file_path)
# print(mtime)
# print(datetime.datetime.fromtimestamp(mtime).strftime("%Y %m %d %H:%M:%S"))

# # 파일의 마지막 접근 날짜
# atime = os.path.getatime(file_path)
# print(atime)
# print(datetime.datetime.fromtimestamp(atime).strftime("%Y %m %d %H:%M:%S"))

# # 파일 크기
# size = os.path.getsize(file_path)
# print(size)

# 파일 목록 가져오기
# print(os.listdir()) # 모든 폴더, 파일 목록 가져오기
# print(os.listdir("rpa_basic"))

# 파일 목록 가져오기 (하위 폴더 모두 포함)
# result = os.walk("rpa_basic") # 주어진 폴더 밑에 있는 모든 폴더, 파일 목록 가져오기
# # print(result)

# for root, dirs, files in result:
#     print(root, dirs, files)

# 만약 폴더 내에서 특정 파일들을 찾으려면?
# name = "11_file_system.py"
# result = []

# for root, dirs, files in os.walk("."):
#     # [a.txt, b.txt, c.txt, 11_file_system.py,...]
#     if name in files:
#         result.append(os.path.join(root, name))
# print(result)

# 만약 폴더 내에서 특정 패턴을 가진 파일들을 찾으려면?
# import fnmatch
# pattern = "*.png"
# result = []
# for root, dirs, files in os.walk("."):
#     for name in files:
#         if fnmatch.fnmatch(name, pattern):
#             result.append(os.path.join(root, name))

# print(result)

# 주어진 경로가 파일인지? 폴더인지?
# print(os.path.isdir("rpa_basic"))
# print(os.path.isfile("rpa_basic"))

# print(os.path.isdir("run_btn.png"))
# print(os.path.isfile("run_btn.png"))

# 만약에 지정된 경로에 해당하는 파일 / 폴더가 없다면?
# print(os.path.isdir("run_btbbbn.png")) # False

# 주어진 경로가 존재하는가?
# if os.path.exists("rpa_basic"):
#     print("파일 또는 폴더가 존재합니다.")
# else:
#     print("없음")

# 파일 만들기
# open("new_file.txt","a").close() #빈 파일 생성

# 파일명 변경
# os.rename("new_file.txt","new_file_rename.txt")

# 파일 삭제
# os.remove("new_file_rename.txt")

# 폴더 만들기 (이미 존재하면 실행 안됨)
# os.mkdir("new_folder") #현재 경로
# os.mkdir("C:/users/....") # 절대 경로

# os.makedirs("new_folders/a/b/c")

# 폴더명 바꾸기
# os.rename("new_folder", "new_folder_rename")

# 폴더 지우기
# os.rmdir("new_folder_rename")

import shutil
# shutil.rmtree("new_folders") # 폴더 안이 비어 있지 않아도 완전 삭제 가능
# 모든 파일이 삭제될 수 있음

# 파일 복사하기
# 어떤 파일을 폴더 안으로 복사
# shutil.copy("run_btn.png","test_folder")
# 어떤 파일을 다른이름으로 복사
# shutil.copy("run_btn.png","test_folder/copied_run_btn.png")
# shutil.copyfile("run_btn.png", "test_folder/copied_run_btn_2.png")

# shutil.copy2("run_btn.png", "test_folder/copy2.png") # 파일의 날짜 등의 정보까지 복사됨

# 폴더 복사
# shutil.copytree("test_folder", "test_folder2")
# shutil.copytree("test_folder", "test_folder3")

# 폴더 이동
# shutil.move("test_folder", "test_folder3")
# shutil.move("test_folder2", "test_folder3")
# shutil.move("test_folder3", "test_folder")


























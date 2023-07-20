# 모듈은 이름을 알아야 사용가능

# math라는 수학모듈 그냥 사용하는 방법
# 1. __import__("math")
# 2. import math
# 2. 방법을 사용할 것을 추천(아니 무조건 2.로 할 것) 

# math라는 수학모듈을 "수학"이라는 변수에 넣어서 사용
# 1. 수학 = __import__("math")
# 2. import math as 수학
# 두 개는 완전히 같은 코드. 역시 2.번을 사용할 것.

# import math as 수학

# print(수학.pi) 
# print(수학.sin(10))

# 모듈에서 일부 기능만을 가져올 때 

# from math import pi, sin

# print(pi)
# print(sin(10))

# 모듈의 모든 기능을 가져와서 쓰고 싶을 때
# 단, 여러개를 불러와서 쓰다가 기능의 이름이 중복될 경우 오류가 발생하므로 주의해서 사용할 필요가 있음.

# from math import *
# print(pi)
# print(sin(10))

# 표준모듈

# import sys

# print(sys.argv)

# import datetime

# now = datetime.datetime.now()
# print("지금은 {}년 {}월 {}일 {}시 {}분 {}초 입니다.".format(now.year, now.month, now.day, now.hour, now.minute, now.second))
# 대부분의 다른 프로그래밍언어는 month를 0~11로 표기하지만 파이썬은 1~12로 표기

# import time
# print("A")
# time.sleep(2) # 2초 간의 딜레이를 주는 함수
# print("B")

# from urllib import request

# target = request.urlopen("https://www.naver.com") # 네이버 페이지의 코드를 가져온다.

# content = target.read()

# print(content)

# 모듈은 외우고 이해하는게 아니라 필요한 기능을 갖고 있는 것을 그 때마다 찾아서 사용하는 것.
# 기본적인 사용법과 어떤 코드들이 존재하는지는 숙지할 필요는 있음.

# 243P 재귀함수 확인 문제 복습
# def flatten(data):
#     f = []
#     for a in data:
#         if type(a) == list:
#             f += flatten(a)
#         else:
#             f.append(a)             
#     return f

# example = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
# print("원본 :", example)
# print("변환 :", flatten(example))

# 330P os모듈 예제

# import os

# 현재 폴더의 파일과 폴더를 추출하여 리스트화
# output = os.listdir(".")
# print("os.listdir() :", output)
# print()

# 추출한 리스트를 for문으로 돌려서 폴더인 경우와 아닌 경우로 나눠서 구분
# print("# 폴더와 파일 구분하기")
# for path in output:
#     if os.path.isdir(path):
#         print("폴더 :", path)
#     else:
#         print("파일 :", path)

# 330P 3번 # 모듈과 재귀함수를 활용하는 문제

# 모듈을 읽습니다.
# import os

# # 폴더를 읽어 들이는 함수
# def read_folder(path):
#     # 폴더의 요소 읽어 들이기
#       output = os.listdir(path)
#     # 폴더의 요소 구분하기
#     for item in output:
#         if os.path.isdir(path + "/" + item): 
#         # 폴더라면 계속 읽어 들이기
#             read_folder(path + "/" + item)
#         else:
#         # 파일이라면 출력하기
#             print("파일 :", item)

# # 현재 폴더의 파일/폴더를 출력합니다.
# read_folder(".")

# 외부 모듈의 설치 방법

# pip install 모듈이름
# pip install 모듈이름 == 1.2.3 # 특정 버전을 다운로드 하고 싶을 때

# 모듈에는 라이브러리와 프레임워크가 존재

# 라이이브러리(Library) : 정상적인 제어가 일어나는 모듈
# math 모듈처럼 모듈에 정의되어 있는 함수를 가져와서 사용하는 모듈

# 프레임워크(Framework) : 제어 역전이 발생하는 모듈
# flask 모듈처럼 사용자가 함수를 정의하면 그 함수를 가져가서 모듈이 사용하는 모듈

# 1. 컴퓨터는 데이터를 저장할 때 무조건 숫자로 저장한다.

# 2. 파이썬의 파일 구분
#  가. 텍스트 데이터 : 텍스터 에디터로 읽을 수 있는 모든 데이터(*.txt *.py 등등)
#  나. 바이너리 데이터 : 텍스터 에디터를 제외한 모든 데이터(*.jpg *.png *.avi font.*)
 
# 3. 텍스트 데이터 읽고 쓰는 방법

# 4. 바이너리 데이터 읽고 쓰는 방법

# 함수 데코레이터 : 어떤 함수에 "미리 만든 규격화된 처리"를 적용하도록 만들 때 사용하는 것

# 기본 함수 데코레이터

# def 데코레이터(함수):
#     print("미리 어떤 처리를 합니다.")
#     return 함수

# @테코레이터 #144라인의 테스트 = 데코레이터(테스트)와 동일한 코드
# def 테스트():
#     print("안녕하세요")

# 테스트 = 데코레이터(테스트)

# 테스트()

# 2겹의 함수 데코레이터

# def 외부테코레이터(number):
#     def 데코레이터(함수):
#         print("미리 어떤 처리를 합니다.", number)
#         return 함수
#     return 데코레이터

# @외부테코레이터(number=100)
# def 테스트():
#     print("안녕하세요")

# 테스트()

# 상속 : 어떤 클래스의 일부 기능을 물려받아 사용하는 것

# 클래스는 최상위 부모 클래스를 무조건 상속

# 자식 : 상속을 받을 클래스 / 부모 : 상속을 해줄 클래스 일 때,
# 상속을 받는 방법 : class 자식(부모):

# 최대값 최소값 구하기

# l = [244, 1, 52, 273, 32, 99, 101]

# max = 1

# min = 1

# for i in l :
#     if i <= min:
#         min = i
#     elif max > i > min:
#         pass
#     else:
#         max = i

# print(max)
# print(min)

# 선생님 답안 

# l = [244, 1, 52, 273, 32, 99, 101]

# max = l[0]

# min = l[0]

# for i in l :
#     if i < min:
#         min = i
#     if i > max:
#         max = i

# print(max)
# print(min)

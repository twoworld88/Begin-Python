# 단항 연산자(not)
# not True # = False
# not False # = True

# 이항 연산자(and, or)
# True and False # 그리고
# True or False  # 또는

# True and True=True
# True and False=False
# False and True=False
# False and False=False

# True or True=True
# True or False=True
# False or True=True
# False or False=Flase

# # 입력을 받습니다.
# number=input("정수 입력>")
# number=int(number)

# # 양수 조건
# if number>0:
#     print("양수입니다.")

# # 음수 조건
# if number<0:
#     print("음수입니다.")

# # 0 조건
# if number==0:
#     print("0입니다.")

# # 날짜/시간과 관련된 기능을 가져옵니다.
# import datetime

# # 현재 날짜/시간을 구합니다.
# now=datetime.datetime.now()

# if now.hour<12:
#     print("현재 시간은 {}시 {}분로 오전입니다!".format(now.hour, now.minute))
# if now.hour>=12:
    # print("현재 시간은 {}시 {}분로 오후입니다!".format(now.hour, now.minute))

# 출력합니다.
# print(now.year, "년")
# print(now.month, "월")
# print(now.day, "일")
# print(now.hour, "시")
# print(now.minute, "분")
# print(now.second, "초")

# # 봄 구분
# if 3 <= now.month<=5:
#     print("이번 달은 {}월로 봄입니다!".format(now.month))

# # 여름 구분
# if 6 <= now.month<=8:
#     print("이번 달은 {}월로 여름입니다!".format(now.month))

# # 가을 구분
# if 9 <= now.month<=11:
#     print("이번 달은 {}월로 가을입니다!".format(now.month))

# # 겨울 구분
# if 12 <= now.month<=2:
#     print("이번 달은 {}월로 겨울입니다!".format(now.month))

# # 입력을 받습니다.
# number=input("정수 입력>")

# # 마지막 자리 숫자를 추출
# last_character=number[-1]

# # 숫자로 변환하기
# last_number=int(last_character)

# # 짝수 확인
# if last_number==0\
#     or last_number==2\
#     or last_number==4\
#     or last_number==6\
#     or last_number==8:
#     print("짝수입니다.")
# # 홀수 확인
# if last_number==1\
#     or last_number==3\
#     or last_number==5\
#     or last_number==7\
#     or last_number==9:
#     print("홀수입니다.")

# # 숫자 변환없이 "in" 활용
# if last_character in "02468":
#     print("짝수입니다.")
# if last_character in "13579":
#     print("홀수입니다.")

# 정수를 이용한 빠른 로직
# number=input("정수를 입력해주세요:")

# number=int(number)

# if number%2 == 0 :
#     print("짝수입니다.")
# if number%2 == 1 :
#     print("홀수입니다.")

# # 정수를 이용한 빠른 로직
# number=input("정수를 입력해주세요:")

# number=int(number)

# if number%2 == 0 :
#     print("짝수입니다.")
# else:
#     print("홀수입니다.") 

# score=float(input("학점 입력:"))

# if score==4.5:
#     print("God")
# elif 4.2<=score<4.5:
#     print("교수님의 사랑")
# elif 3.5<=score<4.2:
#     print("현 체제의 수호자")
# elif 2.8<=score<3.5:
#     print("일반인")
# elif 2.3<=score<2.8:
#     print("일탈을 꿈꾸는 소시민")
# elif 1.75<=score<2.3:
#     print("오락문화의 선구자")
# elif 1.0<=score<1.75:
#     print("불가촉천민")
# elif 0.5<=score<1.0:
#     print("자벌레")
# elif 0<score<0.5:
#     print("플랑크톤")
# elif score==0:
#     print("시대를 앞서가는 혁명의 씨앗")

# score=float(input("학점 입력:"))

# if score==4.5:
#     print("God")
# elif 4.2<=score:
#     print("교수님의 사랑")
# elif 3.5<=score:
#     print("현 체제의 수호자")
# elif 2.8<=score:
#     print("일반인")
# elif 2.3<=score:
#     print("일탈을 꿈꾸는 소시민")
# elif 1.75<=score:
#     print("오락문화의 선구자")
# elif 1.0<=score:
#     print("불가촉천민")
# elif 0.5<=score:
#     print("자벌레")
# elif 0<score:
#     print("플랑크톤")
# else:
#     print("시대를 앞서가는 혁명의 씨앗")

# print("# if 조건문에 0 넣기")
# if 0:
#     print("0은 True로 변환됩니다.")
# else:
#     print("0은 False로 변환됩니다.")
# print()

# print("# if 조건문에 빈 문자열 넣기")
# if "":
#     print("빈 문자열은 True로 변환됩니다.")
# else:
#     print("빈 문자열은 False로 변환됩니다.")

# print("# 미구현 구간은 pass키워드로 스킵")
# if "":
#     pass
# else:
#     pass

# str_input=input("태어난 해를 입력하시오:")
# birth_year=int(str_input)

# if birth_year%12==0:
#     print("원숭이 띠입니다.")
# elif birth_year%12==1:
#     print("닭 띠입니다.")
# elif birth_year%12==2:
#     print("개 띠입니다.")
# elif birth_year%12==3:
#     print("돼지 띠입니다.")
# elif birth_year%12==4:
#     print("쥐 띠입니다.")
# elif birth_year%12==5:
#     print("소 띠입니다.")
# elif birth_year%12==6:
#     print("범 띠입니다.")
# elif birth_year%12==7:
#     print("토끼 띠입니다.")
# elif birth_year%12==8:
#     print("용 띠입니다.")
# elif birth_year%12==9:
#     print("뱀 띠입니다.")
# elif birth_year%12==10:
#     print("말 띠입니다.")
# elif birth_year%12==11:
#     print("양 띠입니다.")


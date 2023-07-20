# list_a=[1,2,3]
# list_b=[4,5,6]

# print("#리스트")
# print("list_a=", list_b)
# print("list_b=", list_a)
# print()

# print("#리스트 기본 연산자")
# print("list_a+list_b", list_a+list_b)
# print("list_a*3=", list_a*3)
# print()

# print("# 길이 구하기")
# print("len(list_a)=", len(list_a))

# list_a=[1,2,3]

# print("# 리스트 뒤에 요소 추가하기")
# list_a.append(4)
# list_a.append(5)
# print(list_a)
# print()

# print("# 리스트 중간에 요소 추가하기")
# list_a.insert(0, 10)
# print(list_a)

# list_a=[0,1,2,3,4,5]
# print("# 리스트의 요소 하나 제거하기")

# del list_a[1]
# print("del list_a[1]:", list_a)

# list_a.pop(2)
# print("pop(2):", list_a)
 
# array=[1,2,3,4,5,6]

# for element in array:
#     print(element)

# 157~159P 확인문제

#2번
# numbers=[273, 103, 5, 32, 65, 9, 72, 800, 99]

# for number in numbers:
#     if number >= 100:
#         print("-100 이상의 수:", number)

#3번

# for a in numbers:
#     if a%2==1:
#         print("{}는 홀수입니다." .format(a))
#     else:
#         print("{}는 짝수입니다.".format(a))
# print()

# for a in numbers:
#     if 0<=a<10:
#         print("{}는 1자릿수입니다.".format(a))
#     elif 10<=a<100:
#         print("{}는 2자릿수입니다.".format(a))
#     else:
#         print("{}는 3자릿수입니다.".format(a))

# for a in numbers:
#     print("{}는 {} 자릿수입니다.".format(a, len(str(a))))

# holzzak = ["짝수", "홀수"]
# for a in numbers:
#     print("{}는 {}입니다.".format(a, holzzak[a%2]))

# 4번

# lol=[[1, 2, 3], [4, 5, 6, 7], [8, 9]]
# a=lol[0]+lol[1]+lol[2]
# print(a)
# print()

# for b in a :
#     print(b)

# for a in lol:
#     for b in a:
#         print(b)

# 5번*****

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# output= [[], [], []]

# for number in numbers:
#     output[(number-1)%3].append(number)
# print(output)

# 번외 *로 피라미드 만들기
# a=[1,2,3,4,5]
# for b in a:
#     c=b+(b-1)
#     print("{0:^9}".format("*"*(c)))

# 딕셔너리 = {
#     "키A":"값A", # 키에는 "문자열", 숫자, 불, 튜플
#     "키B":"값B", # 값에는 구분없이 모두 가능
#     "키C":"값C",
# }
# print(딕셔너리["키A"])
# print(딕셔너리["키B"])
# print(딕셔너리["키C"])

# 170P 예제

# dic={
#     "name":"7D 건조 망고",
#     "type":"당절임",
#     "ingredient":["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
#     "origin":"필리핀"
# }

# for key in dic:
#     print(key, ":", dic[key])

# dic["key"]="value"
# for key in dic:
#     print(key, ":", dic[key])

# del dic["key"]
# for key in dic:
#     print(key, ":", dic[key])

# 168P 예제

# dic={
#     "name":"7D 건조 망고",
#     "type":"당절임",
#     "ingredient":["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
#     "origin":"필리핀"
# }

# key=input("> 접근하고자 하는 키:")

# if key in dic:
#     print(dic[key])
# else:
#     print("존재하지 않는 키에 접근하고 있습니다.")

# 169P 예제

# dic={
#     "name":"7D 건조 망고",
#     "type":"당절임",
#     "ingredient":["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
#     "origin":"필리핀"
# }

# value=dic.get("존재하지 않는 키")
# print("값:", value)

# if value == None:
#     print("존재하지 않는 키에 접근하였습니다.")

# 171~173P 확인문제

# 1번
# dict_a={}
# dict_a['name']='구름'
# print(dict_a)
# del dict_a['name']
# print(dict_a)

# 2번
# pets = [
#     {"name":"구름", "age":5},
#     {"name":"초코", "age":3},
#     {"name":"아지", "age":1},
#     {"name":"호랑이", "age":1}
# ]

# print("# 우리 동네 애완 동물들")
# for a in pets: 
#     print("{} {}살".format(a["name"],a["age"]))
#실행결과
# 우리 동네 애완 동물들
#구름 5살
#초코 3살
#아지 1살
#호랑이 1살


# 3번

# numbers=[1, 2, 6, 8, 4, 3, 2, 1, 9, 5, 4, 9, 7, 2, 1, 3, 5, 4, 8, 9, 7, 2, 3]
# counter={}

# for number in numbers:
#     counter[number]=numbers.count(number)
# print(counter)

# for number in numbers:
#     if number in counter:
#         counter[number]+=1
#     else:
#         counter[number]=1
# print(counter)

# # 실행결과 
# # {1: 3, 2: 4, 6: 1, 8: 2, 4: 3, 3: 3, 9: 3, 5: 2, 7: 2}

# 4번
# character = {
#     "name":"기사",
#     "level": 12,
#     "item":{
#         "sword": "불꽃의검",
#         "armour": "풀플레이트아머"
#     },
#     "skill":["베기", "세게 베기", "아주 세게 베기"]
# }

# for a in character:
#     if type(character[a]) is str:
#         print("{} : {}".format(a, character[a]))
#     elif type(character[a]) is dict:
#         for b in character[a]:
#             print("{} : {}".format(b, character[a][b]))
#     elif type(character[a]) is list:
#         for c in character[a]:
#             print("{} : {}".format(a, c))
# 실행결과
# name : 기사
# level : 12
# sword : 불꽃의 검
# armour : 풀플레이트 아머
# skill : 베기
# skill : 세게 베기
# skill : 아주 세게 베기

# 178P 예제
# for i in range(5):
#     print(str(i) + "=반복 변수")
# print()

# for i in range(5, 10):
#     print(str(i) + "=반복 변수")
# print()

# for i in range(0, 10, 3):
#     print(str(i) + "=반복 변수")
# print()

# 179P 상단 예제

# array=[273, 32, 103, 57, 52]

# for i in range(len(array)):
#     print("{}번째 반복 : {}".format(i+1, array[i]))

# 179P 하단 예제

# for i in range(4, 0-1, -1):
#     print("현재 반복 변수 : {}".format(i))

# 180P 예제

# for i in reversed(range(5)):
#     print("현재 반복 변수 : {}".format(i)) 

# 181P 예제
# while True:
#     print(".", end="")

# 182P 예제
# i=0
# while i <10:
#     print("{}번째 반복합니다.".format(i))
#     i+=1

# 183P 예제
# list_test=[1, 2, 1, 2]
# value=2

# while value in list_test:
#     list_test.remove(value)

# print(list_test)

# 184P 예제 

# import time

# number = 0

# target_tick = time.time() + 5

# while time.time() < target_tick:
#     number+=1

# print("5초 동안 {}번 반복했습니다.".format(number))

# 185P 예제

# i = 0 

# while True:
#     print("{}번째 반복문입니다.".format(i))
#     i+=1

#     input_text = input("> 종료하시겠습니까?(y/n):")
#     if input_text in ["y", "Y"]:
#         print("반복을 종료합니다.")
#         break

# 186P 예제

# numbers=[5, 15, 6, 20, 7, 25]

# for number in numbers:
#     if number < 10 :
#         continue
#     print(number)

# 187~189P 확인문제

# 1번

# range(5) = [0, 1, 2, 3, 4]
# range(4, 6) = a
# range(7, 0, -1) = b
# range(3,8) = [3, 4, 5, 6, 7, 8]
# c = [3, 6, 9]
# a = [4, 5]
# b = [7, 6, 5, 4, 3, 2, 1, 0]
# c = range(3, 10, 3)

# 2번 

# k_l=["name", "hp", "mp", "level"]
# v_l=["기사", 200, 30, 5]
# character={}

# i=0
# while i<4:
#     character[k_l[i]]=v_l[i]
#     i+=1

# print(character)
#{'name': '기사', 'hp': 200, 'mp': 30, 'level': 5}

# 3번*****

# limit = 1000
# i = 1
# sum_value=0

# while sum_value<limit:
#     sum_value+=i
#     i+=1
# print("{}를 더할 대 {}를 넘으며 그 때의 값은 {}입니다.".format(i-1, limit, sum_value))

# 4번********
# max_value = 0
# a = 0
# b = 0

# for i in range(1,99+1):
#     j = 100 - i
#     if max_value < i * j:
#         max_value = i * j
#         a=i
#         b=j
# print("최대가 되는 경우: {} * {} = {}".format(a, b, max_value))

# reversed(), enumerate(), items() 3가지 함수는 1회용

# i=[234, 7768, 535, 3, 23, 345, 65, 8]
# j={"a":123, "b":456, "c":789, "d":1011}

# print(min(i))

# print(max(i))

# print(sum(i))

# for x in reversed(i):
#     print(x, end=" ")

# for y, element in enumerate(i):
#     print(y, element)

# for key, value in j.items():
#     print(key, value)

# 198P 예제상단

# array = []

# for i in range(0, 20, 2):
#     array.append(i*i)

# print(array)

# 198P 예자하단

# array = [i * i for i in range(0, 20, 2)]

# print(array)

# 199P 예제

# array = ["사과", "자두", "초콜릿", "바나나", "체리"]

# output = [fruit for fruit in array if fruit != "초콜릿"]

# print(output)

# 206~207 확인문제

#2번 

# output=[a for a in range(1,100+1) if ("{:b}".format(a)).count("0")==1]

# for i in output:
#     print("{} : {}".format(i, "{:b}".format(i)))

# print("합계:", sum(output))

# output=0

# for i in range(1, 100+1):
#     if "{:b}".format(i).count("0")==1:
#         print("{} : {}".format(i,i))
#         output += i

# print("합계 : {}".format(output))
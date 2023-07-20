# 객체란 무엇인가?

# 객체(object)
# → "속성 + 행위" 를 갖고 있는 것

# Ex)
# 사람
# 속성 : 이름, 나이, 키, 생년월일, IQ ........
# 행위 : 먹는다, 뛴다, 걷는다, 마신다, 본다.............

# 371P 예제

# students = [
#     {"name" : "윤인성", "korean" : 87, "math" : 98, "english" : 88, "science" : 95},
#     {"name" : "연하진", "korean" : 92, "math" : 98, "english" : 96, "science" : 98},
#     {"name" : "구지연", "korean" : 76, "math" : 96, "english" : 94, "science" : 90},
#     {"name" : "나선주", "korean" : 98, "math" : 92, "english" : 96, "science" : 92},
#     {"name" : "윤아린", "korean" : 95, "math" : 98, "english" : 98, "science" : 98},
#     {"name" : "윤명월", "korean" : 64, "math" : 88, "english" : 92, "science" : 92}
# ]

# print("이름", "총점", "평균", sep="\t")

# for student in students:
#     score_sum = student["korean"] + student["math"] + \
#     student["english"] + student["science"]
#     scor_average = score_sum / 4

#     print(student["name"], score_sum, scor_average, sep="\t")

# 371~372P 예제

# def create_student(name, korean, math, english, science):
#     return {
#         "name" : name,
#         "korean" : korean,
#         "math" : math,
#         "english" : english,
#         "science" : science
#     }

# students = [
#     create_student("윤인성", 87, 98, 88, 95),
#     create_student("연하진", 92, 98, 96, 98),
#     create_student("구지연", 76, 96, 94, 90),
#     create_student("나선주", 98, 92, 96, 92),
#     create_student("윤아린", 95, 98, 98, 98),
#     create_student("윤명월", 64, 88, 92, 92)
# ]

# print("이름", "총점", "평균", sep="\t")

# for student in students:
#     score_sum = student["korean"] + student["math"] + \
#     student["english"] + student["science"]
#     scor_average = score_sum / 4

#     print(student["name"], score_sum, scor_average, sep="\t")

# 응용*******

# def create_student(name, korean, math, english, science):
#     return {
#         "name" : name,
#         "korean" : korean,
#         "math" : math,
#         "english" : english,
#         "science" : science
#     }

# students = [
#     create_student("윤인성", 87, 98, 88, 95),
#     create_student("연하진", 92, 98, 96, 98),
#     create_student("구지연", 76, 96, 94, 90),
#     create_student("나선주", 98, 92, 96, 92),
#     create_student("윤아린", 95, 98, 98, 98),
#     create_student("윤명월", 64, 88, 92, 92)
# ]

# print("이름", "총점", "평균", sep="\t")

# def sum(student):
#     return student["korean"] + student["math"] + student["english"] + student["science"]
# def ave(student): 
#     return sum(student) / 4
# def prt(student):
#     print(student["name"], sum(student), ave(student), sep="\t")

# for student in students:
#     prt(student)

# 클래스 구문 사용 ☆☆☆☆☆☆☆☆☆☆☆☆☆

# class Students:
#     def __init__(self, name, korean, math, english, science):
#         self.name = name
#         self.korean = korean
#         self.math = math
#         self.english = english
#         self.science = science 

#     def sum(self):
#         return self.korean + self.math + self.english + self.science
#     def ave(self): 
#         return self.sum() / 4
#     def prt(self):
#         print(self.name, self.sum(), self.ave(), sep="\t")

# students = [
#     Students("윤인성", 87, 98, 88, 95),
#     Students("연하진", 92, 98, 96, 98),
#     Students("구지연", 76, 96, 94, 90),
#     Students("나선주", 98, 92, 96, 92),
#     Students("윤아린", 95, 98, 98, 98),
#     Students("윤명월", 64, 88, 92, 92)
# ]

# print("이름", "총점", "평균", sep="\t")

# for student in students:
#     student.prt()

# 스네이크 케이스와 캐멀 케이스 그리고 클래스
# 스네이크 케이스 i_love_you : i_love_you()와 같이 ()가 있으면 함수, 없으면 변수
# 캐멀 케이스 ILoveYou : 무조건 적으로 클래스명으로 사용
 # *** 다른 언어에서는 첫글자가 소문자인 캐멀 케이스가 사용되나 파이썬에선 미사용

# class Students:
#     pass
# student = Students()

# 클래스(틀, 위 Students) : 학생(객체)에 속성과 행위를 지정하기 위한 틀
# 객체(실체화 된 것, 위 student) : 학생 이름은 "윤인성"이야 라는 실질적인 속성이나 행위를 지정함
# 실체화 된 객체를 "인스턴스"라고 부름

# class Students:
#     def __init__(self):
#         print("객체가 생성되었습니다.")
#     def __del__(self):
#         print("객체가 소멸하였습니다.")
# student = Students() 

#__init__는 class내 함수 실행을 위한 객체를 생성
#__del__는 class내 함수 실행을 위해 생성한 객체를 소멸
#  **** 파이썬에선 __del__ 실제 거의 미사용

# class Students:
#     def __init__(self, name, age):
#         print("객체가 생성되었습니다.")
#         self.name = name
#         self.age = age
#     def __del__(self):
#         print("객체가 소멸하였습니다.")
#     def prt(self):
#         print(self.name, self.age)
# student = Students("이세환", 36) 
# student.prt()


# 211P 예제

# 함수 선언
# def print_3_times():
#     print("안녕하세요")
#     print("안녕하세요")
#     print("안녕하세요")
# 함수 선언
# print_3_times()

# 212P 예제

# def pnt(value, n):
#     for i in range(n):
#         print(value)

# pnt("안녕하세요", 5)

# def 함수이름(매개변수1, 매개변수2, *가변매개변수):
# # 가변매개변수는 함수에 1개만 가능하며, 함수의 매개변수 중 마지막 변수로만 사용이 가능함.
#     print(매개변수1)
#     print(매개변수2)
#     print(가변매개변수)

# 함수이름(0, 1, 2, 3, 4, 5, 6, 7)

# def pnt(value, n=2):
#     # 기본매개변수 함수의 매개변수 중 마지막 변수로만 사용이 가능함.
      # 기본매개변수는 변수가 추가되면 후순위로 밀려서 입력한 변수로 실행됨.
#     for i in range(n):
#         print(value)

# pnt("안녕하세요")

# def f(일반매개변수1, 일반매개변수2, *가변매개변수, 기본매개변수A=10, 기본매개변수B=20):
#     print(일반매개변수1, 일반매개변수2)
#     print(가변매개변수)
#     print(기본매개변수A, 기본매개변수B)

# f(0,1,2,3,4,5,6,7,8,9,10)

# 0, 1
# (2,3,4,5,6,7,8,9,10)
# 10, 20

# def f(일반매개변수1, 일반매개변수2, *가변매개변수, 기본매개변수A=10, 기본매개변수B=20):
#     print(일반매개변수1, 일반매개변수2)
#     print(가변매개변수)
#     print(기본매개변수A, 기본매개변수B)

# f(0,1,2,3,4,5,6,7,8,9,10, 기본매개변수A=203, 기본매개변수B=20202)

# 0, 1
# (2,3,4,5,6,7,8,9,10)
# 203, 20202

# 219P 예제 상단

# def print_n_times(*values, n=2):
#     for i in range(n):
#         for value in values:
#             print(value)
#         print()

# print_n_times("안녕하세요", "즐거운", "파이썬 프로그래밍", n=3)       

# 219P 예제 하단

# def test(a, b=10, c=100):
#     print(a+b+c)

# test(10, 20, 30)    

# test(a=10, b=100, c=200)

# test(c=10, a=100, b=200)

# test(10, c=200)

# 221P 예제

# def return_test():
#     print("A 위치입니다.")
#     return
#     print("B 위치입니다.")

# return_test()

# 223P 예제

# def sum_all(start, end):
#     output=0
#     for i in range(start, end+1):
#         output+=i
#     return output

# sum_all(0, 100)
# print("0 to 100:", sum_all(0, 100))
# print("0 to 1000:", sum_all(0, 1000))
# print("50 to 100:", sum_all(50, 100))
# print("500 to 1000:", sum_all(500, 1000))

# 224P 예제

# def sum_all(start=0, end=100, step=1):
#     output = 0
#     for i in range(start, end + 1, step):
#         output += i
#     return output

# print("A.", sum_all(0, 100, 10))
# print("B.", sum_all(end=100))
# print("C.", sum_all(end=100, step=2))

# 226~227P 확인문제

# 1번

# def f(x):
#     return 2*x+1
# print(f(10))
# def f(x):
#     return x**2+2*x+1
# print(f(10))

# 2번

# def mul(*values):
#     output=1
#     for i in values:
#         output *= i
#     return output

# print(mul(5, 7, 9, 10)) # 3150

# 3번 1,4

# 229P 예제

# def factorial(n):
#     output = 1
#     for i in range(1, n + 1):
#         output *= i
#     return output

# print("1!:", factorial(1))
# print("2!:", factorial(2))
# print("3!:", factorial(3))
# print("4!:", factorial(4))
# print("5!:", factorial(5))

# 230P 예제

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n*factorial(n - 1)

# print("1!:", factorial(1))
# print("2!:", factorial(2))
# print("3!:", factorial(3))
# print("4!:", factorial(4))
# print("5!:", factorial(5))

# 232P 예제

# def fibonacci(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# print("fibonacci(1):", fibonacci(1)) # 1
# print("fibonacci(2):", fibonacci(2)) # 1
# print("fibonacci(3):", fibonacci(3)) # 2
# print("fibonacci(4):", fibonacci(4)) # 3
# print("fibonacci(5):", fibonacci(5)) # 5

# 233P 예제

# counter = 0

# def fibonacci(n):
#     print("fibonacci({})를 구합니다.".format(n))
#     global counter # ***** 함수 밖 변수를 사용하기 위한 global 키워드를 앞에 붙여서 사용
#     counter += 1

#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# fibonacci(10)
# print("-------")
# print("fibonacci(10) 계산에 활용된 덧셈 횟수는 {}번 입니다.".format(counter))

# 236P 예제

# d={
#     1: 1,
#     2: 1
# }
# counter = 0
# def f(n):
#     global counter
#     counter += n
#     if n in d:
#         return d[n] # 레퍼런스를 나타내는 자료형은 global 키워드를 사용하지 않아도 불러옴.
#     else:
#         output = f(n - 1) + f(n - 2)
#         d[n] = output
#         return output

# print("f(10):{}이고, {}번 계산해서 도출한 값입니다.".format(f(10), counter))
# print("f(20):{}이고, {}번 계산해서 도출한 값입니다.".format(f(20), counter))
# print("f(30):{}이고, {}번 계산해서 도출한 값입니다.".format(f(30), counter))
# print("f(40):{}이고, {}번 계산해서 도출한 값입니다.".format(f(40), counter))
# print("f(50):{}이고, {}번 계산해서 도출한 값입니다.".format(f(50), counter))

# 243~245P 확인문제

# 1번

# def flatten(data):
#     a=[]
#     for i in data:
#         if type(i) == int:
#             a.append(i)
#         else:
#             for j in i:
#                 if type(j) == int:
#                     a.append(j)
#                 else:
#                     for k in j:
#                         if type(k) == int:
#                             a.append(k)
#     return a

# def f(d):
#     o=[]
#     for i in d:
#         if type(i) == list:
#             o = o + f(i)
#         else:
#             o += [i]
#     return o

# example = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]

# print("원본:", example) # [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
# print("변환:", f(example)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 1개 테이블당 앉힐 수 있는 최소 사람 수 = 2명
# 1개 테이블당 앉힐 수 있는 최대 사람 수 = 10명
# 전체 사람의 수 100명

# def call_10_times(func): # func
#     for i in range(10):
#         func()

# def print_hello():
#     print("안녕하세요")

# call_10_times(print_hello)

# def call_10_times(func):
#     for i in range(10):
           # func(i)와 같이 다른 함수에서 호출되는 함수를 callback 함수라고 함
#         func(i)

# def print_hello(number):
#     print("안녕하세요", number)

# call_10_times(print_hello)

# def call_10_times(func):
#     for i in range(10):
#         func(i)

# call_10_times(lambda n: print("안녕하세요", n))

# def power(item):
#     return item * item
# def under_3(item):
#     return item < 3

# list_input_a = [1, 2, 3, 4, 5]

# output_a = map(power, list_input_a)
# print("# map() 함수의 실행 결과")
# print("map(power, list_input_a):", output_a)
# print("map(power, list_input_a):", list(output_a))
# print()

# output_b = filter(under_3, list_input_a)
# print("# filter() 함수의 실행결과")
# print("filter(under_3, list_input_a:", output_b)
# print("filter(under_3, list_input_a:", list(output_b))

# 268~269P 확인문제
# numbers=[1, 2, 3, 4, 5, 6]
# print("::".join(
#     map(str, numbers)
#     ))

# numbers = list(range(1, 10 + 1))

# print("# 홀수만 추출하기")
# print(list(filter(lambda a: a % 2 != 0, numbers))) #[1, 3, 5, 6, 7]
# print()

# print("#3 이상, 7미만 추출하기")
# print(list(filter(lambda b: 3<= b < 7, numbers))) #[3, 4, 5, 6]
# print()

# print("# 제곱해서 50미만 추출하기")
# print(list(filter(lambda c: (c*c) < 50, numbers))) #[1, 2, 3, 4, 5, 6, 7]
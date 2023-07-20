# 277P 예제

# u_i_a=input("정수 입력 :")

# if u_i_a.isdigit():
#     n=int(u_i_a)

#     print("원의 반지름 :", n)
#     print("원의 둘레 :", 2*3.14*n)
#     print("원의 넓이 :", 3.14*n*n)
# else:
#     print("정수를 입력하지 않았습니다.")

# 응용
# while True:
#  u_i_a=input("정수 입력 :")

#  if u_i_a.isdigit():
#      n=int(u_i_a)
 
#      print("원의 반지름 :", n)
#      print("원의 둘레 :", 2*3.14*n)
#      print("원의 넓이 :", 3.14*n*n)
#      break
#  else:
#      print("정수를 입력하지 않았습니다.")

# 279P 예제

# try:
#     n_i_a = int(input("정수 입력 :"))

#     print("원의 반지름 :", n_i_a)
#     print("원의 둘레 :", 2*3.14*n_i_a)
#     print("원의 넓이 :", 3.14*n_i_a*n_i_a)
# except:
#     print("무언가 잘못되었습니다.")
 
# 응용

# while True:
#  try:
#      n_i_a = int(input("정수 입력 :"))
 
#      print("원의 반지름 :", n_i_a)
#      print("원의 둘레 :", 2*3.14*n_i_a)
#      print("원의 넓이 :", 3.14*n_i_a*n_i_a)
#      break
#  except:
#      pass

# 280P 예제

# list_input_a = ["52", "273", "32", "스파이", "103"]

# list_number = []

# for item in list_input_a:

#     try:
#         float(item)
#         list_number.append(item)
#     except:
#         pass

# print("{} 내부에 있는 숫자는".format(list_input_a))
# print("{}입니다.".format(list_number))

# 288P 예제

# def test():
#     print("test() 함수의 첫 줄입니다.")
#     try:
#         print("try 구문이 실행되었습니다.")
#         return
#         print("try 구문의 return 키워드 뒤입니다")
#     except:
#         print("except 구문이 실행되었습니다.")
#     else:
#         print("else 구문이 실행되었습니다.")
#     finally:
#         print("finally 구문이 실행되었습니다.")
#     print("test() 함수의 마지막 줄입니다")

# test()

#응용 except에서 리턴

# def test():
#     print("test() 함수의 첫 줄입니다.")
#     try:
#         print("try 구문이 실행되었습니다.")
#         [1, 2, 3][10]
#         print("try 구문의 return 키워드 뒤입니다")
#     except:
#         print("except 구문이 실행되었습니다.")
#         return
#     else:
#         print("else 구문이 실행되었습니다.")
#     finally:
#         print("finally 구문이 실행되었습니다.")
#     print("test() 함수의 마지막 줄입니다")

# test()

# 응용 break사용

# while True:
#     print("test() 함수의 첫 줄입니다.")
#     try:
#         [1, 2, 3][5]
#         print("try 구문이 실행되었습니다.")
#         print("try 구문의 return 키워드 뒤입니다")
#     except:
#         print("except 구문이 실행되었습니다.")
#         break
#     else:
#         print("else 구문이 실행되었습니다.")
#     finally:
#         print("finally 구문이 실행되었습니다.")
#     print("test() 함수의 마지막 줄입니다")

# 289P 예제

# def write_text_file(filename, text):
#     try:
#         file = open(filename, "w")
#         return
#         file.write(text)
#     except exception as e:
#         print(e)
#     finally:
#         file.close()

# write_text_file("test.txt", "안녕하세요!")

# 291~293P 확인문제 

# 2번

# numbers = [52, 273, 32, 103, 90, 10, 275]

# print("# (1) 요소 내부에 있는 값 찾기")
# print("- {}는 {} 위치에 있습니다.".format(52, numbers.index(52)))
# print()

# print("# (2) 요소 내부에 없는 값 찾기")
# number = 10000


#     print("- {}는 {} 위치에 있습니다.".format(number, numbers.index(number)))

#     print("- 리스트 내부에 없는 값입니다.")
# print()

# print("--- 정상적으로 종료되었습니다. ---")

# # (1) 요소 내부에 있는 값 찾기
# - 52는 0 위치에 있습니다.

# # (2) 요소 내부에 없는 값 찾기
# - 리스트 내부에 없는 값입니다.

# --- 정상적으로 종료되었습니다. ---

# 1. 조건문으로 실행결과가 나오도록 작성

# numbers = [52, 273, 32, 103, 90, 10, 275]

# print("# (1) 요소 내부에 있는 값 찾기")
# print("- {}는 {} 위치에 있습니다.".format(52, numbers.index(52)))
# print()

# print("# (2) 요소 내부에 없는 값 찾기")
# number = 10000

# if number in numbers:
#     print("- {}는 {} 위치에 있습니다.".format(number, numbers.index(number)))
# else:
#     print("- 리스트 내부에 없는 값입니다.")
# print()

# print("--- 정상적으로 종료되었습니다. ---")

# 2. Try except 구문으로 실행결과가 나오도록 작성

# numbers = [52, 273, 32, 103, 90, 10, 275]

# print("# (1) 요소 내부에 있는 값 찾기")
# print("- {}는 {} 위치에 있습니다.".format(52, numbers.index(52)))
# print()

# print("# (2) 요소 내부에 없는 값 찾기")
# number = 10000

# try:
#     print("- {}는 {} 위치에 있습니다.".format(number, numbers.index(number)))
# except:
#     print("- 리스트 내부에 없는 값입니다.")
# print()

# print("--- 정상적으로 종료되었습니다. ---")

# 3번

# output = 10 + "개"    # 예외 TypeError
# int("안녕하세요")      # 예외 ValueError
# cursor.close)         # 구문 오류 SyntaxError
# [1, 2, 3, 4, 5][10]   # 예외 IndexError

# 295P 예제

# try:
#     number_input_a = int(input("정수 입력:"))
    
#     print("원의 반지름:", number_input_a)
#     print("원의 둘레:", 2*3.14*number_input_a)
#     print("원의 넓이:", 3.14*number_input_a*number_input_a)
# except Exception as exception:
#     print("type(exception):", type(exception))
#     print("exception:", exception)

# 296P 예제

# list_number = [52, 273, 32, 72, 100]

# try:
#     number_input = int(input("정수 입력:"))
#     print("{}번째 요소 : {}".format(number_input, list_number[number_input]))
# except Exception as exception:
#     print("type(exception):", type(exception))
#     print("exception:", exception)

# 응용

# a = [101, 205, 93, 7, 574, 3285]

# try:
#     i = int(input("0~5까지 정수를 입력하세요 :"))
#     print(a[i])
# except ValueError as ex:
#     print("입력한 값에 문제가 있습니다.")
# except IndexError as ex:
#     print("0~5까지 정수만을 입력해 주세요.")
# except Exception as ex:
#     print("식별할 수 없는 예외가 발생하였습니다.")

# 307~308P 확인문제 

# 1번

# 예외를 발생시키는 키워드는? raise
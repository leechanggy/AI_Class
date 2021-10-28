#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#print() 연습
# 하나만 출략합니다.
print("# 하나만 출력합니다")
print("Hello Python Programming...!")
print()

# 여러 개를 출력합니다.
print('# 여러 개를 출력합니다.')
print(10,20,30,40,50)
print("Hello, ' Good ', Morning!!")
print()

# 아무것도 입력하지 않으면 단순하게 줄바꿈합니다.
print("# 아무것도 출력하지 않습니다")
print("---확인 전용선----")
print()
print()
print("---확인 전용선----")


# In[ ]:


# \를 이용한 특수문자 출력, \n은 newline, \t는 tab을 의미
print("\안녕하세요\" ~~~")


# In[ ]:


# 출력 연습
print("이름Wt나이\t지역)


# In[ ]:


# 여러 라인의 문자열 만들기
print("동해물과 백두산이\n마르고 닳도록\n하느님이")
print('''동해물과 백두산이
마르고 닳도록
하느님이''')
print("""동해물과 백두산이
마르고 닳도록
하느님이""")
a_str = """동해물과 백두산이
마르고 닳도록
하느님이"""
print(a_str)


# In[ ]:


# 문자열 연산자 : +. *
# 문자열 + 문자열 => 문자열 이어 붙이기
# 문자열 * 숫자 => 문자열을 숫자만큼 반복
print("hello" + " world")  # hello world
print("hello" * 2)  # hellohello
print(2 * "hello")  # hellohello


# In[ ]:


# 문자열 index 및 slice => str[0] : 0번지 값, str[1:4] => start:end 여기서 start는 포함, end는 포함하지 않음
str = "안녕하세요"
print(str)
print(str[0], str[2])  # 안 하
print(str[-1], str[-5])  #요 안
print(str[1:4])  # 녕하세
print(len(str))  # len(문자열...)  길이를 구하는 함수
# print(str[5]) index error


# In[ ]:


# str = "임의로 문자를 넣으세요." str[3:], str[:3]
# str의 길이를 구해서 처음 문자를 -인덱스로 구해거 출력하세요
str = "abcd test cdaf rqeteq gdsaga gagad"
print(str[0]," : ", str[-len(str)])
str_len = len(str)  # str의 길이를 구함
print(str[-str_len])


# In[ ]:


# 숫자 : 정수, 실수
# 연산자 : +, -, *, /, //(몫). %(나머지), **(거듭제곱), 우선순위가 있으니 ()로 우선순위 결정
print(" 10 + 5 ", 10 + 5); print(" 10 - 5 ", 10 - 5)
print(" 10 * 5 ", 10 * 5); print(" 10 / 5 ", 10 / 5)
print(" 10 // 3 ", 10 // 3); print(" 10 % 3 ", 10 % 3); print(" 10 ** 3 ", 10 ** 3)


# In[ ]:


# 변수 : 값을 저장하는 공간, 메모리에 방을 만듬, int(값) 정수로 변환, float(), str()
pi = 3.14
print(int(pi + 2))
print(pi - 2)
print(pi * 2)

print("string " + "10")
str(10) + "abcd"


# In[ ]:


# 복합 대입 연산자
num = 100
num += 10; num += 20
print(" num = ", num)  # num = 130

str = "abcd"
str += "test"
str *= 2
print("str : ", str) #abcdtestabcdtest


# In[2]:


# 키보드로부터 입력을 받는 함수 input()
str = input("문자열 입력 > ")
print(str)
# 문자열을 입력받아 문자열의 길이를 출력, 처음 글자와 마지막 글자를 출력 하세요
# 마지막 글자는 문자열의 길이를 구한 값으로 출력
str_len = len(str)
print("str length : ", str_len, str[0],str[str_len -1] )


# In[7]:


# 숫자 두개를 입력받아 정수령으로 바꾸고
# 두 수의 사칙연산을 출력하세요
# 문자열을 입력받아 처음 입력받은 숫자만큼 반복해서 출력하세요
num_1 = int(input(" 숫자 입력 : "))
num_2 = input(" 숫자 입력 : ")
print(type(num_1), type(num_2))  # str -> int 형으로 변경 int()
#print(num_1 + num_2); print(num_1 - num_2)
num_2 = int(num_2)
print(type(num_1), type(num_2))
# 두 수의 사칙연산 출력 num_1 + num_2, num_1 - num_2, *, /, %,..
print(num_1 + num_2); print(num_1 - num_2)
input_str = input("문자열 입력 : ")
print((input_str +'\n') * num_1)


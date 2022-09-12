# 01-1 숫자형 자료형
a = 3
b = 4
print(a+b)
# 더하기
print(a*b)
# 곱하기
print(a/b)
# 나누기
print(a//b) 
# 나눴을 때의 몫
print(a**b)
# 제곱
print(a%b)
# 나머지

# 01-2 문자열 자료형
z = "python"
y = " is fun!"

print(z + y)
print(z * 10)

#01-3 인덱싱 ( -는 역방향 의미)
c = "Life is too short, You need Python"
print(c[0]) # 첫 글자
print(c[1]) # 두번째 글자
print(c[-1]) # 맨뒤글자


# 01-4 슬라이싱(Slicing) - 문자를 자른다
# c[이상:미만:간격]
d = "20010311Rainy"

print(d[:8])

# 01-5 문자열 포멧팅
# %d가 들어간 자리에 뒤에 숫자가 들어감
e = "I eat %d apples." % 3
print(e)

number = 10
day = "three"
f = "I ate %d aples. so I was sick for %s days" % (number, day)
print(f)

g = "asdf {age} asdfa asfd {name} asdfasdf".format(name = "송우기", age = 24)
print(g)

# 01-5 소수점 표현하기
h = "%0.4f" % 3.42134234
# 간격. 소수점 남기는 자리 수
print(h)

# 01-6 count
i = "hobby"
# 인덱스가 0부터시작해서 순차적으로 진행 ex)y의 경우4번째
print(i.find('y'))
# 두번째 b는 걸리지 않음, 변수에 없는 문자인 경우 -1로 표시됨

# 01-7 문자열 삽입(join)
j = ",".join(['a', 'b', 'c', 'd'])
# 앞에 , 기준으로 문자열을 삽입한다
print(j)

# 01-8 소문자를 대문자로 바꾸기(upper), 대문자를 소문자로 바꾸기(lower)
print(z.upper())
print(z.lower())

# 01-9 공백지우기, 양쪽 공백 지우기(strip)
print(y.strip())

# 01-10 문자열 바꾸기(replace)
# replace(바뀌게 될 문자열, 바꿀 문자열)처럼 사용해서 문자열 안의 특정한 값을 다른 값으로 치환해 준다.
print(c.replace("Life", "Your mind"))

# 01-11 문자열 나누기(split)
# split 함수는 a.split()처럼 괄호 안에 아무 값도 넣어 주지 않으면 공백(스페이스, 탭, 엔터 등)을 기준으로 문자열을 나누어 준다
k = "a:b:c:d"
print(k.split(":"))

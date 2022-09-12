# 리스트를 만들 때 대괄호([ ])로 감싸 주고 각 요솟값은 쉼표(,)로 구분해 준다.
# a = ["동해", "서해", "남해", ["int", "북해"]]

# print(a[3][1])
# 리스트안에 리스트를 넣을 수 있고 무한 반복할 수 있음

# 리스트도 인덱싱, 슬라이싱, 사칙연산 가능

# 리스트 교체
# a[0] = "청룡"

# 리스트 삭제
# a[1] = []

# print(a)

# 리스트 관련 함수들

# 리스트에 요소 추가(append)
a = [2, 1, 3]
a.append(4)
print(a)

# 리스트 정렬(sort), 문자의 경우 가나다, 알파벳순, 숫자는 크기순으로 정렬
a.sort()
print(a)


# 리스트 뒤집기(reverse)
a.reverse()
print(a)

# 위치 반환(index)
print(a.index(3))


# 리스트에 요소 삽입(insert) 특정 index에 삽입가능
b = [1, 5, 3]
b.insert(0,4) # 4를 0번째 인덱스에 추가하라

print(b)

# 리스트 요소 제거(remove) - 지우고자하는 값을 제거한다
b.remove(1)

print(b)

# 리스트 요소 끄집어내기(pop) - 리스트 중 마지막 것이 튀어 나감
print(b.pop())

print(b)

# 리스트에 포함된 요소 x의 개수 세기(count)
c = [1, 5, 3, 1, 1, 1]

print(c.count(1))

# 리스트 확장(extend)
c.extend([4,6])
print(b)
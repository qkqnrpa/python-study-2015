# define
t1 = ()
t2 = (1,) # 하나일 땐 , 필요
t3 = (1,2,3)
t4 = 1,2,3 # 괄호 생략 가능
t5 = ('a', 'b', ('foo', 'bar'))
t6 = ('a', 'b', ['foo', 'bar'])

t6[2].append('quz')
print(t6) # ('a', 'b', ['foo', 'bar', 'quz'])

# indexing
print(t4[1]) # 2

# slicing
print(t5[:2]) # ('a', 'b')

# calc
print(t2 + t3) # (1, 1, 2, 3)
print(t3 * 2) # (1, 2, 3, 1, 2, 3)

# del t1[0] # 요소 값 제거 시 에러
# t1[0] = 2 # 요소 값 변경 시 에러
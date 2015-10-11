# define
a = list() # = [] (new 연산자가 필요없다)

# indexing
arr = [1, 2, 3, 4, 5]
print(arr[1] + arr[-1]) # 7 = 2+5 (-인덱스 접근 가능)

twoD = [['foo', 'bar'], [1, 2]] # 변수 이름은 숫자로 시작할 수 없다
print(twoD[0][1]) # bar

# slicing
piece = arr[1:4]
print(piece) # [2, 3, 4]
print(arr[:3]) # [1, 2, 3]
print(arr[2:]) # [3, 4, 5]

# calc
print(arr + piece) # [1, 2, 3, 4, 5, 2, 3, 4]
print(piece * 3) # [2, 3, 4, 2, 3, 4, 2, 3, 4]

# element changing
piece[2] = 5
print(piece) # [2, 3, 5]

arr[1:4] = [6, 7]
print(arr) # [1, 6, 7, 5]

arr[1:3] = []
print(arr) # [1, 5]

del arr[1]
print(arr) # [1]

# functions
arr.append(2)
print(arr) # [1, 2]

arr.append([3, 4])
print(arr) # [1, 2, [3, 4]]

arr = [4, 2, 3, 1]
arr.sort()
print(arr) # [1, 2, 3, 4] (문자가 섞여 있으면 안 된다)

sArr = ['d', 'b', 'c', 'a']
sArr.sort()
print(sArr) # ['a', 'b', 'c', 'd']

sArr = ['d', 'b', 'a', 'c', 'a']
sArr.reverse()
print(sArr) # ['a', 'c', 'b', 'd']

print(sArr.index('a', 2)) # 2 (존재하지 않으면 에러)

arr.insert(1, [3, 4])
print(arr) # [1, [3, 4], 2, 3, 4]

arr.remove([3, 4]) # 같은 요소 중 첫번째만 제거, 다르면 에러
print(arr) # [1, 2, 3, 4]

print(arr.pop(), arr) # 4 [1, 2, 3]
print(arr.pop(1), arr) # 2 [1, 3]

print(sArr.count('a')) # 2

arr.extend([4, 5]) # arr += [4, 5] 와 같다.
print(arr) # [1, 3, 4, 5]
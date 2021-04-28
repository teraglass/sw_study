# 2차원 list
# List 순회 : n x m List의 n*m 개의 모든 원소를 빠짐없이 조사하는 방법

#  1. 행 우선 순회
#  ex)
arr = [[0,1,2,3],
        [4,5,6,7],
        [8,9,10,11]]
# i : 행의 좌표, n = len(arr)
# j : 열의 좌표, m = len(arr[0])

for i in range(len(arr)):
    for j in range(len(arr[0])):
        arr[i][j] # 필요한 연산 수행

# 2. 열 우선 순회
# i : 행의 좌표, n = len(arr)
# j : 열의 좌표, m = len(arr[0])

for j in range(arr[0]):
    for i in range(len(len(arr))):
        arr[i][j] # 필요한 연산 수행

# 3. 지그재그 순회 : List의 행을 좌우로 조사하는 방법
# i : 행의 좌표, n = len(arr)
# j : 열의 좌표, m = len(arr[0])

for i in range(len(arr)):
    for j in range(len(arr[0])):
        arr[i][j + (m-1-2*j)*(i%2)]
         # 필요한 연산 수행

# 델타를 이용한 2차 list 탐색
#     1. 2차 list의 한 좌표에서 네 방향의 인접 list 요소를 탐색할 때 사용하는 방법
#     2. 델타 값은 한 좌표에서 네 방향의 좌표와 x,y의 차이를 저장한 list로 구현
#     3. 델타 값을 이용하여 특정 원소의 상하좌우에 위치한 원소에 접근할 수 있음
#     tip. 이차원 list의 가장자리 원소들은 상하좌우 네 방향에 원소가 존재하지 않을 경우가 있으므로, 
#     inedex를 체크하거나 index의 범위를 제한해야 함       
# ex)
# arr[0...n-1][0...n-1] : 2차원 list
dx = [0,0,-1,1]
dy = [-1,1,0,0]

for x in range(len(arr)):
    for y in range(len(arr[x])):
        for i in range(4):
            testX = x + dx[i]
            testY = y + dy[i]
            print(arr[testX][testY])


# 전치 행렬 : 행과 열의 값이 반대인 행렬을 의미
# i : 행의 좌표, n = len(arr)
# j : 열의 좌표, m = len(arr[0])
arr = [[1,2,3],[4,5,6],[7,8,9]] # 3*3 행렬
for i in range(3):
    for j in range(3):
        if i < j : 
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

#  - zip(iterable*) : 동일한 개수로 이루어진 자료형들을 묶어 주는 역할을 하는 함수
# . 두 자료형의 길이가 다르면 작은 길이의 자료형의 길이에 맞춰 묶어짐
alpha = ['a','b','c']
index = [1,2,3]
alpha_index = zip(alpha,index) 
print(alpha_index) # -> ('a',1),('b',2),('c',3) 각 value를 튜플 객체로 돌려줌, 딕셔너리나 리스트 형태로 사용가능

# zip 함수의 인자로 list를 행별로 쪼개서 사용할 수 있음
arr = [[1,2,3],[4,5,6],[7,8,9]]
print(list(zip(*arr))) # >>> [(1,4,7),(2,5,8),(3,6,9)]

# zip(*matrix) : 전치 행렬



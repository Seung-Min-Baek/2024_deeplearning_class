import numpy as np

x = np.array([[51,55],[14,19],[0,4]])

print(x.ndim)
print(x.shape)
print(x.dtype)

for row in x:
    print(row)

# 슬라이싱
y = x[1:3, 0:2]
print(y)

print(x[x>10]) # x 원소 중 10보다 큰 원소 출력

y[0,0] = 1400

print(x) # 위에 y를 바꾸어서 x도 값이 바뀐다. 조심!!

# 위의 문제를 해결하기 위해 copy()를 사용한다.
Y = x[1:3, 0:2].copy()
Y[0,0] = 14
print(x) # Y를 복사해 놓은 상태라 Y를 바꾸어도 x 값은 바뀌지 않는다.

# range(10)과 비슷한 것 중 numpy에 arange(10)이 있다.
print(np.arange(10))

# numpy 안에 reshape 있다.
print(np.arange(12).reshape((3,4)))
print(np.arange(12).reshape((2,2,3)))

# C스타일, F스타일은 그냥 넘어가기 숫자가 써지는 순서이므로 참고만

# 브로드캐스트 : numpy 연산을 하기 위해서는 행렬의 사이즈가 모두 같아야 하는데 자동으로 사이즈가 맞춰지는 것을 말한다.
k = np.arange(6).reshape((2,1,3))
# 2 x 1 x 3
#         3 처럼 앞에 숫자가 없던지, 같은 위치에 둘 중 한 자리가 1이던지, 숫자가 같아야 브로드캐스트 연산이 가능하다.
# 3처럼 뒤에서부터 자리를 차지한다.

a = np.arange(12).reshape(2,6) #(2,6)
b = a.reshape(3,4)
# a + b 는 연산이 안된다.
print(a)
print(b)

c = np.array([[1],[2]])
print(c)
print(c.shape) # (2,1)
print(a+c) # 는 계산 가능하다. C의 값들이 a의 6자리만큼 복사가 되어서 더해진다.
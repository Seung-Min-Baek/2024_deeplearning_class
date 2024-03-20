import numpy as np
arr = np.arange(12).reshape(2, 3, 2)
print(arr)

# 축끼리 덧셈
print(arr.sum(axis=0)) # [[0+6 1+7][2+8 3+9][4+10 5+11]] (3,2)
print(arr.sum(axis=1)) # [[0+2+4 1+3+5][6+8+10 7+9+11]] (2,2)
print(arr.sum(axis=2)) # [[0+1 2+3 4+5][6+7 8+9 10+11]] (2,3)

# transpose
A = np.arange(1,13).reshape(3,2,2)
B = A.transpose(1,2,0)
print(B)

# 패딩 ( np.pad(x, pad_width,mode))
a = np.pad([1,2,3],(1,2),'constant',constant_values=(-1,-2)) # constant_value 설정 안하면 0으로 자동 설정
print(a)

x = np.arange(1, 13).reshape(3, 4)
np.pad(x, ((1, 2), (3, 4)), mode='constant', constant_values=((-1,-2), (-3, -4))) # ((위,아래)(오른쪽 왼쪽))

# uint8 : unsigned 정수 : 부호가 안붙은 양수
arr = np.array(np.arange(10))
print('타입: {}, 배열: {}'.format(arr.dtype, arr)) # 32비트
arr = arr.astype(np.uint8)                          #-> size 큰걸로 변환하면 안전하지만 32비트를 8비트로 작게 변환하면 문제가 생길수 있기에 조심하여야한다.
print('타입: {}, 배열: {}'.format(arr.dtype, arr)) # 8비트

# matplotlib은 보통 numpy 배열로 사용한다.
import matplotlib.pyplot as plt

x = np.arange(0,6,0.1)
y = np.sin(x)
plt.plot(x,y)
plt.show()
plt.plot([1,2,4],[4,1,2])
plt.show()

# 한글 폰트
from matplotlib import font_manager
from matplotlib import rc

fonts = font_manager.findSystemFonts()
print(fonts[:5])
print(len(fonts))
print([font for font in fonts if 'malgun' in font])

font_name = font_manager.FontProperties(fname='C:\\Windows\\Fonts\\malgunsl.ttf').get_name()
rc('font',family = font_name)
fig, ax = plt.subplots() # fig : window(plt.show() 같은 역할), ax : window 안의 그림(axis의 복수형)

ax.plot([1,2,3],[3,2,1],label='한글 테스트')
ax.legend()
plt.show()

from matplotlib.image import imread
img = imread(r"C:\Users\백승민\Desktop\KakaoTalk_20230409_182347668.jpg") # 경로에 한글 있으면 맨 앞에 r 추가
plt.imshow(img)
plt.show()

#---------------------------------------------------------------------------------

# 퍼셉트론
## and 게이트
def AND(x1, x2):
  w1, w2, beta = 0.5, 0.5, 0.7
  tmp = x1 * w1 + x2 * w2
  if tmp <= beta:
    return 0
  elif tmp > beta:
    return 1
  
## nand 게이트
def NAND(x1, x2):
  w1, w2, beta = -0.5, -0.5, -0.7
  tmp = x1 * w1 + x2 * w2
  if tmp <= beta:
    return 1
  elif tmp > beta:
    return 0

print("NAND(0, 0)={}, NAND(1, 0)={}, NAND(0, 1)={}, NAND(1, 1)={}".format(NAND(0, 0), NAND(1, 0), NAND(0, 1), NAND(1, 1)))

## or 게이트
def OR(x1,x2):
  w1, w2, beta = 0.5, 0.5, 0.3
  tmp = x1 * w1 + x2 * w2
  if tmp <= beta:
    return 0
  elif tmp > beta:
    return 1
  
print("OR(0, 0)={}, OR(1, 0)={}, OR(0, 1)={}, OR(1, 1)={}".format(OR(0, 0), OR(1, 0), OR(0, 1), OR(1, 1)))
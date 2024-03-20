w=5
h=4
a = w*h
print("area =", a)

initial_velocity = 5
accel_of_gravity = 9.81
TIME = 0.6
VerticalPositionOfBall = initial_velocity*TIME - \
                         0.5*accel_of_gravity*TIME**2 ## 백슬래시는 다음 줄에 이어지는 것을 나타낼때 사용

# 객체에는 속성과 메소드로 이루어져있다
# 객체에는 상태와 상태를 바꿀수 있는 메소드가 있다.

# 클래스 안의 def(함수)는 메소드라고 하고, def(함수)와 같은 기능을 한다. 
# 클래스 : 붕어빵(인간) 만드는 기계, 인스턴스 : 붕어빵(인간) = 객체
# 인간을 찍어내면 name이 생긴다. (즉, 인간(self)을 찍어내면 이름이 생긴다.)

# __init__ (메소드) : 내장된 함수를 불러 쓰는 용도

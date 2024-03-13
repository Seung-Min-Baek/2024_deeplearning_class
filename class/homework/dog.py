class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('이름과 나이 입력완료')
    def sit(self):
        print(self.name + '가 앉았습니다')
    def roll(self):
        print(self.name +'가 구릅니다')

dog = Dog('똥개',5)
dog.sit()
dog.roll()
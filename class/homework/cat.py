class Cat:
    def __init__(self, name):
        self.name = name
        print('이름 입력완료')
    def yell(self):
        print('야옹')

cat = Cat('야옹이')
cat.yell()

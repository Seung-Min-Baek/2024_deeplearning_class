import numpy as np

class Perceptron():
    """퍼셉트론 학습 알고리즘"""

    def __init__(self,input_size, threshold=100,title=''):
        self.threshold = threshold
        self.weights = np.zeros(input_size +1)
        self.title = title
        self.count = 0

    def predict(self, inputs):
        summation = np.dot(inputs, self.weights[1:]) + self.weights[0]
        if summation > 0:
            activation = 1
        else:
            activation = -1
            #activation = 0
        return activation
    
    def train(self, training_inputs, labels):
        print("training...")
        for _ in range(self.threshold):
            m = 0
            for input, label in zip(training_inputs, labels):
                summation = np.dot(input, self.weights[1:]) + self.weights[0]
                if summation * label <= 0:
                    print(
                        f"weights:{self.weights}, input:{input}, label:{label}, sum:{summation}")
                    self.weights[1:] += label * input
                    self.weights[0] += label
                    m += 1
                    self.count += 1
            if m ==0:
                break

    def print_result(self, inputs):
        print(10*'-', self.title)
        print('trained weights:', self.weights)
        print(f'total counts:  {self.count}' )
        for x in inputs:
            print('{}, {}'.format(x, self.predict(x)))
        print(10*'-', self.title)

if __name__ == '__main__':
    # AND 게이트
    training_inputs = np.array([[0,0],[1,0],[0,1],[1,1]]) 
    labels = np.array([-1, -1, -1, 1]) # [0,0,0,1] 로 했을 시 이 코드에서는 30번째 줄에서 0을 곱했을 경우 값이 이상하게 나올 수 있다.

    perceptron = Perceptron(2, title='AND 게이트', threshold=10)
    perceptron.train(training_inputs, labels)
    perceptron.print_result(training_inputs)

    # OR 게이트
    training_inputs = np.array([[0,0],[1,0],[0,1],[1,1]]) 
    labels = np.array([-1, 1, 1, 1]) # [0,1,1,1] 로 했을 시 이 코드에서는 30번째 줄에서 0을 곱했을 경우 값이 이상하게 나올 수 있다.

    perceptron = Perceptron(2, title='OR 게이트', threshold=10)
    perceptron.train(training_inputs, labels)
    perceptron.print_result(training_inputs)

    # NAND 게이트
    training_inputs = np.array([[0,0],[1,0],[0,1],[1,1]]) 
    labels = np.array([1, 1, 1, -1]) # [1,0,0,0] 로 했을 시 이 코드에서는 30번째 줄에서 0을 곱했을 경우 값이 이상하게 나올 수 있다.

    perceptron = Perceptron(2, title='NAND 게이트', threshold=10)
    perceptron.train(training_inputs, labels)
    perceptron.print_result(training_inputs)

    # 임의의 게이트
    training_inputs = np.array([[0,0],[1,0],[0,1],[1,1],[2,1],[8,9],[7,8],[6,5],[5,8],[1,8]]) 
    labels = np.array([-1, -1, -1,-1,-1,1,1,1,1,1]) # [1,0,0,0] 로 했을 시 이 코드에서는 30번째 줄에서 0을 곱했을 경우 값이 이상하게 나올 수 있다.

    perceptron = Perceptron(2, title='임의의 게이트', threshold=10)
    perceptron.train(training_inputs, labels)
    perceptron.print_result(training_inputs)


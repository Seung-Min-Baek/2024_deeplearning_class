# 0313

## numpy

* numpy 배열은 리스트가 아니다.
* numpy 배열은 연산 시 안에 들어가 있는 원소의 type이 같아야한다.
* x.shape / x.ndim(x의 차원) / x.dtype (datatype)
* shape이 casting(자동 형변환) 되는 것들 (int32, float)은 자동 형 변환이 되어 연산이 된다.
* numpy 배열의 연산은 성분끼리 연산한다.
* 3차원 : b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
* b.shape = (2,2,2)
* 0축의 0, 1축의 1, 2축의 0 즉 b[0,1,0]은 3이다.

# 0315

*
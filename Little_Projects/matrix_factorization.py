import numpy as np
import random
import time

class Case():
    def __init__(self, solution, xn):
        self.solution = solution
        self.A = self.__calculateA(xn)

    def __calculateA(self, xn):
        a = np.array(list(range(np.size(xn[0], 0))))
        for i in self.solution[::-1]:
            a = a.dot(np.linalg.inv(xn[i]))
        return a


class Playground():

    def __init__(self, toOrder=[0, 1, 2, 3], xs=[[1, 0, 2, 3], [0, 2, 1, 3], [0, 1, 3, 2]]):
        self.size = len(toOrder)
        self.A = np.array(toOrder)
        self.B = np.array(list(range(self.size)))
        self.X = self.associatedMatrix(toOrder)
        self.Xn = [self.associatedMatrix(i).T for i in xs]
        self.sizeXn = len(self.Xn)

    def associatedMatrix(self, v: list) -> np.ndarray:
        return np.array([[0 if v[i] != j else 1 for j in range(self.size)] for i in range(self.size)])
    
    def checkFactoization(self, xs: list) -> bool:
        x = np.identity(self.size)
        for i in xs:
            x = x.dot(self.Xn[i])
        return np.array_equal(x, self.X)
    
    def generateRandomSameLengthCases(self, num: int, lenOfLists: int) -> list:
        self.generatedRandomSameLengthCases = [Case([random.randint(0, self.sizeXn - 1) for j in range(lenOfLists)], self.Xn) for i in range(num)]
        return self.generatedRandomSameLengthCases
    
    def generateRandomCases(self, num: int, minLenth: int, maxLenth: int) -> list:
        self.generatedRandomCases = [Case([random.randint(0, self.sizeXn - 1) for j in range(random.randint(minLenth, maxLenth))], self.Xn) for i in range(num)]
        return self.generatedRandomCases

    def searchFactorization(self) -> list:
        return []

a = Playground(toOrder=[2, 1, 3, 0])
print(a.checkFactoization([0, 2, 1, 0])) # True
print(a.checkFactoization([2, 1, 0, 1])) # True
print(a.checkFactoization([1, 2, 1, 0, 2, 1])) # True
print(a.checkFactoization([1, 2, 1, 0, 2])) # False
x = time.time()
a.generateRandomCases(num=1000, minLenth=0, maxLenth=20)
print(time.time() - x)
for i in [random.randint(0, 499) for j in range(12)]:
    b = a.generatedRandomCases[i]
    a2 = Playground(toOrder=b.A)
    print(b.A, b.solution, a2.checkFactoization(b.solution))







import random

class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = []

        for i in range(self.rows):
            self.data.append([])
            for j in range(self.cols):
                self.data[i].append(0)

    def add(self, n):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] += n.data[i][j]

    def copy(self):
        m = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                m.data[i][j] = self.data[i][j]
        return m

    def subtract(a, b):
        result = Matrix(a.cols, a.rows)
        for i in range(result.rows):
            for j in range(result.cols):
                result.data[i][j] = a.data[i][j] - b.data[i][j]
        return result

    def map(self, fn):
        for i in range(self.rows):
            for j in range(self.cols):
                val = self.data[i][j]
                self.data[i][j] = fn(val)

    @staticmethod
    def map_static(m, fn):
        result = Matrix(m.rows, m.cols)
        for i in range(m.rows):
            for j in range(m.cols):
                val = m.data[i][j]
                result.data[i][j] = fn(val)
        return result


    def fromArray(arr):
        m = Matrix(len(arr), 1)
        for i in range(len(arr)):
            m.data[i][0] = arr[i]
        return m
    
    def toArray(m):
        arr = []
        for i in range(m.rows):
            for j in range(m.cols):
                arr.append(m.data[i][j])
        return arr

    def multiply(a, b):
        #check that the col and rows of the 2 matrices are same
        if a.cols == b.rows:
            result = Matrix(a.rows, b.cols)
            for i in range(result.rows):
                for j in range(result.cols):
                    sum = 0
                    #for size of a columns
                    for k in range(a.cols):
                        #go through each row of a and each col of b
                        #multiply them and sum them up and set that cell to that sum
                        sum += a.data[i][k] * b.data[k][j]
                    result.data[i][j] = sum
            return result
        else:
            print("matrices didnt match!")
            return None

    def multiply_scalar(self, n):
        if isinstance(n, Matrix):
            for i in range(self.rows):
                for j in range(self.cols):
                    self.data[i][j] *= n.data[i][j]
        else:
            for i in range(self.rows):
                for j in range(self.cols):
                    self.data[i][j] *= n


    @staticmethod
    def transpose(m):
        result = Matrix(m.cols, m.rows)
        for i in range(m.rows):
            for j in range(m.cols):
                result.data[j][i] = m.data[i][j]
        return result


    def randomize(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] = random.uniform(-1, 1)           

    def print(self):
        for row in self.data:
            for element in row:
                print(element, end=" ")
            print()  # Move to the next line after printing each row




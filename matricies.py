import copy
import re
from calculator import isNum
from helperFunctions import maxElementLength

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.n = len(matrix)
        self.m = len(matrix[0])

    def det(self):
        return determinant(self.m)

    def trace(self):
        if self.m != self.n:
            raise Exception("Can only take the trace of an nxn matrix.")
        t = 0
        for i in range(self.n):
            t += self.matrix[i][i]
        return t
    
    def transpose(self):
        m = []
        for i in range(self.m):
            m.append(getColumn(self.matrix, i))
        return Matrix(m)

    def power(self, power):
        if self.n != self.m:
            raise Exception("Only nxn matricies can be raised to a power.")
        elif power == 0:
            return identityMatrix(self.n)
        m = self
        for i in range(int(power)-1):
            m = matrixMult(m,self)
        return m

    def display(self):
        size = maxElementLength(self.matrix) + 2
        s = ""
        for row in self.matrix:
            for item in row:
                buffer = " " * ((size - len(str(item)))//2)
                s += buffer + str(item) + buffer 
            s += "\n"
        return s

    
    
# Calculates the determinant recursivly using the laplace expansion
# I chose to do the expansion along the first column as opposed to the first row because I thought it would be less typing
def determinant(m):
    if len(m) != len(m[0]):
        raise Exception("Only nxn matricies have determinants.")
    if len(m) == 1:
        return m[0][0]
    det = 0
    for row in range(len(m)):
        submatrix = (m[:row] + m[row+1:])
        for r in range(len(submatrix)):
            submatrix[r] = submatrix[r][1:]
        det += (1 if row % 2 == 0 else -1) * m[row][0] * determinant(submatrix)
    return det

def scalarMult(s,matrix):
    m = copy.deepcopy(matrix.matrix)
    for row in range(len(m)):
        for col in range(len(m[0])):
            m[row][col] *= s
    return Matrix(m)

def matrixAdd(matrix1, matrix2):
    if matrix1.n != matrix2.n or matrix1.m != matrix2.m:
        raise Exception("Matricies of different sizes cannot be added.")
    m = copy.deepcopy(matrix1.matrix)
    for row in range(len(m)):
        for col in range(len(m[0])):
            m[row][col] += matrix2.matrix[row][col]
    return Matrix(m)

def zeroMatrix(n,m):
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(0)
        matrix.append(row)
    return matrix

def identityMatrix(n):
    m = []
    for i in range(n):
        row = []
        for j in range(n):
            x = 1 if i == j else 0
            row.append(x)
        m.append(row)
    return Matrix(m)

def dotProduct(l1,l2):
    x = 0
    for i in range(len(l1)):
        x += l1[i]*l2[i]
    return x

def getColumn(matrix, c):
    x = []
    for row in matrix:
        x.append(row[c])
    return x

def matrixMult(matrix1,matrix2):
    if matrix1.m != matrix2.n:
        raise Exception("These matricies cannot be multiplied.")
    m = zeroMatrix(matrix1.n, matrix2.m)
    for i in range(matrix1.n):
        for j in range(matrix2.m):
            m[i][j] = dotProduct(matrix1.matrix[i], getColumn(matrix2.matrix, j))
    return Matrix(m)

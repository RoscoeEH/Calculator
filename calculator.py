import math
from parser import *
from helperFunctions import *
from matricies import *


def eval(pt):
    label = pt[0]
    if label == "Pi":
        return math.pi
    if label == "E":
        return math.e
    if label == "Num":
        return float(pt[1])
    if label == "Mat":
        return Matrix(buildMatrix(pt[1]))
    if label == "T":
        return "T"
    x = eval(pt[1])
    if label == "Det":
        if type(x) != Matrix:
            raise Exception("You can only take the determinant of a matrix.")
        return determinant(x.matrix)
    if label == "Tr":
        if type(x) != Matrix:
            raise Exception("You can only take the trace of a matrix.")
        return x.trace()
    if label == "Sin":
        if x == "Undefined":
            return "Undefined"
        if type(x) == Matrix:
            raise Exception("Sin does not work over matricies.")
        return math.sin(x)

    if label == "Cos":
        if x == "Undefined":
            return "Undefined"
        if type(x) == Matrix:
            raise Exception("Cos does not work over matricies.")
        return math.cos(x)

    if label == "Tan":
        if x == "Undefined":
            return "Undefined"
        if type(x) == Matrix:
            raise Exception("Tan does not work over matricies.")
        return math.tan(x)

    y = eval(pt[2])

    if label == "Eq":
        if x == "Undefined" or y == "Undefined":
            return "Undefined"
        if type(x) == type(y):
            return x == y
        else:
            raise Exception("Two values of different types cannot be compared for equality.")

    elif label == "Le":
        if x == "Undefined" or y == "Undefined":
            return "Undefined"
        if type(x) == Matrix or type(y) == Matrix:
            raise Exception("Matricies have no notion of order.")
        return x < y

    elif label == "Ge":
        if x == "Undefined" or y == "Undefined":
            return "Undefined"
        if type(x) == Matrix or type(y) == Matrix:
            raise Exception("Matricies have no notion of order.")
        return x > y

    elif label == "Leq":
        if x == "Undefined" or y == "Undefined":
            return "Undefined"
        if type(x) == Matrix or type(y) == Matrix:
            raise Exception("Matricies have no notion of order.")
        return x <= y

    elif label == "Geq":
        if x == "Undefined" or y == "Undefined":
            return "Undefined"
        if type(x) == Matrix or type(y) == Matrix:
            raise Exception("Matricies have no notion of order.")
        return x >= y

    elif label == "Add":
        if x == "Undefined" or y == "Undefined":
            return "Undefined"
        if type(x) == type(y):
            if type(x) == float:
                return x + y
            else:
                return matrixAdd(x,y)
        raise Exception("A matrix and a floating point value cannot be added.")
        

    elif label == "Sub":
        if x == "Undefined" or y == "Undefined":
            return "Undefined"
        if type(x) == type(y):
            if type(x) == float:
                return x - y
            else:
                return matrixAdd(x, scalarMult(-1,y))
        raise Exception("A matrix and a floating point value cannot be subrtacted.")

    elif label == "Mult":
        if x == "Undefined" or y == "Undefined":
            return "Undefined"
        if type(x) == type(y):
            if type(x) == float:
                return x * y
            else:
                return matrixMult(x,y)
        if type(x) == float:
            return scalarMult(x,y)
        else:
            return scalarMult(y,x)

    elif label == "Div":
        if y == 0 or x == "Undefined" or y == "Undefined":
            return "Undefined"
        if type(x) == type(y) and type(x) == float:
            return x / y
        raise Exception("Matricies have no notion of divison.")


    elif label == "Mod":
        if y == 0 or x == "Undefined" or y == "Undefined":
            return "Undefined"
        if type(x) == type(y) and type(x) == float:
            return x % y
        raise Exception("Matricies have no notion of divison.")

    elif label == "Pow":
        if x == "Undefined" or y == "Undefined":
            return "Undefined"
        if type(y) == float:
            if type(x) == float:
                return x ** y
            elif type(x) == Matrix:
                if y % 1 == 0 and y >=0:
                    return x.power(y)
                raise Exception("Matricies cannot be raised to a negative or non-integer power.")
        elif y == "T":
            if type(x) == Matrix:
                return x.transpose()
            else:
                raise Exception("Only matricies have a transpose operation.")
        raise Exception("Nothing can be raised to the power of a matrix.")






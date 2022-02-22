from calculator import *
from parser import *

RESERVED = ["+", "-", "*", "/", "%", "^", "(", ")", "=", "<", ">", "<=", ">="]

addTests = [("4+6", 4+6), ("100 + -22", 100 + -22), ("10+0", 10+0)]

subTests = [("4-6", 4-6), ("100 - -22", 100 - -22), ("10-0", 10-0)]

multTests = [("4*6", 4*6), ("100 * -22", 100 * -22), ("10*0", 10*0)]

divTests = [("8/4", 8/4), ("100 / -20", 100 / -20), ("10/0", "Undefined"), ("0/12", 0/12)]

modTests = [("8%4", 8%4), ("100 % -20", 100 % -20), ("10%0", "Undefined"), ("0%12", 0%12)]

exTests = [("2^4", 2**4), ("100^-2", 100**-2), ("10^0", 10**0)]

eqTests = [("1=1", 1==1), ("10=2", 10 == 2)]

lessTests = [("1<1", 1<1), ("10<2", 10 < 2), ("3<8", 3 < 8)]

greatTests = [("1>1", 1>1), ("10>2", 10 > 2), ("3>8", 3 > 8)]

leqTests = [("1<=1", 1<=1), ("10<=2", 10 <= 2), ("3<=8", 3 <= 8)]

geqTests = [("1>=1", 1>=1), ("10>=2", 10 >= 2), ("3>=8", 3 >= 8)]

parenTests = [("(1+2)*3", (1+2)*3), ("(50+2)*-1", (50+2)*-1), ("3*(1+2)", 3*(1+2))]

orderOfOpsTests = [("1+2*3", 1+2*3), ("70 * -1 + 1",70 * -1 + 1), ("50+50/2", 50+50/2)]

decimalTests = [("1.1+7.9", 1.1+7.9), ("0.5^2", 0.5**2), ("40/0.25", 40/0.25)]

matrixAddTests = [("[[1,2],[3,4]] + [[5,6],[7,8]]", matrixAdd(Matrix([[1,2],[3,4]]), Matrix([[5,6],[7,8]])).matrix), ("[[2,-3],[4,8]] + [[7.9,6],[7,8]]", matrixAdd(Matrix([[2,-3],[4,8]]), Matrix([[7.9,6],[7,8]])).matrix)]

matrixMultTests = [("[[1,2],[3,4]] * [[5,6],[7,8]]", matrixMult(Matrix([[1,2],[3,4]]), Matrix([[5,6],[7,8]])).matrix), ("[[2,-3],[4,8]] * [[7.9,6],[7,8]]", matrixMult(Matrix([[2,-3],[4,8]]), Matrix([[7.9,6],[7,8]])).matrix)]

scalarMultTests = [("2 * [[5,6],[7,8]]", scalarMult(2, Matrix([[5,6],[7,8]])).matrix), ("[[5.7,6],[7,-8]] * 3", scalarMult(3, Matrix([[5.7,6],[7,-8]])).matrix)]

matrixPowerTests = [("[[5,6],[7,8]]^2", Matrix([[5,6],[7,8]]).power(2).matrix), ("[[5.7,6],[7,-8]] ^ 3", Matrix([[5.7,6],[7,-8]]).power(3).matrix)]



tests = addTests+ subTests+ multTests+ divTests+ modTests + exTests+ eqTests+ lessTests+ greatTests+ leqTests+geqTests+parenTests+orderOfOpsTests + decimalTests + matrixAddTests + matrixMultTests + matrixPowerTests + scalarMultTests

def test(l):
    correct = True
    for t in l:
        try:
            check = calcTest(t[0])
            if check != t[1]:
                print("Test produced incorrect result on " + t[0]+".")
                correct = False
        except:
            print("An error occured on test: " + t[0])
            correct == False
    if correct == True:
        print("All tests successful!")

def calcTest(exp):
    result = eval(parseEq(Tokens(exp)))
    if type(result) == Matrix:
        return result.matrix
    return result

test(tests)
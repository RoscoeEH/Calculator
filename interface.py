from calculator import *
from parser import *

print("Type any operation into the calculator below, when done type 'exit' to stop. It accepts real number inputs, pi, and e with with divison, multiplication, addition, subtraction, and exponents. It also accepts sin, cos, and tan. You can input matricies using python syntax for an array of arrays. The matricies support matrix multiplication, addition, scalar multiplication, determinant, transpose, and trace.\n")
while True:
    exp = input("Input:\n")
    if exp.upper() == "EXIT":
        break
    result = eval(parseEq(Tokens(exp)))
    print("\n")
    if type(result) == Matrix:
        print (result.display())
    else:
        print(result)
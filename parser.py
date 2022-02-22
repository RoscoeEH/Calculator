from helperFunctions import *

RESERVED = ["+", "-", "*", "/", "%", "^", "(", ")", "=", "<", ">", "<=", ">=",'sin','cos','tan', 'pi',"tr","det","T","e"]
LETTERS = "sincostanpitrdetT"

def build(string):
    tkns = []
    neg = False
    openBrackets = 0
    for t in string:
        if t == " ":
            pass
        elif t in RESERVED:
            if tkns != [] and t == "=" and (tkns[-1] == "<" or tkns[-1] == ">"):
                tkns[-1] += "="
            elif t == "-":
                if openBrackets > 0:
                    tkns[-1]+=t
                else:
                    if tkns == [] or not isNum(tkns[-1]):
                        neg = True
                    tkns.append(t)
            
            else:
                tkns.append(t)

        elif isNum(t):
            if openBrackets > 0:
                tkns[-1]+=t
            elif tkns != [] and isNum(tkns[-1]):
                tkns[-1] += t
            else:
                if neg == True:
                    tkns[-1] += t
                    neg = False
                else:
                    tkns.append(t)
        elif t == ".":
            if tkns!=[] and (isNum(tkns[-1]) or openBrackets > 0):
                tkns[-1] += "."
            else:
                raise SyntaxError("Cannot have '.' character without a digit before it.")
        elif t in LETTERS:
            if tkns != [] and tkns[-1] in LETTERS and tkns[-1] not in RESERVED:
                tkns[-1] += t
            else:
                tkns.append(t)
        elif t == "[":
            if openBrackets > 0:
                tkns[-1] += t
            else:
                tkns.append(t)
            openBrackets += 1
        elif t == "]":
            if openBrackets == 0:
                raise SyntaxError("Unmatched brackets.")
            openBrackets -= 1
            tkns[-1] += "]"
        elif t == ",":
            if openBrackets > 0:
                tkns[-1] += t
            else:
                raise SyntaxError('Unexpected token: ' + t)
    for t in tkns:
        if not isNum(t) and t not in RESERVED and not isMatrix(t):
            raise SyntaxError('Unrecognized token: ' + t)
    return tkns

class Tokens:
    def __init__(self, string):
        self.tkns = build(string)

    def next(self):
        if self.tkns != []:
            return self.tkns[0]

    def eat(self, t):
        if t == self.next():
            self.tkns = self.tkns[1:]
        else:
            raise SyntaxError('Expected: '+e+'. Saw: '+self.next()+ '.')

    def eatNum(self):
        if isNum(self.next()):
            x = self.next()
            self.tkns = self.tkns[1:]
            return x
        else:
            raise SyntaxError('Expected a number. Saw: '+self.next()+ '.')
    
    def eatMatrix(self):
        if isMatrix(self.next()):
            x = self.next()
            self.tkns = self.tkns[1:]
            return x
        else:
            raise SyntaxError('Expected a matrix. Saw: '+self.next()+ '.')


def parseEq(tkns):
    x = parseAdd(tkns)
    if tkns.next() == "=":
        tkns.eat("=")
        y = parseAdd(tkns)
        x = ["Eq", x,y]
    elif tkns.next() == "<":
        tkns.eat("<")
        y = parseAdd(tkns)
        x = ["Le", x,y]
    elif tkns.next() == ">":
        tkns.eat(">")
        y = parseAdd(tkns)
        x = ["Ge", x, y]
    elif tkns.next() == "<=":
        tkns.eat("<=")
        y = parseAdd(tkns)
        x = ["Leq", x, y]
    elif tkns.next() == ">=":
        tkns.eat(">=")
        y = parseAdd(tkns)
        x = ["Geq", x, y]
    return x

def parseAdd(tkns):
    x = parseMult(tkns)
    if tkns.next() == "+":
        tkns.eat("+")
        y = parseMult(tkns)
        x = ["Add", x, y]
    elif tkns.next() == "-":
        tkns.eat("-")
        y = parseMult(tkns)
        x = ["Sub", x, y]
    return x

def parseMult(tkns):
    x = parsePow(tkns)
    if tkns.next() == "*":
        tkns.eat("*")
        y = parsePow(tkns)
        x = ["Mult", x, y]
    elif tkns.next() == "/":
        tkns.eat("/")
        y = parsePow(tkns)
        x = ["Div", x, y]
    elif tkns.next() == "%":
        tkns.eat("%")
        y = parsePow(tkns)
        x = ["Mod", x, y]
    return x

def parsePow(tkns):
    x = parseAtom(tkns)
    if tkns.next() == "^":
        tkns.eat("^")
        y = parseAtom(tkns)
        x = ["Pow", x, y]
    return x

def parseAtom(tkns):
    if isNum(tkns.next()):
        n = tkns.eatNum()
        return ["Num", n]
    if isMatrix(tkns.next()):
        m = tkns.eatMatrix()
        return ["Mat", m]
    elif tkns.next() == "(":
        tkns.eat("(")
        x = parseEq(tkns)
        tkns.eat(")")
        return x
    elif tkns.next() == "sin":
        tkns.eat("sin")
        x = parseEq(tkns)
        return ["Sin", x]
    elif tkns.next() == "cos":
        tkns.eat("cos")
        x = parseEq(tkns)
        return ["Cos", x]
    elif tkns.next() == "tan":
        tkns.eat("tan")
        x = parseEq(tkns)
        return ["Tan", x]
    elif tkns.next() == "pi":
        tkns.eat("pi")
        return ["Pi"]
    elif tkns.next() == "e":
        tkns.eat("e")
        return ["E"]
    elif tkns.next() == "det":
        tkns.eat("det")
        x = parseEq(tkns)
        return ["Det", x]
    elif tkns.next() == "tr":
        tkns.eat("tr")
        x = parseEq(tkns)
        return ["Tr", x]
    elif tkns.next() == "T":
        tkns.eat("T")
        return ["T"]

    else:
        raise SyntaxError("Unexpected token: " + tkns.next())
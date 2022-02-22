def isNum(s):
    if s[0] == "-":
        if s[1:].isdigit() == True:
            return True
    if "." in s:
        decimal = s.index(".")
        return (s[:decimal] + s[decimal+1:]).isdigit()
    return s.isdigit()


def isMatrix(s):
    if s[0] != "[" or s[-1] != ']':
        return False
    open = False
    rowSize = 0
    currentSize = 0
    emptySpace = True
    for i in s[1:-1]:
        if i == "[":
            if open == True:
                return False
            open = True
        elif i == ",":
            if open == True:
                currentSize += 1
                if emptySpace == True:
                    return False
                emptySpace = True
        elif i == "]":
            if open == True:
                currentSize += 1
                open = False
                if rowSize != 0:
                    if rowSize != currentSize:
                        return False
                    currentSize = 0
                    
                else:
                    rowSize = currentSize
                    currentSize = 0
        elif i in ["-", "."] or i.isdigit():
            if open == False:
                return False
            if emptySpace == True:
                emptySpace = False
        elif i == " ":
            pass
        else:
            print (i)
            return False
    return True
        

def buildMatrix(s):
    s = s[1:-1]
    num = ""
    open = False
    array = []
    for i in s:
        if i == "[":
            row = []
            open = True
        elif i in [".","-"] or i.isdigit():
            num += i
        elif i == "," and open == True:
            row.append(float(num))
            num = ""
        elif i == "]":
            open = False
            n = float(num)
            if n%1==0:
                n = int(n)
            row.append(n)
            array.append(row)
            row = []
            num = ""
    return array



def maxElementLength(m):
    current = 0
    for row in m:
        for item in row:
            current = max(len(str(item)),current)
    return current

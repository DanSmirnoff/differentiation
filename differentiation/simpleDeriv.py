import diff
import helpFunc

def simplePow(function, n):     #n - number, not function
    if '.' in n:
        n = float(n)
    else:
        n = int(n)
    return str(n) + '*' + function + '^' + str(n-1)

def diffPower(function1, function2):
    if function1 == 'e':                
        if helpFunc.isNumber(function2):         #e.g e^2
            return '0'  
        else:                           #e.g e^sin
            return diff.distr(function2) + '*power(e,' + function2 + ')'
    elif helpFunc.isNumber(function1):
        if helpFunc.isNumber(function2):         #e.g 2^2
            return '0'
        else:                           #e.g 2^sin
            return 'log(e,' + function1 + ')*' + diff.distr(function2) + '*power(' + function1 + ',' + function2 + ')'
    else:
        if helpFunc.isNumber(function2):          
            if float(function2) >= 0:      #e.g sin^2 or sin^0.5
                if float(function2)%1 != 0:    #sin^0.5
                    return function2 + '*' + 'power(' + function1 + ',' + str(float(function2) - 1) + ')*(' + diff.distr(function1) + ')'
                else:                           #sin^2
                    return function2 + '*' + 'power(' + function1 + ',' + str(int(function2) - 1) + ')*(' + diff.distr(function1) + ')'
            else:                       #e.g sin^(-2) or sin^(-0.5)
                if float(function2)%1 != 0:    #sin^(-0.5)
                    return '(' + function2 + ')*' + 'power(' + function1 + ',' + str(float(function2) - 1) + ')*(' + diff.distr(function1) + ')'
                else:                           #sin^(-2)
                    return '(' + function2 + ')*' + 'power(' + function1 + ',' + str(int(function2) - 1) + ')*(' + diff.distr(function1) + ')'
        else:                           #e.g sin^cos
            return '(' + diff.distr(function1) + '*' + function2 + '*power(' + function1 + ',-1)' + '+' + 'log(e,' + function1 + ')*' + diff.distr(function2) + ')*power(' + function1 + ',' + function2 + ')'


def diffTrig(function):     #just simple derivates of triginometric functions
    if function == 'sin':
        return 'cos'
    elif function == 'cos':
        return '-sin'
    elif function == 'tg':
        return 'cos^(-2)'
    elif function == 'ctg':
        return '-sin^(-2)'

def diffLog(function1, function2):
    if function1 == 'e':                
        if helpFunc.isNumber(function2):         # e.g log(e, 2)
            return '0'  
        else:                           # e.g log(e, sin)
            return 'power(' + function2  + ',-1)*(' + diff.distr(function2) + ')'
    elif helpFunc.isNumber(function1):
        if helpFunc.isNumber(function2):         # e.g log(2, 2)
            return '0'
        else:  
            return 'power(log(e,' + function1 + '),-1)*' + 'power(' + function2  + ',-1)*(' + diff.distr(function2) + ')'
    else:                               # maybe needed to be fixed
        return diff.distr('log(e,' + function1 + ')*power(log(e,' + function2 + '),-1)')

def diffArc(function):
    if function == 'arcsin':
        return 'power(1-power(x,2),-0.5)'
    if function == 'arccos':
        return '-power(1-power(x,2),-0.5)'
    if function == 'arctg':
        return 'power(1+power(x,2),-1)'
    if function == 'arcctg':
        return '-power(1+power(x,2),-1)'
        
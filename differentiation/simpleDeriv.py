def simplePow(function, n):     #n - number, not function
    if '.' in n:
        n = float(n)
    else:
        n = int(n)
    return str(n) + '*' + function + '^' + str(n-1)

def trig(function):     #just simple derivates of triginometric functions
    if function == 'sin':
        return 'cos'
    elif function == 'cos':
        return '-sin'
    elif function == 'tg':
        return 'cos^(-2)'
    elif function == 'ctg':
        return '-sin^(-2)'

#def diffPow(a, b):  #a^b
    
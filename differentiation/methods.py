import simpleDeriv
import diff
import helpFunc

def multi(a, b):    #a*b
    c = diff.distr(a)
    d = diff.distr(b)
    return '(' + c + ')' + '*' + '(' + b + ')' + '+' + '(' + a + ')' + '*' + '(' + d + ')'

def comp(a, b):     #a(b)
    c = diff.distr(a)
    d = diff.distr(b)
    return c + '(' + b + ')*' + '(' + d + ')'

def div(a, b):      #a/b
    c = diff.distr(a)
    d = diff.distr(b)
    return '(' + '(' + c + ')' + '*' + '(' + b + ')' + '-' + '(' + a + ')' + '*' + '(' + d + ')' + ')/(' + b + ')^2'
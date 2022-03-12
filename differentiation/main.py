import diff
import methods
import simplif
import helpFunc
import time

equation = diff.converter(input())
equation = diff.distr(equation)
print('diff check - ' + equation)
print(simplif.simplificator(equation))

#print(helpFunc.replacer('xxxx', '.', '.g))